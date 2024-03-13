import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu

def experience_function():

    st.write("#")
    st.write("---")
    col1,col2,col3=st.columns(3)
    with col1:
        st.subheader("Data Analyst- Quant Jugglers")
        # st.subheader("Quant Jugglers")
    with col3:
        st.subheader("May,2023-Present")
    st.write("#")
    st.write("""    
        - Clean Backadjusted Datas and Extract Only Useful Insights
        - Backtest Indices(Banknifty, Nifty, Finnifty etc.) from Last 5-7 years.
        - Create Strategy For Algo-Tradign Using Python.
        - Create Dashboard using Libraries like Streamlit, Dash, flask etc. To Display Current P&L.        
        - Run Algo-Codes on AWS Platform using Services Like EC2.
    """)

    st.write("#")
    st.write("---")
    col1,col2,col3=st.columns(3)
    with col1:
        st.subheader("Automation Engineer- Sysmat Reasearch Solutions LLP")
    with col3:
        st.subheader("Nov,2022-April,2023")
    st.write("#")
    st.write("""    
        - Automated Websites/Windows Applications/Android Applications by Using Libraries like ADB,Selenium etc. 
        - Developed in House Project To Automate Download of Android Applications From Play Store Multiple Times.
        - Maintained Consistency Data & Analyzed it to show in form of Dashboards.
    """)

    st.write("#")
    st.write("---")
    col1,col2,col3=st.columns(3)
    with col1:
        st.subheader("Data Science Intern- The Trinity Company")
    with col3:
        st.subheader("Sept,2022-Oct,2022")
    st.write("#")
    st.write("""    
        - Used ML Models Like Random Forest, Decesion Tree, Logistic Regression etc. To Develop ML Projects 
        - Developed Various in house small case projects like Churn prediction, Stock price prediction, Weather prediction etc.
        - Maintained Consistency of  Data & Analyzed it to show in form of Dashboards.
    """)