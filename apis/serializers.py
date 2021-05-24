from rest_framework import serializers
from .models import Model_Data


class Model_Data_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Model_Data
        fields=('id','model_id','model_name','model_type','created_at')