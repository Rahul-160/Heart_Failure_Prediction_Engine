import streamlit as st
import pickle
from PIL import Image

def main():
    st.title("HEART DISEASE PREDICTION")
    image = Image.open("OIP.jpg")
    st.image(image, width = 500)
    age = st.text_input("Age","Type here")
    gender = st.radio("Sex", ['Male', 'Female'])
    if gender == 'Male':
        sex = 1
    else:
        sex = 0
    cp = st.text_input("cp", "Type here")
    trestbps = st.text_input("trestbps", "Type here")
    chol = st.text_input("chol", "Type here")
    fbs = st.text_input("fbs", "Type here")
    restecg = st.text_input("restecg", "Type here")
    thalach = st.text_input("thalach", "Type here")
    exang = st.text_input("exang", "Type here")
    oldpeak = st.text_input("oldpeak", "Type here")
    slope = st.text_input("slope", "Type here")
    ca = st.text_input("ca", "Type here")
    thal = st.text_input("thal", "Type here")
    features = [age, sex, cp, trestbps, chol, fbs, restecg, thalach,
                exang, oldpeak, slope, ca, thal]
    model = pickle.load(open('model.sav', 'rb'))
    scaler = pickle.load(open('scaler1.sav', 'rb'))
    pred = st.button('Predict')
    if pred:
        prediction = model.predict(scaler.transform([features]))
        if prediction == 0:
            st.write("Not Suffering Heart Disease")
        else:
            st.write("Suffering Heart Disease")
main()
