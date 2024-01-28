from dotenv import load_dotenv
#load all the env variables
load_dotenv()
import os  
import streamlit as st 
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv('API_KEY'))


#function to load gemini pro model and get response
model = genai.GenerativeModel('gemini-pro-vision')

def get_gemini_response(input,image):
    if input != "":
        response = model.generate_content([input,image])
    else:
        response = model.generate_content(image)
    return response.text

##InitializeThe Streamlit app

st.set_page_config(page_title='Gemini Image demo')

st.header('Gemini Application')
input = st.text_input('Input prompt:',key='input')

uploaded_file = st.file_uploader("Choose an imag....",type=['jpg','jpeg','png'])
image =  ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image,caption='Uploaded Image.',use_column_width=True)

submit = st.button('Tell me about the image')

##if submit is clicked
if submit:
    response = get_gemini_response(input,image)

    st.subheader('The response is')
    st.write(response)

