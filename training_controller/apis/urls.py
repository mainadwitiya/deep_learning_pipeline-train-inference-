
from django.urls import path
from .views import PostView

from . import views
urlpatterns = [
  
    #path('models',ModelView.as_view()),
    path('model_records/', views.PostView.as_view(), name= 'posts_list')
]
