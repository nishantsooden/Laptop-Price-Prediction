import streamlit as st
import pickle
import pandas as pd

import os
import pickle

import os
import pickle

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__)) 
BASE_DIR = os.path.dirname(CURRENT_DIR)

MODEL_PATH = os.path.join(BASE_DIR, "model", "laptop.pkl")

model = pickle.load(open(MODEL_PATH, "rb"))

model = pickle.load(open(MODEL_PATH, "rb"))
st.set_page_config(page_title="Laptop Price Prediction", layout="centered")
st.title("💻 Laptop Price Prediction")


brand = st.selectbox("Brand", ['Apple','LG','Dell','HP','Samsung','MSI','Lenovo','Acer','Asus'])
cpu_brand = st.selectbox("CPU Brand", ['AMD','Intel','Apple Silicon'])
ram_gb = st.selectbox("RAM (GB)", [4,8,16,24,32,64])
storage_gb = st.selectbox("Storage (GB)", [256,512,1024,2048])
storage_type = st.selectbox("Storage Type", ['HDD','SSD','Hybrid'])
gpu_brand = st.selectbox("GPU Brand", ['NVIDIA','AMD','Intel','M-Series'])
dedicated_gpu_vram_gb = st.selectbox("GPU VRAM (GB)", [0,2,4,6,8,12])
screen_size_inch = st.selectbox("Screen Size (inch)", [11.0,11.6,12.0,13.0,14.0,15.0,16.0,17.0])
screen_type = st.selectbox("Screen Type", ['TN','VA','IPS','OLED'])
resolution = st.selectbox("Resolution", ['1366x768','1920x1080','2560x1440','3840x2160'])
weight_kg = st.slider("Weight (kg)", 1.0, 4.0, step=0.01)
battery_wh = st.selectbox("Battery (Wh)", [35,45,55,65,80,99])
release_year = st.selectbox("Release Year", [2016,2017,2018,2019,2020,2021,2022,2023,2024])
os = st.selectbox("Operating System", ['macOS','Windows 10','Windows 11','Ubuntu','ChromeOS','Fedora'])
region = st.selectbox("Region", ['India','SE Asia','Europe','Middle East','USA'])
user_rating = st.slider("User Rating", 1.0, 5.0, step=0.1)
num_reviews = st.number_input("Number of Reviews", min_value=0, value=1000)
touchscreen = st.selectbox("Touchscreen", [0,1])
backlit_keyboard = st.selectbox("Backlit Keyboard", [0,1])
fingerprint_reader = st.selectbox("Fingerprint Reader", [0,1])
wifi6_supported = st.selectbox("WiFi 6 Support", [0,1])


width, height = map(int, resolution.split("x"))
resolution_pixels = width * height


input_data = pd.DataFrame([{
    'brand': brand,
    'cpu_brand': cpu_brand,
    'ram_gb': ram_gb,
    'storage_gb': storage_gb,
    'storage_type': storage_type,
    'gpu_brand': gpu_brand,
    'dedicated_gpu_vram_gb': dedicated_gpu_vram_gb,
    'screen_size_inch': screen_size_inch,
    'screen_type': screen_type,
    'resolution_pixels': resolution_pixels,
    'weight_kg': weight_kg,
    'battery_wh': battery_wh,
    'release_year': release_year,
    'os': os,
    'region': region,
    'user_rating': user_rating,
    'num_reviews': num_reviews,
    'touchscreen': touchscreen,
    'backlit_keyboard': backlit_keyboard,
    'fingerprint_reader': fingerprint_reader,
    'wifi6_supported': wifi6_supported
}])


if hasattr(model, "feature_names_in_"):
    input_data = input_data.reindex(
        columns=model.feature_names_in_,
        fill_value=0
    )


if st.button("Predict Price 💰"):
    try:
        price = model.predict(input_data)[0]
        st.success(f"💵 Predicted Price: ₹ {round(price)}")
    except Exception as e:
        st.error(f"Prediction failed ❌: {e}")
