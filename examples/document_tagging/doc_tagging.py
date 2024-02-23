#Import necessary libraries
import gradio as gr
from langchain.chains import create_tagging_chain_pydantic
from langchain_openai import ChatOpenAI
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_community.document_loaders import PyPDFLoader
import os
import dotenv
dotenv.load_dotenv()
#Validate data using pydantic
class Tags(BaseModel):
    Category: str = Field(..., enum=["Finance", "Politics", "Technology"])
#Function takes input as list of file paths and return corresponding tag
def tagging(file_paths):
  llm = ChatOpenAI(temperature=0, model="gpt-4")
  #pydantic chain which is key for tagging
  chain = create_tagging_chain_pydantic(Tags, llm)
  docs = ""
  #Iterating over list of paths
  for path in file_paths:
    head = os.path.split(path)
    loader = PyPDFLoader(path)
    doc = loader.load()
    docs += "FileName: "+str(head[1])+"\n"+str(chain.run(doc))+"\n\n"
  return docs
#User interface using gradio
entity = gr.Interface(
    tagging,
    [
    gr.File(label="Files", file_count="multiple"),
    ],
    "textbox",
    title="Tag the given Documents",
    theme = "gradio/monochrome"
)
entity.launch()