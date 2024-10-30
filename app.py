from dotenv import load_dotenv
load_dotenv()

import streamlit as st 
import os 
import google.generativeai as genai

 
import os 
os.environ['GOOGLE_API_KEY'] =  "AIzaSyBctzvpLFJTmFseKIIUWz4dlEbKBiSrOLM"

genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

model = genai.GenerativeModel("gemini-pro")

def get_gemini_response(question):

 response=model.generate_content(question)
 return response.text


#initialize our streamlit app

st.header("Gemimi LLM Application")
input=st.text_input("Input",key="input")

submit=st.button("Ask the Question")

if submit:
 response=get_gemini_response(input)
 st.subheader("The response is ")
 st.write(response)