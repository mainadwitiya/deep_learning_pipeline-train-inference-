from django.db import models
import string,random

# Create your models here.

class Model_Data(models.Model):
    model_id=models.CharField(max_length=8,unique=True)
    model_name = models.CharField(max_length=8,default="",unique=True)
    model_type=models.CharField(max_length=20,unique=False)
    created_at=models.DateTimeField()
    
    
    def generate_unique_id():
        length=8
        while True:
            model_id=''.join(random.choices(string.ascii_uppercase,k=length))
            if Model_Data.objects.filter(model_id=model_id).count()==0:
                break
            
        return model_id
    

    