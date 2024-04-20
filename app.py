from flask import Flask, request, jsonify
import pandas as pd
from sklearn.preprocessing import StandardScaler
import pickle
import joblib
import json
scaler = StandardScaler()
app = Flask(__name__)


# Function to load models from .pkl file
def load_models(file_path):
    with open(file_path, 'rb') as file:
        models = pickle.load(file)
    return models

# Load models when the Flask app starts
model_file_path = "model_dictionary.pkl"
models = load_models(model_file_path)
scaler_path = 'scaler.pkl'
scaler = joblib.load(scaler_path)


@app.route('/predict', methods=['POST'])
def predict():
    data = request.json  # get input data from the request
    print(data)
    custom_data = {}
    for ele in data:
        custom_data[ele] = [float(data[ele])]
    print(custom_data)
    custom_scaled = scaler.transform(pd.DataFrame(custom_data))
    custom_predictions = {}
    # Use your machine learning model to make predictions
    tree_pollen_values = 0
    grass_pollen_values = 0
    weed_pollen_values = 0
    tree_pollen = ['Ambrosia', 'Artemisia', 'Alnus', 'Betula', 'Carpinus', 'Castanea', 'Quercus',
               'Cupressaceae', 'Acer', 'Fraxinus', 'Fagus', 'Aesculus', 'Larix', 'Corylus',
                    'Juglans', 'Ulmus', 'Populus', 'Pinaceae', 'Platanus', 'Salix', 'Filipendula',
                    'Sambucus', 'Tilia']
    grass_pollen = ['Gramineae', 'Juncaceae', 'Cyperaceae']
    weed_pollen = ['Asteraceae', 'Chenopodium', 'Umbellifereae', 'Urtica', 'Rumex', 'Plantago']
    for column, model in models.items():
        custom_predictions[column] = float(model.predict(custom_scaled))
        if(column in tree_pollen):
            tree_pollen_values += custom_predictions[column]
        elif(column in grass_pollen):
            grass_pollen_values += custom_predictions[column]
        else:
            weed_pollen_values += custom_predictions[column]
        print(f"Pollen values for {column}: {custom_predictions[column]}")
    print(type(custom_predictions['Ambrosia']))
    return jsonify({'predictions':[tree_pollen_values,grass_pollen_values,weed_pollen_values]})


@app.route('/', methods=['GET'])
def message():
    return "Hello"

if __name__ == '_main_':
    app.run(debug=True)