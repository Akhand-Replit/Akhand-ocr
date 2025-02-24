import streamlit as st
from PIL import Image
import pytesseract
import os

# Set Tesseract path (not needed if installed in system PATH)
# pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

st.title('বাংলা OCR - Optical Character Recognition')
st.write('বাংলা ভাষায় লেখা ইমেজ থেকে টেক্সট নিরূপণ')

uploaded_file = st.file_uploader("একটি ইমেজ ফাইল আপলোড করুন...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='আপলোড করা ইমেজ', use_column_width=True)
    
    with st.spinner('ইমেজ প্রসেস করা হচ্ছে...'):
        # Perform OCR with Bengali language
        text = pytesseract.image_to_string(image, lang='ben')
        
        if text.strip():
            st.success('OCR সম্পন্ন হয়েছে!')
            st.subheader("নিরূপিত টেক্সট:")
            st.code(text)
            
            # Add copy button functionality
            st.download_button(
                label="টেক্সট কপি করুন",
                data=text,
                file_name='extracted_text.txt',
                mime='text/plain'
            )
        else:
            st.warning("ইমেজ থেকে কোন টেক্সট পাওয়া যায়নি")
