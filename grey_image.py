import streamlit as st
from PIL import Image

st.subheader("Color to Grayscale Converter")

with st.expander("Upload Image"):
    uploaded_img = st.file_uploader("Upload Image")

    if uploaded_img is not None:
        img = Image.open(uploaded_img)
        gray_img = img.convert('L')
        st.image(gray_img)