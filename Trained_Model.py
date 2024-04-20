import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import GradientBoostingRegressor
import pickle
import joblib

# Load the dataset
data = pd.read_csv('pollen_luxembourg.csv')

# Select the features (MaxAirTempC, MinAirTempC, PrecipitationC) and the target variables
X = data[['MaxAirTempC', 'MinAirTempC', 'PrecipitationC']]
y = data[['Ambrosia', 'Artemisia', 'Asteraceae', 'Alnus', 'Betula', 'Ericaceae', 'Carpinus', 'Castanea', 'Quercus',
          'Chenopodium', 'Cupressaceae', 'Acer', 'Fraxinus', 'Gramineae', 'Fagus', 'Juncaceae', 'Aesculus', 'Larix',
          'Corylus', 'Juglans', 'Umbellifereae', 'Ulmus', 'Urtica', 'Rumex', 'Populus', 'Pinaceae', 'Plantago',
          'Platanus', 'Salix', 'Cyperaceae', 'Filipendula', 'Sambucus', 'Tilia']]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
scaler_path = 'scaler.pkl'
joblib.dump(scaler, scaler_path)

# Initialize KNN models for each target variable
models = {}
for column in y.columns:
    model = GradientBoostingRegressor(n_estimators=100, random_state=42)  # Use KNeighborsClassifier for KNN
    model.fit(X_train_scaled, y_train[column])
    models[column] = model

# Define the file path where you want to save the model dictionary
file_path = "model_dictionary.pkl"

# Open the file in binary write mode
with open(file_path, 'wb') as file:
    # Dump the model dictionary into the file
    pickle.dump(models, file)

print(f"Model dictionary saved to {file_path}")


# Define the file path from where you want to load the model dictionary
file_path = "model_dictionary.pkl"

# Open the file in binary read mode
with open(file_path, 'rb') as file:
    # Load the model dictionary from the file
    loaded_models = pickle.load(file)

# Now you can use the loaded_models dictionary in your code


