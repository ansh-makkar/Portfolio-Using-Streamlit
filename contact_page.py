import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
from telegram_bot import *

def contact_page():
    st.markdown("<h1 style='text-align: center;'>CONTACT ME</h1>", unsafe_allow_html=True)
    st.write(" ")
    st.write(" ")
    col1, col2 = st.columns(2)
    with col1:
        first_name=st.text_input("First Name :")        
        mobile_number=st.text_input("Contact Number :")
        
    with col2:
        last_name=st.text_input("Last Name :")
        email_address=st.text_input("Email Address :")        
    message=st.text_area("You Can Leave Your Messeage Here .....")

    ## Putting Submit button in center.
    col11, col12, col13 , col14, col15 = st.columns(5)
    with col11:
        pass
    with col12:
        pass
    with col14:
        pass
    with col15:
        pass
    with col13 :
        form_submit_button = st.button('Submit')
    errors=False
    
    
    if first_name and len(first_name)<3 or form_submit_button and len(first_name)<3:
        st.error("Please Enter A Valid Name")  
        errors=True              
    if mobile_number and len(mobile_number)!=10 or form_submit_button and len(mobile_number)!=10:
        st.error("please Enter Valid Mobile Number.")
        errors=True
    if email_address and ("@" not in email_address or "com" not in email_address) or form_submit_button and ("@" not in email_address or "com" not in email_address):
            st.error("Please Enter a Valid Email Id")
            errors=True    
    if form_submit_button and not errors:        
        
        email_notification(email_address,f"Thankyou For Conatacting Me {first_name}",f"Heyy! {first_name} {last_name}, Thankyou For Reaching Out to Me ! I will Get Back To you As Soon As I Can.")
        telegram_bot(f"NAME :- {first_name} {last_name}")
        telegram_bot(f"{message}")
        st.success(f"Thankyou! {first_name} ,Your Response Has Been Recorded, Please Check Your Mail Id.")