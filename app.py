import streamlit as st
import pickle
import pandas as pd
import gdown
import os
from dict import display_names, labelenc_map, ohe_map, bin_map
from column import NUMERIK, KATEGORIK, MULTIKELAS_OHE, BINER_LAIN, LABELENC_BINER_3
MODEL_PATH = "model/best_stacking_res.pkl"
os.makedirs("model", exist_ok=True)

if not os.path.exists(MODEL_PATH):
    url = "https://drive.google.com/file/d/1UKAvBLzYRC7y6BpWQiIcbPJPsRIw-nbI/view?usp=drive_link" 
    gdown.download(url, MODEL_PATH, quiet=False)

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)
# model = pickle.load(open("https://drive.google.com/file/d/1UKAvBLzYRC7y6BpWQiIcbPJPsRIw-nbI/view?usp=sharing", "rb"))
preprocessor = pickle.load(open("model/preprocessor.pkl", "rb"))

st.set_page_config(
    page_title="Prediksi Risiko Serangan Jantung",
    layout="wide"
)

left, main, right = st.columns([1,3,1])   
with main:
    st.markdown("<h1 style='text-align:center; color:#c1121f; margin-top:-60px;'>Prediksi Risiko Serangan Jantung</h1>", unsafe_allow_html=True)
    st.markdown("<p style='margin-top:-20px;'>Isi data pasien pada form berikut untuk melihat tingkat risiko serangan jantung.</p>", unsafe_allow_html=True)

    input_data = {}
    layoutn = [3, 3, 2, 2]
    start_idx = 0
    for n_cols in layoutn:
        cols = st.columns(n_cols)
        for i in range(n_cols):
            if start_idx >= len(NUMERIK):
                break
            col_name = NUMERIK[start_idx]
            with cols[i]:
                val = st.number_input(display_names[col_name], value=0.00, step=1.0)
                input_data[col_name] = float(val)
            start_idx += 1

    layoutk = [3, 3, 3, 3, 3, 2]
    start_idx = 0
    for n_cols in layoutk:
        cols = st.columns(n_cols)
        for i in range(n_cols):
            if start_idx >= len(KATEGORIK):
                break
            col_name = KATEGORIK[start_idx]
            with cols[i]:
                if col_name in LABELENC_BINER_3:
                    pilihan = list(labelenc_map[col_name].keys())
                    input_data[col_name] = labelenc_map[col_name][st.selectbox(display_names[col_name], pilihan)]
                elif col_name in MULTIKELAS_OHE:
                    pilihan = list(ohe_map[col_name].keys())
                    pilih = st.selectbox(display_names[col_name], pilihan)
                    input_data[col_name] = ohe_map[col_name][pilih]
                elif col_name in BINER_LAIN:
                    pilih = st.selectbox(display_names[col_name], ["Iya", "Tidak"])
                    input_data[col_name] = bin_map[pilih]
            start_idx += 1
            
    if st.button("Prediksi Risiko", use_container_width=True):
        invalid_cols = [col for col in NUMERIK if input_data[col] == 0.0]
        if invalid_cols:
            st.error(f"Mohon isi semua kolom numerik: {', '.join([display_names[c] for c in invalid_cols])}")
        else:
            df_input = pd.DataFrame([input_data])
            X_proc = preprocessor.transform(df_input)
            prob = model.predict_proba(X_proc)[0][1] * 100
            pred = model.predict(X_proc)[0]
            if prob < 30:
                message = ("Probabilitas Anda terkena serangan jantung relatif rendah. "
                        "Tetap jaga gaya hidup sehat, pola makan seimbang, dan rutin berolahraga.")
            elif prob < 50:
                message = ("Probabilitas Anda terkena serangan jantung sedang. "
                        "Disarankan untuk memeriksa kesehatan jantung secara berkala dan memperhatikan faktor risiko seperti kolesterol dan tekanan darah.")
            else:
                message = ("Probabilitas Anda terkena serangan jantung cukup tinggi. "
                        "Segera konsultasikan dengan dokter dan perhatikan pola hidup, tekanan darah, kolesterol, dan kadar gula darah.")
            st.markdown(f"""
            <div style='text-align:center; font-size:40px; color:#f1faee;'>
            Probabilitas: <span style='color:{'#e63946' if pred==1 else '#2a9d8f'};'>{prob:.2f}% Terkena Serangan Jantung</span>
            </div>
            <div style='text-align:center; font-size:20px; color:#f1faee; margin-top:10px;'>
            {message}
            </div>""", unsafe_allow_html=True)
