import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
EMAIL="anshmakkar64@gmail.com"
Socail_Media_Links={"Linkedin":"https://www.linkedin.com/in/ansh-makkar/",
                    "GitHub":"https://github.com/ansh-makkar",
                    "Kaggle":"https://www.kaggle.com/anshmakkar"
                    }

def home_page_function():
    col1,col2=st.columns(2)
    with col1:
        st.image("profile-pic.png",width=280)
    with col2:
        st.title("Ansh Makkar")
        st.write("Data Analyst at Quant Jugglers")
        st.write("+91-82953514150")
        st.write("",EMAIL)
    st.write("#")
    cols=st.columns(len(Socail_Media_Links))
    for index,(platform,links) in enumerate(Socail_Media_Links.items()):
        cols[index].write(f"[{platform}]({links})")

    st.write("#")
    st.write("---")
    st.subheader("**Hard Skills**")
    st.write("""
    - 👩‍💻 Programming: Python (Scikit-learn, Pandas), Data Analytics,Automation(ABD, Selenium)
    - 📊 Data Visulization: Streamlit, Flask, dash, PowerBi, MS Excel, Plotly
    - 📚 Modeling: Logistic regression, linear regression, decition trees, Random Forest
    - 🗄️ Databases:  MySQL
    
    """)

    st.write("#")
    