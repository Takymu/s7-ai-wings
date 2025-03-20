from huggingface_hub import login
from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel, tool
import requests

@tool
def visit_web_page(url: str) -> str:
    '''
    This tool can be used to visit page on web by the url. It returns text of the page.
    
    Args:
        url: url to the website.
    Returns:
        function is returning a string, containing all text of the website
    '''
    try:
        page = requests.get(url)
        page.raise_for_status()
        return page.text
    except requests.exceptions.RequestException as e:
        return f"error, cannot access URL: {url}, exception {e}"

login()

agent = CodeAgent(tools=[DuckDuckGoSearchTool(), visit_web_page], model=HfApiModel(), 
                  additional_authorized_imports=['os', 'open', 'io', 'close', 'write'],
                  max_steps=20)

prompt = '''hello. Search in internet some responses on S7 airlines company.
Based on what you find, formulate table of responses, consist of 3 columns: 
date, client emotion, and what need to be improved in company.'''

# agent.run(input("prompt: "))
agent.run(prompt)