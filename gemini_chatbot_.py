import streamlit as st
import google.generativeai as genai
import os
from datetime import date

# Set API Key
os.environ["GOOGLE_API_KEY"] = "AIzaSyD4WveSDzvsuoW_M-ovQ6ifh3HDZOW3_SM"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# Load Gemini model
model = genai.GenerativeModel("models/gemini-1.5-flash-latest")

# Title
st.title("💊 MedAlert - Medicine Info Checker (AI-Powered)")
st.write("Enter a medicine name to get AI-powered insights including usage, dosage, side effects, and more.")

# Input for Medicine
medicine_name = st.text_input("Enter Medicine Name", placeholder="e.g. Paracetamol, Amoxicillin")

if st.button("Get Medicine Info") and medicine_name.strip() != "":
    prompt = f"""
    You are a professional medical assistant AI trained to provide detailed medicine information.

    Give a full report on the medicine: *{medicine_name}*.

    Format your response like this:

    - *Medicine Name*:
    - *Common Brand Names*:
    - *Medical Uses*:
    - *Dosage Instructions*:
    - *Common Side Effects*:
    - *Warnings & Precautions*:
    - *Drug Interactions*:
    - *Advice for Storage*:
    - *Disclaimer*: This is AI-generated info. Always consult a certified doctor or pharmacist.

    Date: {date.today().strftime('%Y-%m-%d')}
    """

    with st.spinner("Fetching medical details..."):
        response = model.generate_content(prompt)
        st.success("Here is the medicine information:")
        st.markdown(response.text.strip())

elif medicine_name.strip() == "":
    st.warning("Please enter a valid medicine name.")
