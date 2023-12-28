# Semantic Kernel Python Hello World Starter

The application showcases how to connect FastAPI with an LLM model, and expose it's functions over na API. 

## Prerequisites

- [Python](https://www.python.org/downloads/) 3.8 and above
  - [Poetry](https://python-poetry.org/) is used for packaging and dependency management
  - [Semantic Kernel Tools](https://marketplace.visualstudio.com/items?itemName=ms-semantic-kernel.semantic-kernel)

## Configuring the starter

The starter can be configured with a `.env` file in the project which holds api keys and other secrets and configurations.

Make sure you have an
[Open AI API Key](https://openai.com/api/) or
[Azure Open AI service key](https://learn.microsoft.com/azure/cognitive-services/openai/quickstart?pivots=rest-api)

Copy the `.env.example` file to a new file named `.env`. Then, copy those keys into the `.env` file:

```Press   ⇧   ⌘   V   to select the text fragment that you have previously copied to the clipboard.
OPENAI_API_KEY=""
OPENAI_ORG_ID=""
```

## Running the starter


To build and run the console application from the terminal use the following commands:

```powershell
poetry install
poetry run python main.py
```
