from django.shortcuts import render
from rest_framework import generics #class that inherits from generic api view
from django.http import HttpResponse
from .models import Model_Data
from .serializers import Model_Data_Serializer
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