import streamlit as st

title = """
            <div style="background-color:#966E30;padding:10px;border-radius:10px">
		    <h1 style="color:white;text-align:center;">Customer Segmentation Prediction App </h1
        """

desc_temp = """
            #### Data Source
            - https://www.kaggle.com/datasets/andrewmvd/cyberbullying-classification
            #### App Content
            - Home: This section provides an overview of the application's purpose and its data sources.
            - Machine Learning: In this section, users can input some text in the input column and predict whether the text falls into the category of bullying or not. 
            """

css = """
    <style>
        .elegant-text {
            font-family: 'Times New Roman', Times, serif;
            font-size: 25px;
            color: #567582; /* Coklat muda */
            text-align: center;
            # background: linear-gradient(to right, #654321, #3e2723); /* Transisi dari coklat muda ke coklat tua */
            # -webkit-background-clip: text;
            # -webkit-text-fill-color: transparent;
        }
    </style>
"""

# data prosedur in machine learning section
prosedur_ml = """
                1. Insert your text into the text area.
                2. Click 'send' button and see the result
              """
              
# label encoder untuk tipe cyberbullying
le = {
        3: 'not_cyberbullying',
        2: 'gender',
        4: 'religion',
        0: 'age', 
        1: 'ethnicity'
    }

