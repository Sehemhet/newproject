from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', home_def, name='home'),
    re_path(r'^register', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
]