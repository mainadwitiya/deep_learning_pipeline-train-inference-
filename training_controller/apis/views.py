from django.shortcuts import render
from rest_framework import generics #class that inherits from generic api view
from django.http import HttpResponse
from .models import *
#from .serializers import Model_Data_Serializer
from .serializers import Tf_Model_PostSerializer,Tf_Config_File_Post_Seralizer
from .models import Model_Post
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from django.http import FileResponse
import argparse

# import tensorflow as tf
# from google.protobuf import text_format
# from object_detection.protos import pipeline_pb2


# Create your views here.

# def effed(request):
#     return HttpResponse("<h2>hello</h2>")


#CREATE API VIEW
# class ModelView(generics.ListAPIView):
#     queryset= Model_Data.objects.all()
#     serializer_class = Model_Data_Serializer
    
#CREATE API VIEW
# class ModelView(generics.CreateAPIView):
#     queryset= Model_Data.objects.all()
#     serializer_class = Model_Data_Serializer

def edit_data(config_file_path):
    pipeline_config = pipeline_pb2.TrainEvalPipelineConfig()
    print(pipeline_config)
    with tf.io.gfile.GFile(file_path, "r") as f:                                                                                                                                                                                                                     
        proto_str = f.read()                                                                                                                                                                                                                                          
        text_format.Merge(proto_str, pipeline_config) 
    pipeline_config.train_input_config.label_map_path= "123/label_map.txt"
    pipeline_config.model.ssd.image_resizer.fixed_shape_resizer.height = 300                                                                                                                                                                                          
    pipeline_config.model.ssd.image_resizer.fixed_shape_resizer.width = 300

    config_text = text_format.MessageToString(pipeline_config)                                                                                                                                                                                                        
    with tf.io.gfile.GFile(path_2, "wb") as f:                                                                                                                                                                                                                       
        f.write(config_text)  

    
    

def response_data(model_arch_type):
    print('inside reponse data')
    if model_arch_type=='centernet':
        config_file_path='apis/configs/tf2/centernet_hourglass104_512x512_coco17_tpu-8.config'
    elif model_arch_type=='fasterrcnn':
        config_file_path='apis/configs/tf2/faster_rcnn_resnet50_v1_640x640_coco17_tpu-8.config'
    return config_file_path

class PostView_Model_Selection_TF(APIView): 

    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        posts = Model_Post.objects.all()
        serializer = Tf_Model_PostSerializer(posts, many=True)
        return Response(serializer.data)
    
    
            

    def post(self, request, *args, **kwargs):
        posts_serializer = Tf_Model_PostSerializer(data=request.data)
        if posts_serializer.is_valid():
            posts_serializer.save()
            xxx=response_data(posts_serializer.data['model_arch_type'])
            img = open(xxx, 'rb')
            response = FileResponse(img)
            print(response)
            print('Sahi se upload hui image')
            return response  
        else:
            print('error', posts_serializer.errors)
            return Response(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class PostView_Tf_Config_File(APIView):
    def post(self,request,*args,**kwargs):
        post=serealizers=PostSerializer(data='request.data')
              