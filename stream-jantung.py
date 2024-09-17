import pickle
import numpy as np
import streamlit as st

#load

model = pickle.load(open ('penyakit_jantung.sav', 'rb'))

#judul web

st.title('Prediksi Penyakit Jantung')

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input('Umur')
with col2:
    sex = st.number_input('jenis Kelamin')
with col3:
    cp = st.number_input('Jenis nyeri dada')
with col1:
    trestbps = st.number_input('tekanan darah')
with col2:
    chol = st.number_input('Nilai Kolesterol')
with col3:
    fbs = st.number_input('Gula darah')
with col1:
    restecg = st.number_input('Hasil Elektrokardiografi')
with col2:
    thalach = st.number_input('Detak jantung maksimum')
with col3:
    exang = st.number_input('induksi angina')
with col1:
    oldpeak = st.number_input('ST Depresion')
with col2:
    slope = st.number_input('Slope')
with col3:
    ca = st.number_input('nilai CA')
with col1:
    thal = st.number_input('nilai THal')

heart_diagnosis = ''

if st.button('Hasil Prediksi Penyakit Jantung'):
    heart_prediction = model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal ]])

    if (heart_prediction[0]==1):
        heart_diagnosis = 'Terkena Penyakit Jantung'
    else: 
        heart_diagnosis ='Tidak Terkena Penyakit Jantung'

st.success(heart_diagnosis)