from django.urls import path,include
from . import views
urlpatterns = [
    
    path('',views.home,name='plant-home'),
    path('pot/',views.pot,name='pot-colour'),
]