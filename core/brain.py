#Talk to LLM

from langchain.tools import tool
import core.AI_Prompts as pm
from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from typing import Literal
from dotenv import load_dotenv, find_dotenv
import os
import json
import re
import ollama
from tools.registry import *
import pathlib

load_dotenv(dotenv_path="data/.env")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGSMITH_KEY")  # Your LangSmith Key
os.environ["LANGCHAIN_PROJECT"] = "My First Trace" 

@tool
def open_app(app):
    """Open desktop applications"""
    try:
        tool_launch_app(app)
    except Exception as e:
        return f"Failed to open app. App:{app} Error:{e}"

@tool
def search_files(keyword:str):
    """Search for files that include the keyword given by user"""
    
    file_list=[]
    desktop = pathlib.Path("C:/Users/chris/Downloads")
    for file in desktop.rglob("*"):
        if str(keyword).lower() in file.name.lower() and file.is_file():
            file_list.append(file)
    print(str(file_list))    

    if not file_list:
        return "No files found"
    return file_list
    
@tool
def open_files(filepath:str):
    """Open the correct file"""
    
    try:
        os.startfile(filepath)
    except Exception as e:
        return f"Failed to open file. File:{filepath} Error:{e}"

tools = [open_app, open_files, search_files]

#Future Changes: Stream response, add fallback if invalid json is returned
class Router(BaseModel):
    tool: Literal["chat","launch_app","open_file","summarize"]
    #tool: str
    arguments: dict[str, str] = {}
    

class Brain():
    def __init__(self, model =("openai/gpt-oss-120b")):
        
        my_api_key = os.getenv("GROQ_API_KEY")
        self.llm = ChatGroq(model=model, temperature=0, max_tokens=500,api_key=my_api_key)
        self.agent = create_agent(model=self.llm, tools=tools, system_prompt=pm.strict_prompt)
    def tool_caller(self, history):
        
        try: 
            print("tool caller")
            response = self.agent.invoke({"messages": [{"role": "system", "content": str(history)}]})
            print(f"arguemnt:{response["messages"][-1].additional_kwargs["reasoning_content"]}")
            return response["messages"][-1].additional_kwargs["reasoning_content"]
            
        except Exception as e: 
            error_string = str(e)
    
        # 2. Find where the JSON dictionary starts in the error text
        if "{" in error_string:
            json_part = error_string[error_string.find("{"):]
            
            try:
                # 3. Convert the string into a readable Python dictionary
                # Note: If the API uses single quotes, we replace them with double quotes for valid JSON parsing
                error_data = json.loads(json_part.replace("'", '"'))
                
                # 4. Extract and print the exact failed text block
                failed_text = error_data['error']['failed_generation']
                
                print("--- FAILED GENERATION START ---")
                print(failed_text)
                print("--- FAILED GENERATION END ---")
                
            except Exception:
                print("Could not parse the error JSON automatically.")
                print(f"Raw error text: {error_string}")
                
                return "Response Generation Failed"

    def jarvis_reply(self, history):
        return str(self.llm.invoke(pm.conversation_prompt.format(text=history)).content)
        
        