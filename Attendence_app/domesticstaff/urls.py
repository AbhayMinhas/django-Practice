from django.urls import path,include
from . import views
urlpatterns = [
    
    path('',views.attendenceForm,name="home-form"),
    path('/result',views.Mark,name="is-Marked")
]