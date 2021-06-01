from django.db import models
import string,random
import os
import tensorflow as tf
from google.protobuf import text_format
from object_detection.protos import pipeline_pb2

# Create your models here.

# class Model_Data(models.Model):
#     model_id=models.CharField(max_length=8,unique=True)
#     model_name = models.CharField(max_length=8,default="",unique=True)
#     model_type=models.CharField(max_length=20,unique=False)
#     created_at=models.DateTimeField()
    
    
#     def generate_unique_id():
#         length=8
#         while True:
#             model_id=''.join(random.choices(string.ascii_uppercase,k=length))
#             if Model_Data.objects.filter(model_id=model_id).count()==0:
#                import argparse



#         return model_id

  
def user_directory_path(model_id):
    return 'post_data/'+str(model_id)


def create_path(instance,model_id):
    print(model_id)
    #print(os.path.join('post_data',model_id))
    return os.path.join('post_data',model_id)

def group_based_upload_to(instance, filename):
    return "post_data/{}/{}".format(instance.model_id, filename)

    
class Model_Post(models.Model):
    
    
    
    model_id = models.CharField(max_length=32)
    title = models.CharField(max_length=100)
    content = models.TextField()
    model_type=models.CharField(max_length=100)
    
    training_data = models.FileField(upload_to=group_based_upload_to)
    test_data = models.FileField(upload_to=group_based_upload_to)
    label_file_data= models.FileField(upload_to=group_based_upload_to)
    def __str__(self):
        return self.title
