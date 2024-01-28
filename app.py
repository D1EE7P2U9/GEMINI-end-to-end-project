from dotenv import load_dotenv
#load all the env variables
load_dotenv()
import os  
import streamlit as st 
import google.generativeai as genai

genai.configure(api_key=os.getenv('API_KEY'))


#function to load gemini pro model and get response
model = genai.GenerativeModel('gemini-pro')
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

#set up streamlit app

st.set_page_config(page_title="Q&A")
st.header('Gemini LLM Application')

input = st.text_input('Input: ',key='input')
submit = st.button('Ak the question')

#When the submit is clicked

if submit:
    response = get_gemini_response(input)
    st.subheader('The Response is')
    st.write(response)
