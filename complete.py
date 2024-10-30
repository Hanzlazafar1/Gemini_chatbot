from dotenv import load_dotenv
from PIL import Image
import streamlit as st
import os
import google.generativeai as genai

load_dotenv()

 
os.environ['GOOGLE_API_KEY'] = "AIzaSyBctzvpLFJTmFseKIIUWz4dlEbKBiSrOLM"   
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

model = genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_response(input_text, image=None):
    if input_text and image:
        response = model.generate_content([input_text, image])
    elif input_text:
        response = model.generate_content(input_text)
    elif image:
        response = model.generate_content(image)
    else:
        response = "Please provide some input."
    return response.text

# Streamlit app layout
st.title("Gemini LLM and Image Analysis Demo")
st.write("### Experience the power of Gemini LLM with text and image-based AI capabilities!")

# Input fields
st.subheader("Ask Gemini Anything")
input_text = st.text_input("Enter your question or description:", key="input")

st.subheader("Or Upload an Image for Analysis")
uploaded_image = st.file_uploader("Choose an image", type=['jpg', 'jpeg', 'png'])

# Display uploaded image
if uploaded_image:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_column_width=True)

# Submit button
if st.button("Generate Response"):
    response = get_gemini_response(input_text, uploaded_image if uploaded_image else None)
    st.subheader("Gemini's Response")
    st.write(response)

# Style adjustments for a more polished interface
st.markdown("""
    <style>
    .stButton button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 24px;
        font-size: 16px;
        border-radius: 8px;
    }
    .stTextInput input {
        border: 1px solid #ddd;
        padding: 8px;
        font-size: 16px;
        width: 100%;
    }
    .stFileUploader div {
        border: 1px solid #ddd;
        border-radius: 8px;
        padding: 10px;
    }
    </style>
""", unsafe_allow_html=True)
