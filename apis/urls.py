
from django.urls import path
from .views import ModelView

urlpatterns = [
  
    path('models',ModelView.as_view())
]
