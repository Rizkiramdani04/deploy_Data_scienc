import streamlit as st
import numpy as np
import joblib

# Judul Aplikasi
st.set_page_config(page_title="Deteksi Email Phishing", page_icon="📧")
st.header('📧 Deteksi Email Phishing dengan Machine Learning')

st.markdown(
    """
    Aplikasi ini menggunakan model **Random Forest** untuk memprediksi apakah sebuah email termasuk *phishing* atau aman.
    Masukkan fitur-fitur email yang ingin Anda evaluasi di bawah ini:
    """
)

# Load Model
model = joblib.load('random_forest_model.pkl')

# Input Form
st.subheader("🔢 Masukkan Fitur Email:")
col1, col2,col3,col4 = st.columns(4)

with col1:
    num_words = st.number_input('Jumlah Kata:', min_value=0, step=1)
with col2:
    num_unique_words = st.number_input('Jumlah Kata Unik:', min_value=0, step=1)
with col3:
    num_stopwords = st.number_input('Jumlah Stopwords:', min_value=0, step=1)
with col4:
    num_links = st.number_input('Jumlah Tautan:', min_value=0, step=1)
with col1:
    num_unique_domains = st.number_input('Jumlah Domain Unik:', min_value=0, step=1)
with col2:
    num_email_addresses = st.number_input('Jumlah Alamat Email:', min_value=0, step=1)
with col3:
    num_spelling_errors = st.number_input('Jumlah Kesalahan Ejaan:', min_value=0, step=1)
with col4:
    num_urgent_keywords = st.number_input('Jumlah Kata Mendesak:', min_value=0, step=1)

# Prediksi
if st.button('🔍 Prediksi Email Phishing'):
    input_data = np.array([
        num_words, num_unique_words, num_stopwords, num_links,
        num_unique_domains, num_email_addresses, num_spelling_errors, num_urgent_keywords
    ]).reshape(1, -1)

    prediction = model.predict(input_data)

    st.subheader("📊 Hasil Prediksi:")
    if prediction[0] == 1:
        st.error("⚠️ Email Terdeteksi Sebagai *Phishing*! Harap berhati-hati.")
    else:
        st.success("✅ Email Ini Aman dari *Phishing*.")

    # Penjelasan Hasil
    with st.expander("ℹ️ Penjelasan Hasil"):
        st.markdown("""
        - **Phishing (1):** Email ini memiliki karakteristik yang mirip dengan email phishing.
        - **Aman (0):** Email tidak mengandung ciri khas email phishing berdasarkan fitur yang dimasukkan.
        """)

# Footer
st.markdown("---")
st.caption("📌 Dibuat oleh Rizki Ramdani | Model: Random Forest")
