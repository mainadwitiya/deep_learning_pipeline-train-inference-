
from django.urls import path
from .views import index

urlpatterns = [
  
    path('',index),
    #path('Select_Model',index)
]
