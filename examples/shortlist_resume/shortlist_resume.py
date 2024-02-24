import gradio as gr
from langchain_community.document_loaders import PyPDFLoader
from openai import OpenAI
from fuzzywuzzy import fuzz
import os
# from dotenv import load_dotenv
# load_dotenv()
# api_key = os.getenv("openai_api_key")
#Create a OpenAI object
client = OpenAI(api_key="api_key")

def extract_skills(data):
  response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "You are an expert in extracting key technical skill, experience, education qualification from the given resume/job description"},
      {"role": "user", "content": data}
    ]
  )
  return response.choices[0].message.content
def resume_shortlist(desc, path, criteria):
  question = "Extract all the key skills, experience, education qualification from the text given"
  doc1 = extract_skills(question+desc)
  print(doc1)
  loader = PyPDFLoader(path)
  docs = loader.load()
  doc2 = extract_skills(question+str(docs[0].page_content))
  print(doc2)
  match_percentage = fuzz.ratio(doc1, doc2)
  if match_percentage >= criteria:
    return "This resume qualified for screening round!\n\n"+"Match Percentage: "+str(match_percentage)
  else:
    return "It does not match with our job description!\n\n"+"Match Percentage: "+str(match_percentage)
  
#gradio web interface
resume = gr.Interface(
    resume_shortlist,
    [
      gr.Textbox(label="Job Description:", value=""),
      gr.File(label="Resume:", file_count="single"),
      gr.Number(label="Match Criteria:"),
    ],
    "textbox",
    title="Shortlist Resume",
    theme = "gradio/monochrome"
)
resume.launch()