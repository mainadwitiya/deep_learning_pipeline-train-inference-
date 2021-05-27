from django.shortcuts import render
from rest_framework import generics #class that inherits from generic api view
from django.http import HttpResponse
from .models import Model_Data
from .serializers import Model_Data_Serializer
from .serializers import PostSerializer
from .models import Post
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

# def effed(request):
#     return HttpResponse("<h2>hello</h2>")


#CREATE API VIEW
# class ModelView(generics.ListAPIView):
#     queryset= Model_Data.objects.all()
#     serializer_class = Model_Data_Serializer
    
#CREATE API VIEW
class ModelView(generics.CreateAPIView):
    queryset= Model_Data.objects.all()
    serializer_class = Model_Data_Serializer
    
class PostView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        posts_serializer = PostSerializer(data=request.data)
        if posts_serializer.is_valid():
            posts_serializer.save()
            print(posts_serializer.data)
            print('Sahi se upload hui image')
            return Response(posts_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', posts_serializer.errors)
            return Response(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)