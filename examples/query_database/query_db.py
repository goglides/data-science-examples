import streamlit as st
from langchain.agents import create_sql_agent
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_openai import ChatOpenAI
from langchain.sql_database import SQLDatabase
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("openai_api_key")
st.title("Query Database using Natural Language")
llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo", api_key=api_key)
def mysqldb_agent(db, llm, input):
    toolkit = SQLDatabaseToolkit(db=db, llm=llm)
    agent_executor = create_sql_agent(
        llm=llm,
        toolkit=toolkit,
        verbose=True
    )
    return agent_executor.run(input)

st.subheader("Query MySQL Database:", divider='rainbow')
db_user = st.text_input("UserName:","root")
db_password = st.text_input("Password:","root")
db_host = st.text_input("Host:","localhost")
db_name = st.text_input("DBName:","bankdata")
try:
    db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}")
    print("Database connection successful!")
except Exception as e:
    # If an exception occurs, print an error message
    print(f"Error connecting to the database: {str(e)}")

input_text = st.text_input("Enter your question here:","What is the maximum transaction in database table?")
button = st.button("Generate Response")
if button and input_text:
    with st.spinner("Generating Response!"):
        reply = mysqldb_agent(db, llm, input_text)
    st.write(reply)



