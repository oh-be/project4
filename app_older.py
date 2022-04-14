import numpy as np
import pandas as pd
from flask import Flask, request, render_template
from sklearn import preprocessing
from pycaret.regression import *
import Pipeline
import pickle


app = Flask(__name__)
model = load_model('Regression_insurance_model.pkl')
model2 = load_model('Regression_maintenance_model.pkl')
model3 = load_model('Regression_rent_model.pkl')
model4 = load_model('Regression_tax_model.pkl')
cols=['Latitude', 'Longitude', 'SalePrice']

@app.route('/') 
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    feature_list = request.form.to_dict()
    feature_list = list(feature_list.values())
    feature_list = list(map(int, feature_list))
    Latitude,Longitude,total_price = feature_list
    final_features = np.array(feature_list).reshape(1, 3) 
    
    prediction = model.predict(final_features)
    prediction2 = model2.predict(final_features)
    prediction3 = model3.predict(Latitude,Longitude)
    prediction4 = model4.predict(final_features)
    
    insurance = int(prediction[0])
    maintenance = int(prediction2[0])
    rent = int(prediction3[0])
    taxes = int(prediction4[0] / 12)
    
    return int(total_price, insurance, maintenance, rent, taxes)

@app.route('/pipeline',methods=['POST'])
def pipeline():
    pipe_data = Pipeline.investment_calc(total_price, insurance, maintenance, rent, taxes)
    return render_template('index.html', prediction_text = pipe_data)

if __name__ == "__main__":
    app.run(debug=True)