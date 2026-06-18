from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='traffic-home'),
    path('display/',views.displaydata,name='display-data'),
    path('error/',views.error,name='display-error'),
]