import streamlit as st
from prediction_helper import predict

# Define the page layout
st.title('Health Insurance Prediction App')


categorical_options = {
    'Gender' : ['Male', 'Female'],
    'Region' : ['Northeast', 'Northwest', 'Southeast', 'Southwest'],
    'Marital Status' : ['Unmarried', 'Married'],
    'BMI Category' : ['Overweight', 'Underweight', 'Normal', 'Obesity'],
    'Smoking Status' : ['Regular', 'No Smoking', 'Occasional'],
    'Employment Status' : ['Self-Employed', 'Freelancer', 'Salaried'],
    'Medical History' : ['High blood pressure', 'No Disease', 'Diabetes & High blood pressure',
        'Diabetes & Heart disease', 'Diabetes', 'Diabetes & Thyroid',
        'Heart Disease', 'Thyroid', 'High blood pressure & Heart disease'],
    'Insurance Plan' : ['Silver', 'Bronze', 'Gold']
}

# Create four rows of three columns each
row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)
row4 = st.columns(3)

# Assing inputs to the grid
with row1[0]:
    age = st.number_input("Age", min_value=18, max_value=100, step=1)
with row1[1]:
    number_of_dependants = st.number_input("Number Of Dependants", min_value=0, max_value=20, step=1)
with row1[2]:
    income_lakhs = st.number_input("Income Lakhs", min_value=0, max_value=200, step=1)

with row2[0]:
    genetical_risk = st.number_input("Genetical Risk", min_value=0, max_value=5, step=1)
with row2[1]:
    insurance_plane = st.selectbox("Insurance Plan", categorical_options["Insurance Plan"])
with row2[2]:
    employment_status = st.selectbox("Employment Status", categorical_options["Employment Status"])

with row3[0]:
    gender = st.selectbox("Gender", categorical_options["Gender"])
with row3[1]:
    marital_status = st.selectbox("Marital Status", categorical_options["Marital Status"])
with row3[2]:
    bmi_category = st.selectbox("BMI Category", categorical_options["BMI Category"])

with row4[0]:
    smoking_status = st.selectbox("Smoking Status", categorical_options["Smoking Status"])
with row4[1]:
    region = st.selectbox("Region", categorical_options["Region"])
with row4[2]:
    medical_history = st.selectbox("Medical History", categorical_options["Medical History"])

# Create a dictionary for input values
input_dict = {
    "Age": age,
    "Number of Dependants": number_of_dependants,
    "Income in Lakhs": income_lakhs,
    "Gender": gender,
    "Marital Status": marital_status,
    "BMI Category": bmi_category,
    "Smoking Status": smoking_status,
    "Employment Status": employment_status,
    "Medical History": medical_history,
    "Insurance Plan": insurance_plane,
    "Region": region,
    "Genetical Risk": genetical_risk
}

# button to make prediction
if st.button('Predict'):
    prediction = predict(input_dict)
    st.success(f"Predicted Premium: {prediction}")

