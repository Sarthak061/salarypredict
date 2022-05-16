import streamlit as st
from predict import show_predict


page = st.sidebar.selectbox("Predict", ("Predict Fresher's Salary"))
show_predict()
