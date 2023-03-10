"""aaa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

from news import views as news_views
from auto import views as auto_views
from garage import views as garage_views


news_patterns = [
    path('post/<slug:slug>/', news_views.post_detail.as_view(), name='post'),
    path('category/<slug:slug>/', news_views.post_category.as_view(), name='post_category'),
    path('', news_views.post_list.as_view(), name='post_list'),
    path('create/', news_views.post_create.as_view(), name='post_create'),
]

garage_urlpatterns = [
    path('<slug>/', garage_views.my_car.as_view(), name='mycar'),
    path('', garage_views.garage.as_view(), name='garage'),
]

auto_patterns = [
    # path(r'\w+/<slug:slug>/', auto_views.car_detail.as_view(), name='cars'),           #Работает
    # path(r'\w+/(?=<slug:slug>)/', auto_views.car_detail.as_view(), name='cars'),           #Работает
    # path(r'[.]/<slug:slug>/', auto_views.car_detail.as_view(), name='cars'),           #Работает
    # path('/<slug>', auto_views.car_detail.as_view(), name='cars'),           #Работает проще всех
    re_path(r'^/(?P<slug_car>[-\w]+)/$', auto_views.car_detail.as_view(), name='cars'),
    # path(r'^\[.]{1,40}/<slug:slug>/', auto_views.car_detail.as_view(), name='cars'),    #Работает
    # re_path(r'^(?P<slug>\w+)/$', auto_views.car_detail.as_view(), name='cars'),
    re_path(r'^(?P<slug_brand>[-\w]+)/$', auto_views.model_list.as_view(), name='brands'),
    # re_path(r'^/(?P<slug_brand>[a-z]+)/$', auto_views.model_list.as_view(), name='brands'),
    re_path(r'^', auto_views.brand_list.as_view(), name='auto'),
    path('create/', auto_views.car_create.as_view(), name='car_create'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('garage/', include(garage_urlpatterns)),
    path('map/', include('maps.urls')),
    re_path(r'^', include('b1.urls')),
    path('news/', include(news_patterns)),
    path('auto/', include(auto_patterns)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)