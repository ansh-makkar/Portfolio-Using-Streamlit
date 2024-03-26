import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu



def project_function():


    st.write("#")
    st.write("---")
    col1,col2=st.columns(2)
    with col1:
        st.subheader(" 🛠️NLP-Toolkit - Deep Learning ")
        # st.subheader("Quant Jugglers")

    with col2:
        link = '[Link](https://github.com/VIT-Bhopal-University-Minor-Project/nlp-toolkit)'
        st.markdown(link, unsafe_allow_html=True)
    
    st.write("#")
    st.write("""    
        - NLP ToolKit is an Web-Application Used to Get Sentimental Analysis or Summarization.
        - NLP help Us to Extract The Main Agenda Behind a Review/ a block Of Text / paragraph etc.
        - NLP Uses BERT( Bi-Directional Encoding Transformer) Model From 
        - The Main Tech Stack Behind This WEB-APP are Deep Learning, Machine Learning, React JS, HTML, CSS etc.
        
    """)


    st.write("#")
    st.write("---")
    col1,col2=st.columns(2)
    with col1:
        st.subheader(" 🌿 Go Harvest- Machine Learning")
        # st.subheader("Quant Jugglers")

    with col2:
        link = '[Link](https://github.com/VIT-Bhopal-University-Project-Sem-3/Minor_project/tree/ML_code)'
        st.markdown(link, unsafe_allow_html=True)
    
    st.write("#")
    st.write("""    
        - 
        - 
        - 
        - 
    """)




    st.write("#")
    st.write("---")
    col1,col2=st.columns(2)
    with col1:
        st.subheader(" 🚗 Car Price Prediction - Machine Learning")
        # st.subheader("Quant Jugglers")

    with col2:
        link = '[Link](https://github.com/ansh-makkar/Car-Price-Prediction-Using-Random-Forest-Regression)'
        st.markdown(link, unsafe_allow_html=True)
    
    st.write("#")
    st.write("""    
        - It is a Complete Web-app that is Deployed On Heroku Cloud Platform.
        - It is Guided Project Trained using Kaggle Dataset.
        - It Helped me Understand Concepts Like Data Cleaning, Data Transformation, Model Building , Model Deployment etc.
        - It help In predicting the Cost of Car by taking on Factors like No. of Owner, Total Kilometer , Petrol or Disel etc.
    """)

    
