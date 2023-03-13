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
from b1 import views as b1_views
from maps import views as maps_views

user_url = [
    path('', b1_views.home_def, name='home'),
    re_path(r'^register', b1_views.RegisterUser.as_view(), name='register'),
    path('login/', b1_views.LoginUser.as_view(), name='login'),
    path('logout/', b1_views.logout_user, name='logout'),
]

news_url = [
    path('post/<slug:slug>/', news_views.post_detail.as_view(), name='post'),
    path('category/<slug:slug>/', news_views.post_category.as_view(), name='post_category'),
    path('', news_views.post_list.as_view(), name='post_list'),
    path('create/', news_views.post_create.as_view(), name='post_create'),
]

garage_url = [
    path('<slug>/', garage_views.my_car.as_view(), name='mycar'),
    path('', garage_views.garage.as_view(), name='garage'),
]

auto_url = [
    re_path(r'^/(?P<slug>[-\w]+)/$', auto_views.car_detail.as_view(), name='cars'),
    re_path(r'^(?P<slug>[-\w]+)/$', auto_views.model_list.as_view(), name='brands'),
    re_path(r'^', auto_views.brand_list.as_view(), name='auto'),
]

map_url = [
    path('', maps_views.maps, name='map')
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('garage/', include(garage_url)),
    path('map/', include(map_url)),
    re_path(r'^', include(user_url)),
    path('news/', include(news_url)),
    path('auto/', include(auto_url)),
    path('newcar/', auto_views.car_create.as_view(), name='newcar'),
    path('captcha/', include('captcha.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)