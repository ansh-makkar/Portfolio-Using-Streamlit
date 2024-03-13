import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu

def experience_function():
    st.write("#")
    col1,col2,col3=st.columns(3)
    with col1:
        st.subheader("Data Analyst- Quant Jugglers")
        # st.subheader("Quant Jugglers")
    with col3:
        st.subheader("May,2023-Present")
    st.write("""
    
    -Backtest Indices(Banknifty, Nifty, Finnifty etc.) from Last 5-7 years.
    -Create Strategy For Algo-Tradign Using Python.
    -Create Dashboard using Libraries like Streamlit, Dash, flask etc. To Display Current P&L.
    -Clean Backadjusted Datas and Extract Only Useful.

    
    
    """)