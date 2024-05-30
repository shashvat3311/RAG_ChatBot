import streamlit as st 
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.vectorstores import FAISS
import google.generativeai as genai
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
# from langchain

load_dotenv()
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

st.header("Streamlit Application ")
input =st.text_input("Ask your Questions")
buttonSubmit=st.button("Submit")

model_gemini_pro=ChatGoogleGenerativeAI(model="gemini-pro",temperature=0.3)
model_gemini_pro_vision=ChatGoogleGenerativeAI(model='gemini-pro-vision',temperature=0.3)

def geminiPro(text):
    response=model_gemini_pro.invoke(text)
    return response.content

def geminiProVision(text,image):
    print("geminiProVisionInvoked")
    st.image(image)
    st.write(text)

    message=HumanMessage(content=[
    {
        "type":"text",
        "text":"Write the description about the production shown inn the image for mentioning it in ecommerce website "
    },
    {
        "type":"image_url",
        "image_url":"image.png"
     }
])
    response=model_gemini_pro_vision.invoke([message])
    # print(response.content)
    return response.content
# def fun1():
#     st.write("Welcome to the streamlit APP:")

with st.sidebar:
    st.title("Gemini-Pro-Vision")
    image=st.file_uploader("Upload Image:")
    inputImage=st.text_input("Enter Query for Image:")
    
    # st.image("")
    if st.button("Execute"):
        with st.spinner("Processing.."):
            if not image or not inputImage:
                 st.error("Please upload Image and Image Query")
            elif image and inputImage:  
                  content= geminiProVision(inputImage,image)
                  st.success(content)
                    
           
if buttonSubmit and not input:
    st.error("Please Enter Your Question")
elif input and buttonSubmit:
    content=geminiPro(input)
    st.success(f"Your Input: {input}\n\n Generated Response: {content}")



     