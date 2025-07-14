import streamlit as st
import numpy as np
import cv2
from PIL import Image
import io
from cartoonify import cartoonify_image

st.set_page_config(page_title="Cartoonify Your Image", layout="wide")

st.title("🎨 Cartoonify Your Images")

uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read uploaded image as OpenCV BGR image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img_cv2 = cv2.imdecode(file_bytes, 1)  # 1 = color image
    
    # Call your cartoonify function
    cartoon_cv2 = cartoonify_image(img_cv2)
    
    # Convert images from BGR → RGB for display in Streamlit
    orig_rgb = cv2.cvtColor(img_cv2, cv2.COLOR_BGR2RGB)
    cartoon_rgb = cv2.cvtColor(cartoon_cv2, cv2.COLOR_BGR2RGB)
    
    # Display side by side
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Original Image")
        st.image(orig_rgb, use_container_width=True)
    
    with col2:
        st.subheader("Cartoonified Image")
        st.image(cartoon_rgb, use_container_width=True)
    
    # Save cartoon image to BytesIO for download
    cartoon_pil = Image.fromarray(cartoon_rgb)
    buf = io.BytesIO()
    cartoon_pil.save(buf, format="PNG")
    byte_im = buf.getvalue()
    
    st.download_button(
        label="Download Cartoon Image",
        data=byte_im,
        file_name="cartoonified.png",
        mime="image/png"
    )
else:
    st.info("Please upload an image to get started.")
