import streamlit as st
import streamlit.components.v1 as stc
import joblib, os
import numpy as np
from data import *
import pandas as pd


# home
def home_content():
    st.markdown("""
        # Welcome To Our App
        This app will be used by the Sales team to predict customer segmentation classification for better promotion
        """)
    stc.html('<div style="border-top: 2px solid black; margin: 5px 0;"></div>', height=10)
    st.markdown(desc_temp)


# machine learning 
def ml_content():
    
    st.markdown("""## Machine Learning Section""")
    with st.expander("Steps to Obtain Your Customer Segmentation"):
        st.markdown(prosedur_ml)
    with st.expander("Attribute Information"):
        st.markdown(attribute_info)
    st.markdown("""
                ### Which Customer Segmentation Do You Belong To?
                Input your Data!
                """)
    # input data       
    with st.expander("Your Selected Options"): 
        gender = st.radio('Gender', ['Male', 'Female']) 
        ever_married = st.radio('Married?', ['Yes', 'No'])
        age = st.number_input("Age",10, 70)
        graduated = st.radio("Graduated", ['Yes', 'No'])
        profession = st.selectbox("Profession", ['Healthcare', 'Engineer', 'Lawyer', 'Artist', 'Doctor','Homemaker', 'Entertainment', 'Marketing', 'Executive'])
        work_experience = st.number_input("work_experience", 0, 30)
        spending_score = st.selectbox("spending_score", ["Low", "Average", "High"])
        family_size = st.number_input("Family_Size", 0, 12)
    
    with st.expander("Your Selected Options"):
        result = {
            'Gender': gender,
            'Ever_Married': ever_married,
            'Age': age,
            'Graduated': graduated,
            'Profession': profession,
            'Work_Experience': work_experience,
            'Spending_Score': spending_score,
            'Family_Size': family_size,
        }
    st.markdown("""You sure with your information below?""")
    st.write(result)
    
    if st.button('Predict'):
        predict(result)

def predict(result):
        
    def load_pkl(model_file):
        loaded_pkl = joblib.load(open(os.path.join(model_file), 'rb'))
        return loaded_pkl
    
    def apply_log(column):
        return np.log(column+1)
    
    df = pd.DataFrame(result, index=[0])
    df['Age'] = apply_log(df['Age'])
    df['Work_Experience'] = apply_log(df['Work_Experience'])
    df['Family_Size'] = apply_log(df['Family_Size'])
    

    for keys in result.keys():
        value = result[keys]
        if keys == 'Gender':
            df[keys] = gen[value]
        elif keys == 'Ever_Married':
            df[keys] = evmar[value]
        elif keys == 'Graduated':
            df[keys] = grad[value]
        elif keys == 'Spending_Score':
            df[keys] = spensco[value]
    
    df = pd.get_dummies(df)

    for kolom in train_column:
        if kolom not in df.columns:
            df[kolom] = 0

    scaler = load_pkl('scaler.pkl')
    
    df = df[train_column]
    # df = df.drop(columns=['Segmentation'])
    df = scaler.transform(df.loc[0].values.reshape(1,-1))
 
    # prediction section
    st.subheader('Prediction Result')
    # Menambahkan kolom-kolom yang hilang pada data baru

    # st.write(single_array)

    model = load_pkl("model_xgb.pkl")

    pred_proba = model.predict_proba(df)
    # Mendapatkan daftar label kelas dari model
    
    pred_probability_score = {'Group A':round(pred_proba[0][0]*100,4),
                            'Group B':round(pred_proba[0][1]*100,4),
                            'Group C':round(pred_proba[0][2]*100,4),
                            'Group D':round(pred_proba[0][3]*100,4)}
    
    # Mendapatkan kelompok dengan probabilitas tertinggi
    predicted_group = max(pred_probability_score, key=pred_probability_score.get)

    # Menampilkan hasil prediksi
    st.success(f"Congratulations, you are in {predicted_group}")
    st.write("Probability for each class", pred_probability_score)
    
    # Explaination about the segment
    st.write(f"Profile {predicted_group}")
    st.write(profiling[predicted_group[-1]])