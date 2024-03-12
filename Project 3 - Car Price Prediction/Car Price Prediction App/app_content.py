import streamlit as st
import streamlit.components.v1 as stc
import joblib, os
import numpy as np
from data import *
import pandas as pd


# home
def home_content():
    st.markdown("""
        # Welcome To My Car Prediction App
        """)
    stc.html('<div style="border-top: 2px solid black; margin: 5px 0;"></div>', height=10)
    st.markdown(desc_temp)

# machine learning 
def ml_content():
    st.markdown("""# Machine Learning Section""")
    stc.html('<div style="border-top: 2px solid black; margin: 5px 0;"></div>', height=10)
    with st.expander("Prosedur"):
        st.markdown(prosedur_ml)
    with st.expander("Attribute Info"):
        st.markdown(attribute_info)
    st.markdown("""
                ### Choose Your Favorite Car Style!!
                Input your data!
                """)
    # input data       
    with st.expander("Your Selected Options"): 
        levy = st.number_input("levy (max 10000)", 0, 10000) 
        manufacturer = st.selectbox('Manufacturer', unique_values['Manufacturer'])
        model = st.selectbox('Model', manufacturer_models[manufacturer])
        production_year = st.number_input("Production Year (1970 - 2024)",1970, 2024) 
        category = st.selectbox("Category", unique_values['Category'])
        leather_interior = st.selectbox("Leather Interior", unique_values['Leather interior'])
        fuel_type = st.selectbox("Fuel Type", unique_values['Fuel type'])
        engine_volume = st.selectbox("Engine Volume", unique_values['Engine volume'])
        cylinders = st.number_input("Cylinder (1 - 20)", 1, 20)
        gear_box_types = st.selectbox("Gear Box Type", unique_values['Gear box type'])
        mileage = st.number_input("mileage (max 1000000)", 1, 1000000)
        drive_wheels = st.selectbox("Drive wheels", unique_values['Drive wheels'])
        wheel = st.selectbox("Wheel", unique_values['Wheel'])
        color = st.selectbox("Car Color", unique_values['Color'])
        airbags = st.number_input("airbags (0 - 20)", 0, 20)
    
    with st.expander("Your Selected Options"):
        result = {
            'Levy': levy,
            'Manufacturer': manufacturer,
            'Model': model,
            'Production year': production_year,
            'Category': category,
            'Leather interior': leather_interior,
            'Fuel type': fuel_type,
            'Engine volume': engine_volume,
            'Cylinders': cylinders,
            'Mileage': mileage,
            'Gear box type': gear_box_types,
            'Drive wheels': drive_wheels,
            'Wheel': wheel,
            'Color': color,
            'Airbags': airbags,
        }
    st.markdown("""You sure with your information below?""")
    st.write(result)
    
    if st.button('Predict'):
        predict(result)

def predict(result):
        
    def load_pkl(model_file):
        loaded_pkl = joblib.load(open(os.path.join(model_file), 'rb'))
        return loaded_pkl
    
    df = pd.DataFrame(result, index=[0])
    
    # data di bawah merupakan data bantuan agar syarat transfor untuk loo_encoder terpenuhi karena perbedaan kolom yang
    # di-fit pada notebook dengan result atau df
    df['Price'] = 123
    df = df[data_loo]
    
    # melakukan label encoder
    for keys in le_encoder.keys():
        df[keys] = le_encoder[keys].transform(df[keys])
    
    # melakukan leave one out encoder
    df_encoded = loo_encoder.transform(df)
    
    # menimpa data nilai pada kolom tertentu pada df dengan data nilai df_encoded
    columns_to_encode = ('Manufacturer', 'Model', 'Category')
    for column in columns_to_encode:
        df[column] = df_encoded[column]
    
    # melakukan one hot encoder
    df = pd.get_dummies(df)
    for kolom in train_column:
        if kolom not in df.columns:
            df[kolom] = 0

    # melakukan scaling
    scaler = load_pkl('scaler/standard_scaler.pkl')
    df = df.drop(columns='Price')
    df = df[train_column]
    df = scaler.transform(df.loc[0].values.reshape(1,-1))
    
    # prediction section
    st.subheader('Prediction Result')
    # Menambahkan kolom-kolom yang hilang pada data baru

    # st.write(single_array)

    model = load_pkl("model/model_rf.pkl")

    pred = model.predict(df)

    # Menampilkan hasil prediksi
    st.success(f"Price of the car is  {pred[0]} $")