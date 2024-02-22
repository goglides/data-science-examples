import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("openai_api_key")
#Streamlit Subheading
st.subheader("SQL equivalent code generation in pandas", divider='rainbow')
#Create a OpenAI object
client = OpenAI(api_key=api_key)
#Funtion take natural language query as input and returns pandas code
def Sql2pandas(query):
  response = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages=[
      {"role": "system", "content": "You are an expert in SQL and Pandas, For the given sql query give me equivalent pandas statements"},
      {"role": "user", "content": query}
    ]
  )
  return response.choices[0].message.content
#Input through streamlit Natural language as input
input_text  = st.text_area("Write SQL Query here")
#Streamlit button to generate response
button = st.button("Generate Response")
#Validate button and input text.
if button and input_text:
    with st.spinner("Holdon Generating Pandas Statement!"):
        resp = Sql2pandas(input_text)
    st.write(resp)
