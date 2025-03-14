import streamlit as st
import numpy as np
import pickle

# Load the trained model
with open("diamod.pkl", "rb") as file:
    model = pickle.load(file)

st.title("Diabetes Prediction using Decision Tree Classifier")

# Collect user input
gender = st.selectbox("Gender", ["Male", "Female", "Other"])  
age = st.number_input("Age", min_value=1, max_value=120, value=30)
hypertension=st.selectbox("Hypertenison",["Yes","No"])
heart_disease = st.selectbox("Heart Disease", ["No", "Yes"])
smoking_history = st.selectbox("Smoking History", ["Currently", "No Currently","Former", "Never", "Ever"])
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0)
HbA1c_level = st.number_input("HbA1c Level (%)", min_value=3.0, max_value=15.0, value=5.7)
blood_glucose_level = st.number_input("Blood Glucose Level", min_value=50, max_value=300, value=100)

# Convert categorical values to numerical
gender_dict = {"Male": 0, "Female": 1, "Other": 2}
gender = gender_dict[gender]

heart_disease = 1 if heart_disease == "Yes" else 0
hypertension = 1 if hypertension =="Yes" else 0
smoking_dict = {"Currently": 0, "No Currently": 1, "Never": 2, "Ever": 3}
smoking_history = smoking_dict[smoking_history]

# Convert input to numpy array
user_input = np.array([[gender, age,hypertension, heart_disease, smoking_history, bmi, HbA1c_level, blood_glucose_level]])

# Predict diabetes
if st.button("Predict"):
    prediction = model.predict(user_input)
    if prediction[0] == 1:
        st.error("The model predicts: **Diabetic** 😞")
    else:
        st.success("The model predicts: **Not Diabetic** 😊")
