import streamlit as st

title = """
            <div style="background-color:#966E30;padding:10px;border-radius:10px">
		    <h1 style="color:white;text-align:center;">Customer Segmentation Prediction App </h1
        """

desc_temp = """
            #### Data Source
            - https://www.kaggle.com/datasets/kaushiksuresh147/customer-segmentation/data
            #### App Content
            - Home: This section provides an overview of the application's purpose and its data sources.
            - Machine Learning: In this section, users can input data and predict visitor customer segmentation based on information about the dataset. 
            """

css = """
    <style>
        .elegant-text {
            font-family: 'Times New Roman', Times, serif;
            font-size: 40px;
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
                 - Gender: Gender of the customer
                 - Ever_Married: Marital status of the customer
                 - Age: Age of the customer
                 - Graduated: Status of customer that graduate from university
                 - Profession: Profession of the customer
                 - Work_Experience: Work experience in years
                 - Spending_Score: Spending score of the customer
                 - Family_Size: Number of family members for the customer (including the customer)
                 """
                 
prosedur_ml = """
                1. Check the attribute or feature information to understand the context of the data.
                2. Input the data and check the input data results to ensure there are no errors in your data.
                3. Press the 'predict' button to see the results of your customer segmentation.
              """

# key and value for label encoder
gen = {'Male':1, 'Female':0}
evmar = {'Yes':0, 'No':1}
grad = {'Yes':0, 'No':1}
spensco = {'Average':0,'High':1,'Low':2}


train_column = ['Gender', 'Ever_Married', 'Age', 'Graduated', 'Work_Experience',
       'Spending_Score', 'Family_Size', 'Segmentation', 'Profession_Artist',
       'Profession_Doctor', 'Profession_Engineer', 'Profession_Entertainment',
       'Profession_Executive', 'Profession_Healthcare', 'Profession_Homemaker',
       'Profession_Lawyer', 'Profession_Marketing']


