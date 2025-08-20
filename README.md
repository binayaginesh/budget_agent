<h1 align="center">BUDGET_AGENT</h1>

<p align="center">
    <em><code>AI-powered Budget-Friendly Product Finder</code></em>
</p>

---

## Overview  

<p>
Budget Agent is an Agentic AI project that goes beyond static chatbots by reasoning, planning, and interacting with external tools.  
It helps users find the most budget-friendly products by searching online, analyzing options, and providing intelligent recommendations.
</p>

<p>
<b>Core Idea:</b> AI agent searches, compares, and suggests the best product under budget.  
<b>AI Backbone:</b> Powered by LangChain, enabling the Reason → Action → Observation loop.  
<b>LLM Used:</b> Groq LLM for high-speed reasoning.  
<b>External Tool:</b> Tavily Search API to fetch live product info and pricing.  
<b>Frontend:</b> Built with Streamlit for a simple, interactive UI.  
</p>

---

## Project Structure  

```sh
budget_agent/
├── agent.py           
├── app.py             
└── requirements.txt   
````

---

## Getting Started

<p><b>Prerequisites</b></p>
<p>Make sure you have:</p>

```sh
Python 3.8+
pip (Python package manager)
```

<p><b>Installation</b></p>

```sh
git clone https://github.com/binayaginesh/budget_agent.git
cd budget_agent
pip install -r requirements.txt
```

API Key Setup
<p> You need API keys for the LLM and search tool. Create a file named <code>.env</code> in the project root and add: </p>

```sh
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

<p> Replace <code>your_groq_api_key</code> and <code>your_tavily_api_key</code> with actual keys from: </p>
<a href="https://console.groq.com" target="_blank">Groq Console</a> (for Groq LLM)
<a href="https://tavily.com" target="_blank">Tavily Search API</a>

<p><b>Running the App</b></p>

```sh
streamlit run app.py
```

<p>
This will open a local web app where you can enter queries such as:  
"Find me the best smartphone under ₹20,000"  
The agent will search online, analyze products, and recommend the best fit.
</p>

---

## Contributing

```sh
# Fork the repo and clone your fork
git clone https://github.com/your-username/budget_agent.git
cd budget_agent

# Create a new branch
git checkout -b feature-name

# Make changes and commit
git commit -m "Added feature X"

# Push the branch
git push origin feature-name
```

<p>
Then, open a Pull Request with a description of your changes.
</p>

---
