import streamlit as st
import pickle
import numpy as np

#load model
model=pickle.load(open('penyakit_jantung.sav','rb'))
#header
st.title('Prediksi Penyakit 🫀')
col1,col2,col3,col4=st.columns(4)
with col1:
    age=st.number_input('Usia: ',min_value=0, step=1, format="%d")
with col2:
    sex=st.number_input('Jenis Kelamin: ',min_value=0, step=1, format="%d")
with col3:
    cp=st.number_input('Jenis Nyeri Dada ', min_value=0, step=1, format="%d")
with col4:
    threstbps=st.number_input('Tekanan Darah: ',min_value=0, step=1, format="%d")
with col1:
    chol=st.number_input('Cholesterol: ',min_value=0, step=1, format="%d")
with col2:
    fbs=st.number_input('Gula Darah: ',min_value=0, step=1, format="%d")
with col3:
    restech=st.number_input('Elektrokadiografi',min_value=0, step=1, format="%d")
with col4:
    thalach=st.number_input('Detang Jantung Maksimum',min_value=0, step=1, format="%d")
with col1:
    exang=st.number_input('Induksi Angina',min_value=0, step=1, format="%d")
with col2:
    oldpeak=st.number_input('ST Depression')
with col3:
    slope=st.number_input('Slope',min_value=0, step=1, format="%d")
with col4:
    ca=st.number_input('Ca',min_value=0, step=1, format="%d")
with col1:
    thal=st.number_input('Thal',min_value=0, step=1, format="%d")
#code for prediction
heart_diagnosis=''
#membuat tombol prediksi
if st.button('Prediksi Penyakit Jantung'):
    input_data = np.array([age, sex, cp, threstbps, chol, fbs, restech, thalach, exang, oldpeak, slope, ca, thal]).reshape(1, -1)
    heart_predik = model.predict(input_data)
    if(heart_predik[0]==1):
        heart_diagnosis='Pasien Terkena Penyakit Jantung'
        st.error(heart_diagnosis)
    else:
        heart_diagnosis='Pasien Tidak Terkena Penyakit Jantung'
        st.success(heart_diagnosis)
