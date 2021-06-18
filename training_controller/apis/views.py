from django.shortcuts import render
from rest_framework import generics #class that inherits from generic api view
from django.http import HttpResponse
from .models import *
#from .serializers import Model_Data_Serializer
from .serializers import Tf_Model_PostSerializer
# Tf_Config_File_Post_Seralizer
from .models import Model_Post
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from django.http import FileResponse
import argparse
import json

from .tf_config_utils import configure_the_pipeline_file_tf_faster_rcnn
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

 

    
    

def get_original_config_files(model_arch_type):
    print('inside reponse data')
    if model_arch_type=='centernet':
        config_file_path='apis/tf_base_od_models/ssd_mobilenet_v1_fpn_640x640_coco17_tpu-8/pipeline.config'
    elif model_arch_type=='fasterrcnn':
        config_file_path='apis/tf_base_od_models/faster_rcnn_resnet101_v1_640x640_coco17_tpu-8/pipeline.config'
    return config_file_path




def get_original_checkpoint_files(model_arch_type):
    print('inside reponse data')
    if model_arch_type=='fasterrcnn':
        checkpoint_path='apis/tf_base_od_models/faster_rcnn_resnet101_v1_640x640_coco17_tpu-8/checkpoint/ckpt-0'
    elif model_arch_type=='centernet':
        checkpoint_path='apis/tf_base_od_models/ssd_mobilenet_v1_fpn_640x640_coco17_tpu-8/checkpoint/ckpt-0'
    return checkpoint_path


class PostView_Model_Selection_TF(APIView): 

    parser_classes = (MultiPartParser, FormParser)

    # def get(self, request, *args, **kwargs):
    #     posts = Model_Post.objects.all()
    #     serializer = Tf_Model_PostSerializer(posts, many=True)
    #     return Response(serializer.data)
    
    
            

    def post(self, request, *args, **kwargs):
        obj=Model_Post()
        unique_uuid=obj.make_uuid_value()
        print(unique_uuid)
        posts_serializer = Tf_Model_PostSerializer(data=request.data)
        if posts_serializer.is_valid():
            posts_serializer.save()
            print(posts_serializer.data)
                       
            
            config_file_path=get_original_config_files(posts_serializer.data['model_arch_type'])
            print('xxxxxxxxxxxxxxxx',config_file_path)
            label_path=posts_serializer.data['label_file_data']
            print('yyyyyyyyyyyyyyyyyyyyyyyy',label_path)
            checkpoint_path=get_original_checkpoint_files(posts_serializer.data['model_arch_type'])
            
            
            train_record_file=posts_serializer.data['training_data']
            test_record_file=posts_serializer.data['test_data']
            final_config_file_path=new_path='/'+test_record_file.split('/')[1]+'/'+test_record_file.split('/')[2]+'/'
            final_path=configure_the_pipeline_file_tf_faster_rcnn(config_file_path,label_path,checkpoint_path,train_record_file,test_record_file)
            info_dict=obj.json_file_info_save(posts_serializer.data['usecase_type'],posts_serializer.data['framework_type'],posts_serializer.data['model_arch_type'],unique_uuid) 
            with open(os.path.join('post_data',str(unique_uuid),'file.json'),'w+')as f:
                f.write(json.dumps(info_dict))
            print(info_dict)
            
            print('===================================')
            print(info_dict.keys())
            img = open(final_path, 'rb')
            response = FileResponse(img)
            print(response)
           
            return response  
        else:
            print('error', posts_serializer.errors)
            return Response(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# class PostView_Tf_Config_File(APIView):
#     def post(self,request,*args,**kwargs):
#         post_serealizers=PostSerializer(data='request.data')
        
        
              