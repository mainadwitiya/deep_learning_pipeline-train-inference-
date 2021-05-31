from rest_framework import serializers
from .models import Model_Post


# class Model_Data_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model=Model_Data
#         fields=('id','model_id','model_name','model_type','created_at')
        

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model_Post
        fields = '__all__'
