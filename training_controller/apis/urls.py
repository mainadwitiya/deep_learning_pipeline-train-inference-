
from django.urls import path
from .views import *

from . import views
urlpatterns = [
  
    #path('models',ModelView.as_view()),
    path('model_records/', views.PostView_Model_Selection_TF.as_view(), name= 'posts_list'),
#     path('tf_config_file_edited/',views.PostView_Tf_Config_File.as_view(),name='config_data')
]
