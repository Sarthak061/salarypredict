import streamlit as st
import pickle
import numpy as np


def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

regressor = data["model"]
le_naac = data["le_naac"]
le_course = data["le_course"]
le_upskill = data["le_upskill"]
le_pgcourse = data["le_pgcourse"]
le_country = data["le_country"]

def show_predict():
    st.title("Freshers Salary Prediction")

    st.write("""### We need some information to predict the salary""")

    naac = (
           "A++",
           "A+",
           "A",
           "B++",
           "B+",
           "B",
           "C",
           "D",
           "No Grade"
    )

    course = (
            "BE in CS,Electronics,IT,Telecom",
            "BE in data science",
            "BE in others",
            "BCOM",
            "BA",
            "BSc",
            "PG in HR",
            "PG in Marketing",
            "PG in finance",
            "PG in Data science",
            "CA"
    )
    upskill = (
           "IT",
           "Data Science",
           "Finance",
           "Management",
           "Art"
    )
    
    pgcourse = (
        "Engineering",
            "IT",
            "Management",
            "Finance",
            "Economics",
            "Others"
    )
    
    country = ("US",
               "Australia",
               "Germany",
               "UK",
               "India",
               "Canada",
               "Other Asian countries",
               "Other European countries"
    )

    naac = st.selectbox("NAAC Grade", naac)
    course = st.selectbox("Course", course)
    upskill = st.selection("Upskill Course", upskill)
    pgcourse = st.selection("PG Course", pgcourse)
    country = st.selection("Country for PG", country)

    ranking = st.slider("Ranking of College for PG", 0, 200, 1)

    ok = st.button("Predict Salary")
    if ok:
        X = np.array([[naac,ourse,upskill,pgcourse,country,ranking]])
        X[:, 0] = le_naac.transform(X[:,0]) 
        X[:, 1] = le_course.transform(X[:,1])
         X[:, 0] = le_upskill.transform(X[:,0]) 
            X[:, 0] = le_pgcourse.transform(X[:,0]) 
            X[:, 0] = le_country.transform(X[:,0])
             X[:, 0] = le_ranking.transform(X[:,0])
        X = X.astype(float)

        salary = regressor.predict(X)
        st.subheader(f"The estimated salary is {salary[0]:.2f}/-")
