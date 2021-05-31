from django.shortcuts import render
from rest_framework import generics #class that inherits from generic api view
from django.http import HttpResponse
from .models import Model_Post
#from .serializers import Model_Data_Serializer
from .serializers import PostSerializer
from .models import Model_Post
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from django.http import FileResponse
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
def response_data(model_type):
    if model_type=='centernet':
        file_path='apis/configs/tf2/centernet_hourglass104_512x512_coco17_tpu-8.config'
    return file_path
class PostView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        posts = Model_Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
    
            

    def post(self, request, *args, **kwargs):
        posts_serializer = PostSerializer(data=request.data)
        #print(request.data.model_type)
        if posts_serializer.is_valid():
            #print(posts_serializer)
            posts_serializer.save()
            print(posts_serializer.data['model_type'])
            
            xxx=response_data(posts_serializer.data['model_type'])
            img = open(xxx, 'rb')
            response = FileResponse(img)
            print(response)
            print('Sahi se upload hui image')
            
            #return Response(posts_serializer.data, status=status.HTTP_201_CREATED)
            return response
            
        else:
            print('error', posts_serializer.errors)
            return Response(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
            