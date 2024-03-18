import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu

projects_link={"Car_price_predication":"https://github.com/ansh-makkar/Car-Price-Prediction-Using-Random-Forest-Regression"}


def project_function():
    st.write("#")
    st.write("---")
    col1,col2=st.columns(2)
    with col1:
        st.subheader(" 🚗 Car Price Prediction - Machine Learning")
        # st.subheader("Quant Jugglers")

    with col2:
        st.write()
    
    st.write("#")
    st.write("""    
        - It is a Complete Web-app that is Deployed On Heroku Cloud Platform.
        - It is Guided Project Trained using Kaggle Dataset.
        - It Helped me Understand Concepts Like Data Cleaning, Data Transformation, Model Building , Model Deployment etc.
        - It help In predicting the Cost of Car by taking on Factors like No. of Owner, Total Kilometer , Petrol or Disel etc.        
        
    """)
