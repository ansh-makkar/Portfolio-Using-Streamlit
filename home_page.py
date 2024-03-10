import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
EMAIL="anshmakkar64@gmail.com"

def home_page_function():
    col1,col2=st.columns(2)
    with col1:
        st.image("profile-pic.png",width=350)
    with col2:
        st.title("Ansh Makkar")
        st.write("Data Analyst at Quant Jugglers")
        st.write("+91-82953514150")
        st.write("",EMAIL)
    st.write("#")
    st.write("#")
