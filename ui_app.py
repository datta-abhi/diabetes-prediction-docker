import streamlit as st
import requests

st.title("🩺 Diabetes Prediction App")
st.write("Enter patient data below:")

# input form
with st.form("diabetes_form"):
    Pregnancies= st.number_input("Pregnancies",0,20,1)
    Glucose= st.number_input("Glucose",0.0, 200.0, 120.0)
    BloodPressure= st.number_input("BloodPressure", 0.0, 150.0, 70.0)
    SkinThickness= st.number_input("SkinThickness",0.0, 100.0, 20.0)
    Insulin= st.number_input("Insulin",0.0, 1000.0, 79.0)
    BMI= st.number_input("BMI",0.0, 100.0, 25.0)
    DiabetesPedigreeFunction= st.number_input("DiabetesPedigreeFunction",0.0, 2.5, 0.5)
    Age= st.number_input("Age",1, 120, 30)
    
    submitted = st.form_submit_button("Predict")
    
if submitted:
   input_data = {
        "Pregnancies": Pregnancies,
        "Glucose": Glucose,
        "BloodPressure": BloodPressure,
        "SkinThickness": SkinThickness,
        "Insulin": Insulin,
        "BMI": BMI,
        "DiabetesPedigreeFunction": DiabetesPedigreeFunction,
        "Age": Age
    }
   
   res = requests.post("http://localhost:8000/predict",json=input_data)
   
   if res.status_code ==200:
       prediction = res.json()['prediction']
       st.success(f"Prediction: {'Diabetic' if prediction==1 else 'Non-Diabetic'}")
   else:
       st.error("API call failed")    
            