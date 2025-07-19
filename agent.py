from tavily import TavilyClient
from langchain_tavily import TavilySearch
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()
tavily_api_key = os.getenv("TAVILY_API_KEY")

llm = ChatGroq(
    model="llama3-8b-8192", 
    api_key=os.getenv("GROQ_API_KEY")
)
tool = TavilySearch(tavily_api_key=tavily_api_key)

tools = [
    Tool(
        name="Tavily Search",
        func=tool.invoke,
        description="Useful for finding ecommerce product data like prices, features, comparisons",
    )
]

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)

def run_agent(query):
    response = agent.run(query)
    return response
