# Note: This script runs only on a local IDE with "streamlit run webcam_or_upload_grayscale.py"
import streamlit as st
from PIL import Image

st.subheader("Color to Grayscale Converter")

uploaded_image = st.file_uploader("Upload Image")
st.write("Or u can use your camera")
with st.expander("Start camera"):
    camera_image = st.camera_input("Camera")

if camera_image:
    img = Image.open(camera_image)
    gray_camera_img = img.convert('L')
    st.image(gray_camera_img)

if uploaded_image:
    up_img = Image.open(uploaded_image)
    gray_up_img = up_img.convert("L")
    st.image(gray_up_img)