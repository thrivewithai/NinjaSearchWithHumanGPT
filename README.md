# NinjaSearchWithHumanGPT 🥷
An agent with human in the loop that can search the web for information while bypassing bot detection for private sites.

## Getting Started
To get started with the repo, you will need to set up the necessary environment variables. In particular, you will need to create and set the following environment variables:
* OPENAI_API_KEY: Your OpenAI API key
* ZENROWS_API_PROXY: A proxy for bypassing bot detection on private websites\*

OpenAI's gpt-3.5 is used by default, but you can use [other models LangChain supports](https://python.langchain.com/en/latest/modules/models/llms/integrations.html). 

\* Zenrows: https://zenrows.com

Additionally, you will need to make sure the dependencies are installed:

`python3 -m pip install requirements.txt`
## Usage
Once you have set up the necessary environment variables and installed the langchain package, you can start using the chatbot. Simply run the main.py file:

`python3 main.py`

The chatbot will prompt you to follow certain requirements in order to achieve your goal. If the goal is unclear or not provided, the chatbot will prompt you to ask a "human" (you) using the "human" tool, which is included by default. If the goal is still unclear or not detailed enough, the chatbot will prompt you to ask the "human" to provide more information.

The chatbot also includes a custom tool called ninjaSearch which is designed to bypass bot detection for private websites. 
The tool will scrape the specified URL and return a summary of the page's contents.

The tool summarizes the response from the URL in the following steps:
1. Split the html into chunks using `RecursiveCharacterTextSplitter`
2. Create a vector representation of the chunks and save it into db (we used FAISS in this example)
3. Create a retriever (`RetrievalQA`) from the llm and db so that we can ask questions from the content of the page.

## Note

- I've tested successfully with LinkedIn urls (e.g., https://www.linkedin.com/in/hirokihori), but after a couple of attempts, I started getting rejected. It's still not working at the time of writing this (4/15/2023). I rotated my proxy, but it still blocks me so LinkedIn automatically started blocking requests through Zenrows (?) Not really sure. 
- I love the fact that the LLM asks me if they are not sure about the answer. Autonomous agents with human-in-the-loop are pretty powerful and I believe that's the way to go. 

## Contributing
If you would like to contribute to this project, please submit a pull request on GitHub.
