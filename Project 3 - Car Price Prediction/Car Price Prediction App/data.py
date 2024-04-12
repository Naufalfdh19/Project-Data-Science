import streamlit as st
import pickle

title = """
            <div style="background-color:#093145;padding:10px;border-radius:10px">
		    <h1 style="color:white;text-align:center;">Car Price Prediction App </h1
       """
desc_temp = """
            This app will be used to by someone to make a prediction about a car price and make the best transaction, whether they want to sell or buy a car
            #### Data Source
            - https://www.kaggle.com/datasets/deepcontractor/car-price-prediction-challenge
            #### App Content
            - Home: This section provides an overview of the application's purpose and its data sources.
            - Machine Learning: In this machine learning section, users can input data and predict the price of a model based on various categories, such as brand, production year, or automobile components 
            """

css = """
    <style>
        .elegant-text {
            font-family: 'Times New Roman', Times, serif;
            font-size: 25px;
            color: #0D3D54; 
            text-align: center;
            # background: linear-gradient(to right, #654321, #3e2723); /* Transisi dari coklat muda ke coklat tua */
            # -webkit-background-clip: text;
            # -webkit-text-fill-color: transparent;
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
                2. Verify the input data to ensure that there are no erros in the data before proceeding with data analysis.
                3. Press the 'predict' button to predict the price of your car that you want to sell or buy.
              """

# kolom yang digunakan untuk melakukan transformasi leave one out encoder
data_loo = ['Price', 'Levy', 'Manufacturer', 'Model', 'Production year',
       'Category', 'Leather interior', 'Fuel type', 'Engine volume', 'Mileage',
       'Cylinders', 'Gear box type', 'Drive wheels', 'Wheel', 'Color',
       'Airbags']

# kolom yang digunkana saat melakukan fitting scaler 
train_column = ['Levy', 'Model', 'Prod. year', 'Leather interior', 'Fuel type',
       'Engine volume', 'Mileage', 'Cylinders', 'Gear box type',
       'Drive wheels', 'Wheel', 'Airbags', 'Manufacturer_ALFA ROMEO',
       'Manufacturer_AUDI', 'Manufacturer_BMW', 'Manufacturer_BUICK',
       'Manufacturer_CADILLAC', 'Manufacturer_CHEVROLET',
       'Manufacturer_CHRYSLER', 'Manufacturer_CITROEN', 'Manufacturer_DAEWOO',
       'Manufacturer_DAIHATSU', 'Manufacturer_DODGE', 'Manufacturer_FERRARI',
       'Manufacturer_FIAT', 'Manufacturer_FORD', 'Manufacturer_GAZ',
       'Manufacturer_GMC', 'Manufacturer_GREATWALL', 'Manufacturer_HAVAL',
       'Manufacturer_HONDA', 'Manufacturer_HUMMER', 'Manufacturer_HYUNDAI',
       'Manufacturer_INFINITI', 'Manufacturer_ISUZU', 'Manufacturer_JAGUAR',
       'Manufacturer_JEEP', 'Manufacturer_KIA', 'Manufacturer_LANCIA',
       'Manufacturer_LAND ROVER', 'Manufacturer_LEXUS', 'Manufacturer_LINCOLN',
       'Manufacturer_MASERATI', 'Manufacturer_MAZDA',
       'Manufacturer_MERCEDES-BENZ', 'Manufacturer_MERCURY',
       'Manufacturer_MINI', 'Manufacturer_MITSUBISHI', 'Manufacturer_MOSKVICH',
       'Manufacturer_NISSAN', 'Manufacturer_OPEL', 'Manufacturer_PEUGEOT',
       'Manufacturer_PONTIAC', 'Manufacturer_PORSCHE', 'Manufacturer_RENAULT',
       'Manufacturer_ROLLS-ROYCE', 'Manufacturer_ROVER', 'Manufacturer_SAAB',
       'Manufacturer_SATURN', 'Manufacturer_SCION', 'Manufacturer_SEAT',
       'Manufacturer_SKODA', 'Manufacturer_SSANGYONG', 'Manufacturer_SUBARU',
       'Manufacturer_SUZUKI', 'Manufacturer_TOYOTA', 'Manufacturer_UAZ',
       'Manufacturer_VAZ', 'Manufacturer_VOLKSWAGEN', 'Manufacturer_VOLVO',
       'Manufacturer_ZAZ', 'Manufacturer_სხვა', 'Category_Coupe',
       'Category_Goods wagon', 'Category_Hatchback', 'Category_Jeep',
       'Category_Limousine', 'Category_Microbus', 'Category_Minivan',
       'Category_Pickup', 'Category_Sedan', 'Category_Universal',
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
with open('le_encoder.pkl', 'rb') as f:
    le_encoder = pickle.load(f)
    
# # leave one out encoder
# with open('encoder/loo_encoder.pkl', 'rb') as f:
#     loo_encoder = pickle.load(f)




