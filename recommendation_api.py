import uvicorn

import pickle

import numpy as np
import pandas as pd

from fastapi import FastAPI

from flask import jsonify

new_pt = pickle.load(open('new_pt.pkl', 'rb'))
new_similarity_scores = pickle.load(open('new_similarity_scores', 'rb'))
doctor_df = pickle.load(open('doctor_df.pkl', 'rb'))

app = FastAPI()

@app.get('/{int},{area}')
def recommend(int, area):
    doctor_df[['int', 'area']] == (int, area)
    groups = doctor_df.groupby(['int'])
    result = groups.get_group(int)
    return {'recommendation':result}
  
# run api with uvicorn
if __name__ == '__main__':
    uvicorn.run(app, host = '127.0.0.1', port = 8000)