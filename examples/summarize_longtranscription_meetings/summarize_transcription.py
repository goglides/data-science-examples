from langchain.chains.summarize import load_summarize_chain
from langchain_openai import ChatOpenAI
from langchain.schema.document import Document
import gradio as gr
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("openai_api_key")
llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo", api_key=api_key)

def summary(trans):
  # Create a document object with some text and metadata
  doc = Document(page_content=trans, metadata={"source": "local"})
  chain = load_summarize_chain(llm, chain_type="stuff")
  return chain.run([doc])

summ = gr.Interface(
    summary,
    [
      gr.Textbox(label="Meetings Transcription:", value="")
    ],
    "textbox",
    title="Summarize Long Transcription Meetings",
    theme = "gradio/monochrome"
)
summ.launch()
  