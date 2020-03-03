#work in progress

import fastai 
from fastai.vision import *
import joblib
import json
import pathlib
from pathlib import Path
import numpy as np
import torch


from azureml.core.model import Model


def init():
    global model
    # note here "food_classification_model" is the name of the model registered under the workspace, this call should return the path to the model.pkl file on the local disk
    model_path = Model.get_model_path('food_classification_model')
    model = joblib.load(model_path)

    
def run(input_data):
    #convert list to array 
    nparray = np.array(input_data)    
    #convert array to fastai image 
    img_fastai = Image(pil2tensor(nparray, dtype=np.float))
    img = open_image(img_fastai)     
    pred_class,pred_idx,outputs = model.predict(img)
    #return pred_class
    return json.dumps({"result": pred_class.tolist()})
    


