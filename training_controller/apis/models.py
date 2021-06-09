from django.db import models
import string,random
import os
import uuid



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

  
def user_directory_path(usecase_type):
    return 'post_data/'+str(id)


def create_path(instance,usecase_type):
    print(usecase_type)
    #print(os.path.join('post_data',model_id))
    return os.path.join('post_data',id)

def group_based_upload_to(instance, filename):
    

    return "apis/post_data/{}/{}".format(instance.uniqueid, filename)



class Model_Post(models.Model):
    uniqueid = uuid.uuid1()
    #model_id = model_type=models.CharField(max_length=100)
    usecase_type = models.CharField(max_length=100)
    framework_type = models.CharField(max_length=100)
    model_arch_type =models.CharField(max_length=100)
    training_data = models.FileField(upload_to=group_based_upload_to)
    test_data = models.FileField(upload_to=group_based_upload_to)
    label_file_data= models.FileField(upload_to=group_based_upload_to)
    
    def make_uuid_value(self):
        return self.uniqueid

    def json_file_info_save(self,usecase_type,framework_type,model_arch_type,uniqueid):
        info_dict={'usecase_type':usecase_type,'framework_type':framework_type,'model_arch_type':model_arch_type}
        
        return info_dict
        


# class Tf_Config_File_Post(models.Model):
#     uniqueid = models.CharField(max_length=100)
#     label_file_data= models.FileField(upload_to=group_based_upload_to)
    


 