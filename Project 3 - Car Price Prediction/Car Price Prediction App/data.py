import streamlit as st
import pickle
from category_encoders import LeaveOneOutEncoder

desc_temp = """
            This app will be used to by someone to make a prediction about a car price that he/her want to sell and make a good transaction
            #### Data Source
            - https://www.kaggle.com/datasets/deepcontractor/car-price-prediction-challenge
            #### App Content
            - Home: This section provides an overview of the application's purpose and its data sources.
            - Machine Learning: In this section, users can input data and predict visitor customer segmentation based on information about the dataset. 
            """

css = """
    <style>
        .elegant-text {
            font-family: 'Times New Roman', Times, serif;
            font-size: 25px;
            color: #654321; /* Coklat muda */
            text-align: center;
            background: linear-gradient(to right, #654321, #3e2723); /* Transisi dari coklat muda ke coklat tua */
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
    </style>
"""


# information about attribute
attribute_info = """
                - Price: The price of the car in a specific currency unit.
                - Levy: Additional fee charged on imported used cars. 
                - Manufacturer: The maker or manufacturer of the car. 
                - Model: The model or type of the car. 
                - Prod. year: The production year of the car. 
                - Category: The category or type of the car (e.g., sedan, SUV, hatchback, etc.).
                - Leather interior: Indicates whether the car has a leather interior or not. 
                - Fuel type: The type of fuel used by the car (e.g., petrol, diesel, electric, etc.). 
                - Engine volume: The engine volume of the car in liters. 
                - Mileage: The number of miles traveled by the car.
                - Cylinders: The number of cylinders in the car's engine.
                - Gear box type: The type of transmission of the car. 
                - Drive wheels: The type of drive wheels of the car.
                - Wheel: The type of wheels of the car.
                - Color: The color of the car.
                - Airbags: The number of airbags in the car.
                 """
                 
prosedur_ml = """
                1. Check the attribute or feature information to understand the context of the data.
                2. Input the data and check the input data results to ensure there are no errors in your data.
                3. Press the 'predict' button to see the price of your favorite car.
              """

# kolom yang digunakan untuk melakukan transformasi leave one out encoder
data_loo = ['Price', 'Levy', 'Manufacturer', 'Model', 'Production year',
       'Category', 'Leather interior', 'Fuel type', 'Engine volume', 'Mileage',
       'Cylinders', 'Gear box type', 'Drive wheels', 'Wheel', 'Color',
       'Airbags']

# kolom yang digunkana saat melakukan fitting scaler 
train_column = ['Levy', 'Manufacturer', 'Model', 'Prod. year', 'Category',
       'Leather interior', 'Fuel type', 'Engine volume', 'Mileage',
       'Cylinders', 'Gear box type', 'Drive wheels', 'Wheel', 'Airbags',
       'Color_Black', 'Color_Blue', 'Color_Brown', 'Color_Carnelian red',
       'Color_Golden', 'Color_Green', 'Color_Grey', 'Color_Orange',
       'Color_Pink', 'Color_Purple', 'Color_Red', 'Color_Silver',
       'Color_Sky blue', 'Color_White', 'Color_Yellow']

# data unik dari setiap kolom dalam dataset
with open('unique_values.pkl', 'rb') as f:
    unique_values = pickle.load(f)

# list model untuk setiap manufacturer
with open('manufacturer_models.pkl', 'rb') as f:
    manufacturer_models = pickle.load(f)
    
# label encoder 
with open('encoder/le_encoder.pkl', 'rb') as f:
    le_encoder = pickle.load(f)
    
# leave one out encoder
with open('encoder/loo_encoder.pkl', 'rb') as f:
    loo_encoder = pickle.load(f)




