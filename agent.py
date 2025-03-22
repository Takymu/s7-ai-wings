from huggingface_hub import login
from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel, tool

from visiter import visit_web_page
from saver import Memory

login()

agent = CodeAgent(tools=[DuckDuckGoSearchTool(), visit_web_page], model=HfApiModel(), 
                  additional_authorized_imports=['os', 'open', 'io', 'close', 'write'],
                  max_steps=20)

prompt = '''hello. Search in internet some responses on S7 airlines company.
Based on what you find, formulate table of responses, consist of 3 columns: 
date, client emotion, and what need to be improved in company.'''

# agent.run(input("prompt: "))
agent.run(prompt)