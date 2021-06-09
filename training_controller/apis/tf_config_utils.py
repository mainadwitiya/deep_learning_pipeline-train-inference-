
import argparse
import pandas as pd
import json
import tensorflow as tf
from google.protobuf import text_format
from object_detection.protos import pipeline_pb2

import os

def read_label_map(label_map_path):

    item_id = None
    item_name = None
    items = {}
    print(label_map_path)
    print('xxxxxxxxxxxxxxxxxxxxx',os.getcwd())
    with open(label_map_path, "r") as file:
        for line in file:
            
            line.replace(" ", "")
            if line == "item{":
                pass
            elif line == "}":
                pass
            elif "id" in line:
                item_id = line.split(":", 1)[1].strip()
            elif "name" in line:
                item_name = line.split(":", 1)[1].replace("'", "").strip()

            if item_id is not None and item_name is not None:
                items[item_name] = item_id
                item_id = None
                item_name = None

    return items


def configure_the_pipeline_file_tf_faster_rcnn(config_file_path,label_path,checkpoint_path,train_record_file,test_record_file)->str:
    '''
     arg:config_file_path
     desc: path to the original config_path,
     
     arg:label_path
     desc: label_map_path from user,
     
     arg:checkpoint_path
     desc:initial checkpoint path of the pre-trained model,
     
     arg:train_record_file_path
     desc:train_record file generated or from user,
     
     
     arg:test_record_file_path
     desc:train_record file generated or from user,
     
     
     arg:final_config_path
     desc:final_config_path,
     
     
     returns: final_config_path
    '''
    pipeline_config = pipeline_pb2.TrainEvalPipelineConfig()
    print(pipeline_config)
    with tf.io.gfile.GFile(config_file_path, "r") as f:                                                                                                                                                                                                                     
        proto_str = f.read()                                                                                                                                                                                                                                          
        text_format.Merge(proto_str, pipeline_config)
    classes_dict=read_label_map(label_path)
    print(len(classes_dict))
    pipeline_config.model.faster_rcnn.num_classes=len(classes_dict)
    pipeline_config.train_config.fine_tune_checkpoint=checkpoint_path
    pipeline_config.train_config.fine_tune_checkpoint_type='detection'
    pipeline_config.train_config.batch_size=int(1)
    
    
    pipeline_config.train_input_reader.label_map_path=label_path
    pipeline_config.train_input_reader.tf_record_input_reader.input_path[:]=[train_record_file]
    pipeline_config.eval_input_reader[0].label_map_path=label_path
    pipeline_config.eval_input_reader[0].tf_record_input_reader.input_path[:]=[test_record_file]

    print(pipeline_config)
    pipeline_config.train_config.fine_tune_checkpoint='lol'
    config_text = text_format.MessageToString(pipeline_config)                                                                                                                                                                                                        
    with tf.io.gfile.GFile(final_config_file, "wb") as f:                                                                                                                                                                                                                       
        f.write(config_text)
    
    return final_config_file_path