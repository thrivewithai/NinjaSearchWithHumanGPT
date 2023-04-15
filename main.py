import os

# Set the environment variables
os.environ["OPENAI_API_KEY"] = ""

# zenrows.com
os.environ["ZENROWS_API_PROXY"] = ""

if (os.environ.get("OPENAI_API_KEY") == ""):
    raise Exception("Please set the environment variable OPENAI_API_KEY")
if (os.environ.get("ZENROWS_API_PROXY") == ""):
    raise Exception("Please set the environment variable ZENROWS_API_PROXY")

import requests

from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain.agents import load_tools, initialize_agent, AgentType, tool
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA

llm = ChatOpenAI(temperature=0.0)

# search with bot detection tool 

@tool
def ninjaSearch(targetURL: str) -> str:
    """Scrape the specified URL while bypassing the bot detection for private sites"""
    proxy = os.environ.get("ZENROWS_API_PROXY")
    proxies = {"http": proxy, "https": proxy}
    response = requests.get(targetURL, proxies=proxies, verify=False)

    # Split the response text (html) into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap  = 200, length_function = len)
    docs = text_splitter.create_documents([response.text])

    # Create a vector store and a retriever
    embeddings = OpenAIEmbeddings()
    db = FAISS.from_documents(docs, embeddings)
    retriever = db.as_retriever()
    qa = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff", retriever=retriever)
    # LangChain's tool needs a better way to accept multiple inputs (e.g. target URL & user's question)
    return qa.run("Return a summary of what's written in the page")

tools = load_tools(
    [
        "human",
    ]
)

# Add the custom ninjaSearch tool
tools.append(ninjaSearch)

agent_chain = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)

agent_chain.run("""
Please follow the requirements below and try your best to achive the goal.

Requirements: 
- Ask the "human" using the "human" tool if the goal is unclear or not provided yet.
- If the goal provided is still unclear, or not detailed enough, ask the "human" to provide more information.
- If you don't know the answer, ask the "human" to provide more information.
- Use the tool "ninjaSearch" to bypass bot detection for private websites.
""")