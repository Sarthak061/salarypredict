import streamlit as st
import pickle
import numpy as np
import pandas as pd

@st.cache
def get_data():
path = r'input.csv'
return pd.read_csv(path)
df = get_data()

def show_predict():
    st.title("Freshers Salary Prediction")

    st.write("""### We need some information to predict the salary ###""")

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

    naac = df['naac1'].drop_duplicates()
    naac1 = st.selectbox("NAAC Grade", naac)
    course = df["course1"].loc[df["naac"] = naac1]
    course1 = st.selectbox("Course", course)
    upskill = df["upskill1"].loc[df["naac"] = naac1 ]
    upskill1 = st.selection("Upskill Course", upskill)
    pgcourse = df["pgcourse1"].loc[df["naac"] = naac1]
    pgcourse1 = st.selection("PG Course", pgcourse)
    country = df["country1"].loc[df["naac"] = naac1]
    country1 = st.selection("Country for PG", country)
    ranking = df["ranking1"].loc[df["naac"] = naac1]
    ranking1 = st.slider("Ranking of College for PG", 0, 200, 1)

    ok = st.button("Predict Salary")
    if ok:
        X = np.array([[naac1,course1,upskill1,pgcourse1,country1,ranking1]])
        X[:, 0] = naac1.transform(X[:,0]) 
        X[:, 1] = course1.transform(X[:,1])
        X[:, 0] = upskill1.transform(X[:,0]) 
        X[:, 0] = pgcourse1.transform(X[:,0]) 
        X[:, 0] = country1.transform(X[:,0])
        X = X.astype(float)

        #salary = regressor.predict(X)
        #st.subheader(f"The estimated salary is {salary[0]:.2f}/-")
