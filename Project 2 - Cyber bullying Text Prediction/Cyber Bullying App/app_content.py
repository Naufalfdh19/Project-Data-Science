import streamlit as st
import streamlit.components.v1 as stc
import joblib, os
from data import *
import numpy as np
import pandas as pd
import re

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')


# home content
def home_content():
    st.markdown("""
        # Welcome To Cyberbullying Text Prediction App
        The machine learning algorithms embedded in this application can be utilized by owners of interactive applications, such as social media platforms, games, and others, to create a positive environment and experience for app users and prevent verbal bullying.
        """)
    stc.html('<div style="border-top: 2px solid black; margin: 5px 0;"></div>', height=10)
    st.markdown(desc_temp)


if "chats" not in st.session_state:
    st.session_state.chats = {}
if "chat_received" not in st.session_state:
    st.session_state.chat_received = 0
if "input_text" not in st.session_state:
    st.session_state.input_text = 'Type here!'

# machine learning content
def ml_content():
    # Tambahkan judul dengan st.title
    st.title("Cyber bullying Text Prediction")
    stc.html('<div style="border-top: 2px solid black;"></div>', height=10)
    
    with st.expander("Prosedure"):
        st.markdown(prosedur_ml)
    
    # Membuat dua kolom dengan lebar yang sama
    col1, col2 = st.columns([2, 4])
    
    # Menambahkan konten ke kolom pertama
    # # with col1:
    #     st.image('img/pic.jpeg')
    
    # create image
    with col1:
        st.image('img/pic.jpeg')
    
    # Mendapatkan nilai chat_received dari state
    # chat_received = st.session_state.chat_received
    
    # Mendapatkan nilai chats dari state
    # chats = st.session_state.chats
    
    
    
    # # Menambahkan konten ke kolom kedua
    # with col2:
    #     if chat_received == 0:
    #         st.text("Your chat!")
    #     else:
    #         for chat_key, chat_val in chats.items():
    #             st.write(chat_key, chat_val)
    with col2:
        input_text = st.text_input('Enter your text', 'Text Area')
        if st.button('Send'):
            predict(input_text)
        # Update nilai chat_received dan chats di state
        # if input_text not in chats.values():
        #     # Update nilai chat_received dan chats di state hanya jika teks chat belum ada sebelumnya
        #     pred = predict(input_text)
        #     if pred:
        #         chat_received += 1
        #         chats[f'chat {chat_received}'] = input_text

                
        #         st.session_state.chat_received = chat_received
        #         st.session_state.chats = chats
        # if chat_received > 3:
        #     st.session_state.chat_received = 0
        #     st.session_state.chats = {}
    

# data preprocessing, scaling, and modelling       
def predict(text):
    def load_pkl(model_file):
        loaded_pkl = joblib.load(open(os.path.join(model_file), 'rb'))
        return loaded_pkl
    
    def remove_NoV_word(text, word):
        NoV_word = word

        # Menghapus kata-kata tertentu dari teks
        for word in NoV_word:
            text = text.replace(word, ' ')

        return text.strip()

    
    # cleansing
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'@\S+', '', text)
    text = re.sub(r'#\S+', '', text)
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'[^\w\s]|[\d]', '', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = re.sub(r'@\w+|\#\w+', '', text).strip()

    # tokenization
    text = word_tokenize(text)
    
    # remove stopwords
    filter = []
    stop_words = set(stopwords.words('english'))
    for token in text:
        if token not in stop_words:
            filter.append(token)
    
    lem_text = []
    lem = WordNetLemmatizer()
    for word in text:
        lem_text.append(lem.lemmatize(word, 'v'))
        
    clean_text = ' '.join(lem_text).lower()
    clean_text = remove_NoV_word(clean_text, [' i ', ' u ', ' people ', ' im ', ' dont ',  ' like '])
    
    scaler = load_pkl('vectorizer.pkl')
    
    clean_text = [clean_text] 
    clean_text = scaler.transform(clean_text)
    
    model = load_pkl("model_rf.pkl")
    
    result = model.predict(clean_text)
    result_value = result.item() if result.size == 1 else result.tolist()
    type_of_cyberbullying = le[result_value]
    st.write(type_of_cyberbullying)

    if type_of_cyberbullying == 'not_cyberbullying':
        st.success(f"Upload")
        return

   
    st.error(f'Sorry, your message is considered to contain a {type_of_cyberbullying} cyberbullying violation')
    return

    
    