# NinjaSearchWithHumanGPT
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

## Contributing
If you would like to contribute to this project, please submit a pull request on GitHub.
