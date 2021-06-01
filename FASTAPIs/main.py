
import os
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("API.log")
formatter = logging.Formatter('%(asctime)s :: %(module)s :: %(levelname)s :: %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
from fastapi import FastAPI, File, UploadFile


def logger_output(message,level=2):
    
    if level==1:
        logger.info(message)
    elif level==2:
        logger.info(message)
    elif level==3:
        logger.exception(message)

    return

 
from fastapi import FastAPI, File, UploadFile,Depends
import json
from datetime import datetime, timedelta
from typing import Optional
from typing import Any, Dict, AnyStr, List, Union
import time
from fastapi import Depends, FastAPI, HTTPException, status,Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from jose import jws, jwt
# from jose.exceptions import JWTError
from passlib.context import CryptContext
from pydantic import BaseModel


from typing import IO

from tempfile import NamedTemporaryFile
import shutil

from fastapi import FastAPI, File, Header, Depends, UploadFile, HTTPException
from starlette import status


async def valid_content_length(content_length: int = Header(..., lt=80_000)):
    return content_length


app = FastAPI()


class File_info_training(BaseModel):
    title:str
    content:str
    
    
class Pipeline_config_upload(BaseModel):
    model_type:str
    model_architecture:str




# @app.post('/files/pipeline_upload')
# async def upload_config()

@app.post("/files/upload")
async def create_file(file: UploadFile = File(...),file_info:File_info_training=Depends()):
    global upload_folder
    upload_folder='upload_folder/'
    file_object = file.file
    print(file_info.title)
    print(file_info.content)
    #create empty file to copy the file_object to
    upload_folder = open(os.path.join(upload_folder, file.filename), 'wb+')
    shutil.copyfileobj(file_object, upload_folder)
    upload_folder.close()
    return {"filename": file.filename}



from fastapi import FastAPI
from fastapi.responses import FileResponse

some_file_path = "centernet_hourglass104_1024x1024_kpts_coco17_tpu-32.config"




@app.post("/config_file_path")
async def send_config_file(obj:Pipeline_config_upload):
    model_type=obj.model_type
    model_architecture=obj.model_architecture
    if model_architecture=='centernet_hourglass':
        file_path=some_file_path
    
    print(model_type)    
    return FileResponse(file_path)
    
    

# @app.get("/lol")
# async def myfile():
#     print()
#     return FileResponse(some_file_path)

# @app.post("/uploadfile/")
# async def create_upload_file(file: UploadFile = File(...)):
#     return 1

