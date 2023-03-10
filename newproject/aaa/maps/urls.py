from django.urls import path
from .views import *

urlpatterns = [
    path('', maps, name='map')
]