import streamlit as st
from pages import home, predict, dashboard

st.set_page_config(
    page_title="Student Predictor",
    page_icon="🎓",
    layout="wide"
)

page = st.sidebar.selectbox(
    "Navigation",
    ["Home", "Predict", "Dashboard"]
)

if page == "Home":
    home.show()

elif page == "Predict":
    predict.show()

elif page == "Dashboard":
    dashboard.show()