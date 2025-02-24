import streamlit as st
from PIL import Image
import pytesseract
import numpy as np

st.title('বাংলা OCR কনভার্টার')
st.write('বাংলা লেখা সমৃদ্ধ একটি ইমেজ আপলোড করুন')

# File uploader
uploaded_file = st.file_uploader("একটি ইমেজ নির্বাচন করুন...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Display the image
    image = Image.open(uploaded_file)
    st.image(image, caption='আপলোডকৃত ইমেজ', use_column_width=True)
    
    # Convert image to RGB
    image = image.convert('RGB')
    
    # Perform OCR
    try:
        text = pytesseract.image_to_string(image, lang='ben')
        
        # Display OCR results
        st.subheader("পাঠ্য উত্তোলন করা হয়েছে")
        st.text_area("OCR ফলাফল", text, height=300)
        
        # Add copy instructions
        st.write("উপরের লেখা সিলেক্ট করে Ctrl+C (Windows/Linux) বা Cmd+C (Mac) চাপে কপি করুন")
        
    except Exception as e:
        st.error(f"OCR প্রক্রিয়ায় ত্রুটি: {str(e)}")
