import pandas as pd
import numpy as np
from flask import Flask, request, jsonify
import pickle
import yaml
from yaml.loader import SafeLoader
import utils.preprocess as p
from sklearn.pipeline import make_pipeline
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import OneHotEncoder


app = Flask(__name__)


def get_params(resources_path = 'models/resources.yaml'):
    with open(resources_path, 'r') as f:
        resources = yaml.load(f, Loader=SafeLoader)
    return resources.get('preprocess_params')

# Carga de modelo productivo
def get_model(resources_path = 'models/resources.yaml'):
    with open(resources_path, 'r') as f:
        resources = yaml.load(f, Loader=SafeLoader)
        path = resources.get('prod_model_path')
    with open('models/' + path, 'rb') as infile:
        model = pickle.load(infile)
    return model


def get_pipeline(resources_path = 'models/resources.yaml'):
    with open(resources_path, 'r') as f:
        resources = yaml.load(f, Loader=SafeLoader)
        path = resources.get('prod_pipeline_path')
    with open('models/' + path, 'rb') as infile:
        pipeline = pickle.load(infile)
    return pipeline


def process_input_data(data):
    preprocess_f_list = [p.create_country_features,
                         p.create_source_features, p.create_platform_features, p.create_device_features,
                         p.create_event_1_flag, p.create_event_2_flag, p.drop_metadata_columns
    ]
    data = p.apply_pipeline(preprocess_f_list, data, params)
    return pipeline.transform(data)


# Guardo el modelo y el pipeline para hacer las predicciones
model = get_model()
pipeline = get_pipeline()
params = get_params()


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