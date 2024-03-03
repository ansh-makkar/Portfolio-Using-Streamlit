import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="Ansh Makkar",  # Set the title of the browser tab
    page_icon="emoji-laughing-fill",  # Set the icon for the browser tab
    layout="wide",  # Set the layout of the app (wide or centered)
    initial_sidebar_state="expanded"  # Set the initial state of the sidebar (expanded or collapsed)
)




selected=option_menu(

    menu_title=None,
    options=["Home","Experience","Projects","Contact Me"],
    icons=["house","clipboard-data-fill","book","envelope"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal"
)
if selected:
    st.write(f"{selected}")

if selected=="Contact Me":
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
        
    st.text_area("You Can Leave Your Messeage Here .....")
    st.write("<div style='text-align: center;'>", unsafe_allow_html=True)
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
        form_submit_button = st.button('Button')
    # form_submit_button=st.button("Sumbit")
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
        st.success(f"Thankyou! {first_name} , I will Contact as Soon as Possible.")