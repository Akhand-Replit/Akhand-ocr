import streamlit as st
from PIL import Image
import easyocr
import numpy as np

st.title('বাংলা OCR - Optical Character Recognition')
st.write('ইমেজ থেকে বাংলা টেক্সট 추출')

# Initialize EasyOCR reader for Bengali
reader = easyocr.Reader(['bn'])

uploaded_file = st.file_uploader("একটি ইমেজ ফাইল আপলোড করুন", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
    st.image(image, caption='আপলোড করা ইমেজ', use_container_width=True)
    
    with st.spinner('টেক্সট চিহ্নিত করা হচ্ছে...'):
        # Convert to numpy array
        img_array = np.array(image)
        
        # Perform OCR
        results = reader.readtext(img_array)
        
        # Extract text from results
        extracted_text = '\n'.join([result[1] for result in results])

        if extracted_text.strip():
            st.success('সফলভাবে টেক্সট চিহ্নিত করা হয়েছে!')
            st.subheader("প্রাপ্ত টেক্সট:")
            st.code(extracted_text)
            
            st.download_button(
                label="টেক্সট ডাউনলোড করুন",
                data=extracted_text,
                file_name='extracted_text.txt',
                mime='text/plain'
            )
        else:
            st.warning("ইমেজে কোন টেক্সট পাওয়া যায়নি")
