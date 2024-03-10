import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
from contact_page import *
from home_page import *

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
    contact_page()

if selected=="Home":
    home_page_function()