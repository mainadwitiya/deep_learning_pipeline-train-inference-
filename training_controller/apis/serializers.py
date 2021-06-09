from rest_framework import serializers
from .models import Model_Post
# Tf_Config_File_Post

# class Model_Data_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model=Model_Data
#         fields=('id','model_id','model_name','model_type','created_at')
        

class Tf_Model_PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model_Post
        fields = '__all__'

# class Tf_Config_File_Post_Seralizer(serializers.ModelSerializer):
#     class Meta:
#         model=Tf_Config_File_Post
#         fields='__all__'