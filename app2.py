from flask import Flask, render_template, request
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Set up Google API key for generative AI
os.environ['GOOGLE_API_KEY'] =  "AIzaSyBctzvpLFJTmFseKIIUWz4dlEbKBiSrOLM"  # Move the key to a .env file for security

# Configure generative AI model
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
model = genai.GenerativeModel("gemini-pro")

def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

# Set up Flask route for the main page
@app.route("/", methods=["GET", "POST"])
def home():
    response = ""
    if request.method == "POST":
        user_input = request.form.get("input")
        if user_input:
            response = get_gemini_response(user_input)
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
