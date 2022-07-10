import pandas as pd
import numpy as np
from flask import Flask, request, jsonify
import pickle
import yaml
from yaml.loader import SafeLoader
from sklearn.pipeline import make_pipeline
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import OneHotEncoder
from utils.preprocess import Pipeline
from utils.experiment_1_features import *


app = Flask(__name__)


# Obtener parámetros
def get_params(resources_path = 'models/prod/params.yaml'):
    with open(resources_path, 'r') as f:
        resources = yaml.load(f, Loader=SafeLoader)
    return resources


# Carga de artefacto
def get_artifact(path):
    with open(path, 'rb') as infile:
        artifact = pickle.load(infile)
    return artifact


def process_input_data(data):
    data = pipeline.apply(data, params)
    data = scikit_pipeline.transform(data)
    return data


# Guardo el modelo y el pipeline para hacer las predicciones
params = get_params()
model = get_artifact(params.get('prod_model_path'))
pipeline = get_artifact(params.get('prod_pipeline_path'))
scikit_pipeline = get_artifact(params.get('prod_scikit_pipeline_path'))


# Definición de métodos HTTP
@app.route('/api', methods = ['POST'])
def predict():
    data = request.get_json(force=True)

    # Transformación de los datos de entrada
    data = pd.DataFrame.from_dict(data)
    data = process_input_data(data)

    # Predicción
    prediction = model.predict(data)[0]
    if prediction <= 0:
        prediction = 0

    return jsonify(prediction)


if __name__ == '__main__':
    app.run(port=5000, debug=True)