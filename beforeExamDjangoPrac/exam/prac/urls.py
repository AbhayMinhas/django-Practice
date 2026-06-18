from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='prac-home'),
    path('result/',views.res,name='prac-res'),
]