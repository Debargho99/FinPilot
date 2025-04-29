# Finbot

<img src="./assets/finbot_sticker.png" alt="Finbot Sticker" width="100"/>

Finbot is a modular AI-driven assistant built using the [LlamaIndex](https://gpt-index.readthedocs.io/) library. It leverages a **Structured Planner Agent** to interact with tools and execute tasks. The project also includes an MCP (Model Context Protocol) server for managing tool specifications.

## Setup
- Clone the repository 
- `pip install --upgrade pip`
- `pip install uv`
- Create your `.env` file with openAI key - `echo 'OPENAI_API_KEY="xyz"' > .env`
- Install Dependencies - `uv sync` if you have a python 3.10 virtualenv already `uv sync --active`
- If you are using `uv sync` make sure to activate the virtualenv `source .venv/bin/activate`


## Components

### MCP Server
The MCP server is responsible for providing tool specifications and handling tool-related interactions. It is built using the `mcp[cli]` package in Python and runs as a standalone server.

### Agent
The `agent.py` script initializes a **Structured Planner Agent** from LlamaIndex. It uses:
- **Tools**: Loaded from the MCP server.
- **LLM**: OpenAI's GPT-4o model.
- **Prompts**: Custom initial and refinement prompts for planning.

The agent interacts with the tools and executes tasks based on user input.


### Running the MCP Server
 To start the server:
1. Navigate to the directory containing the MCP server code.
2. Run the following command:
   ```bash
   uv run --active server.py
   ```
3. To use the MCP inspector `mcp dev server.py`

  

### Running the Agent
To start the agent:
1. Ensure the MCP server is running.
2. Run the `agent.py` script:
   ```bash
   python agent.py
   ```

   The agent will initialize, load tools from the MCP server, and start a chat interface.

## Project Structure
```
finbot/
├── agent.py          # Main script for the Structured Planner Agent
├── prompts.py        # Contains custom prompts for the agent
├── requirements.txt  # Python dependencies
├── .env              # Environment variables
├── README.md         # Project documentation
└── mcp_server/       # MCP server implementation
```

## Logging
The project uses the `loguru` library for logging. Tool metadata is logged during initialization for better traceability.

## License
This project is licensed under the MIT License.
