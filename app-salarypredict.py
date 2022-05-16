import streamlit as st
from predict import show_predict


page = st.sidebar.selectbox("Explore Or Predict", ("Predict", "Explore"))
show_predict_page()
