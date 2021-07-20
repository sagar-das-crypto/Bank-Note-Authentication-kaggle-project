# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 18:00:49 2021

@author: das10
"""
import pandas as pd
import numpy as np
from flask import Flask, request
import pickle
import flasgger
from flasgger import Swagger

app= Flask(__name__)
Swagger(app)
pickle_in=open("classifier.pkl", "rb")
classifier= pickle.load(pickle_in)

@app.route("/")
def welcome():
    return "welcome all"

@app.route("/predict", methods=["GET"])
def predict_note_authentication():
    """Let"s authentictae the bank notes
    this is using docstrings
    ---
    parameters:
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: the output values
    
    """
    
    variance=request.args.get("variance")
    skewness=request.args.get("skewness")
    curtosis=request.args.get("curtosis")
    entropy=request.args.get("entropy")
    
    prediction= classifier.predict([[variance, skewness, curtosis, entropy]])
    return "the prediciton value is"+str(prediction)



    


if __name__=="__main__":
    app.run()

