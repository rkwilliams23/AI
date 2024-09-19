import streamlit as st
from utils import *

# Creating Session state variable
if 'HuggingFace_API_Key' not in st.seesion_state:
  st.session_state['HuggingFace_API_Key'] =''
if 'Pinecone_API_Key' not in st.session_state:
  st.seesion_state['Pinecone_API_Key'] =''


#
st.title('🤖 AI Assistence For Website')

#********SIDE BAR Funtionality started********

# Sidebar to capture the API keys
st.sidebar.title("😎🔑")
st.session_state['HuggingFace_API_key']= st.sidebar.text_input("What's your HuggingFace API key?",type="password")
st.session_state['Pinecone_API_key']= st.sidebar.text_input("what's your Pinecone API key?",type="password")

load_button = st.sidebar.button("Load data to Pinecone", key="load_button")

#if the bove button is clicked, pushing the data to Pinecone...
if load_button:
  #Proceed only if API keys are provided
  if st.session_state['HuggingFace_API_Key'] !="" and st.seesion_state['Pinecone_API_Key']!="":
    
    #Fetch data from site
    site_data=get_website_data("https://jobs.excelcult.com/wp-sitemap-posts-post-1.xml")
    st.write("Data pull done...")
    
    #Split data into chunks
    st.write("Spliting data done...")
    
    #Creating embeddings instance
    st.write("Embeddings instance creation done...")
    
    #Push data to Pinecone
    st.write("Pushing data to Pinecone done...")
    
    st.sidebar.success("Data pushed to Pinecone successfully!")
  else:
    st.sidebar.error("Ooopssss!!! Please provide API keys.....")

#********SIDE BAR Funtionality ended********
