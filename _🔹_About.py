import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Depression Project",
    page_icon="📉",
    layout="wide",
)

st.sidebar.write("Author: [Mauricio Lobo](https://github.com/mauricio-lobo-ds)")

st.title("🔹 About the Project")

st.write("Welcome to the project's homepage.")
st.write("This project uses the [Depression Professional Dataset](https://www.kaggle.com/datasets/ikynahidwin/depression-professional-dataset/data) for analysis.")
st.write("""
The dataset includes 2054 entries and 11 columns with information about individuals, such as gender, age, work pressure, job satisfaction, sleep duration, dietary habits, and more. 
It also contains mental health-related data, such as whether the person has experienced suicidal thoughts, financial stress levels, family history of mental illness, and if they have depression.
This data can be used to explore correlations and trends in factors that might contribute to mental health outcomes.
""")

