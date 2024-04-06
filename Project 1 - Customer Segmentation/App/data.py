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
                1. Review the attribute information to grasp the data context thoroughly.
                2. Enter your data and verify the input results for accuracy before proceeding to predict your customer segmentation.
                3. Click on the 'predict' button to view the outcomes of your customer segmentation analysis.
              """

# key and value for label encoder
gen = {'Male':1, 'Female':0}
evmar = {'Yes':1, 'No':0}
grad = {'Yes':1, 'No':0}
spensco = {'Average':0,'High':1,'Low':2}


train_column = ['Gender', 'Ever_Married', 'Age', 'Graduated', 'Work_Experience',
       'Spending_Score', 'Family_Size', 'Profession_Doctor',
       'Profession_Engineer', 'Profession_Entertainment',
       'Profession_Executive', 'Profession_Healthcare', 'Profession_Homemaker',
       'Profession_Lawyer', 'Profession_Marketing']


profiling = {
    "A":
""" 
    1. The majority of individuals in Segment A work in artistic professions
    2. Individuals in Segment A tend to have a low spending score
    3. Most individuals in Segment A are married or in committed relationships
    4. The majority of individuals in Segment A have completed their education and hold at least a bachelor's degree or higher
    5. The age range of individuals in Segment A typically falls between 35 to 42 years old.
""",

    "B": 
"""
    1. The majority of individuals in Segment B work in artistic professions
    2. Almost 49.6% population in Segment B have average and high spending score
    3. Most individuals in Segment B are married or in committed relationships
    4. The majority of individuals in Segment B have completed their education and hold at least a bachelor's degree or higher
    5. The age range of individuals in Segment B typically falls between 45 to 55 years old.
""",

    "C":
"""
    1. The majority of individuals in Segment C work in artistic professions
    2. Almost 64.8% population in Segment C have average and high spending score
    3. Most individuals in Segment C are married or in committed relationships
    4. The majority of individuals in Segment C have completed their education and hold at least a bachelor's degree or higher
    5. The age range of individuals in Segment C typically falls between 45 to 55 years old.
""",

    "D":
"""
    1. The majority of individuals in Segment D work in healtcare professions
    2.  Individuals in Segment D tend to have a low spending score
    3. Most individuals in Segment D are not married
    4. The majority of individuals in Segment D have not completed their education
    5. The age range of individuals in Segment D typically falls between 20 to 30 years old.
"""
}

