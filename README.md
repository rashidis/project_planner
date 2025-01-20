# AI Project Planner

An intelligent AI-powered assistant designed to streamline project planning and team collaboration through automated task extraction and smart suggestions.

## Features

- **Automated Task Extraction**: Converts meeting transcripts and chat logs into structured task lists
- **Smart Summarization**: Generates concise meeting summaries with key points and decisions
- **Improvement Suggestions**: Provides actionable recommendations based on historical project data
   - **RAG Integration**: Leverages Pinecone for context-aware responses for points of improvement

## Prerequisites

- Python 3.11+
- Poetry for dependency management
- Pinecone API key
- OpenAI or Anthropic API key
- langgraph-cli

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd ai-project-planner
   ```

2. Install dependencies using Poetry:
   ```
   poetry install
   ```

3. Set up environment variables:
   ```
   export PINECONE_API_KEY="your-key-here"
   export OPENAI_API_KEY="your-key-here" # or ANTHROPIC_API_KEY
   export LANGSMITH_API_KEY="your-key-here"
   ```

## Usage
### Using LangGraph Studio
 You can load this repository into LangGraph Studio to visualise and interact with the sample agent.

### Without LangGraph Studio
If you can't use LangGraph Studio, there's a `local_run.py` script to interact with the agent directly.
You just need to run `local_run.py`

You need to take the following steps for setup:

- Install langgraph-cli

   ```brew install langgraph-cli```

- Build the agent

   ```langgraph build -t agent-test```
- Run the setup

   ```docker-compose up```

NOTE: The provided docker-compose.yml file uses the free langgraph redis and postgresql services. You can set your own redis and postgresql creds in the file.

Once the containers are running you can use the `local_run.py` to prompt the agentic system. This system provides two main functionalities for processing text data:

1. **Task Extraction Mode**: Extracts tasks and action items from a meeting transcript or chat log.
2. **Planning Mode**: Facilitates planning based on a given query or set of messages.


### 1. General model
Respond to general or followup questions if the tasks are already generated.

#### Example:
```python
    input_data = {"messages": HumanMessage(content="hi")}
```

With this one, you should see a generic response, or the content based response if it's a follow-up task, from the generator node.

### 2. Planning Mode
Generate plans or solutions based on a provided query or list of messages. In the `local_run.py` you need to change
the input data as follows:

#### Example:
```python
    input_data = {"messages": HumanMessage(content=""), "chat_log":chat_log}
```

With this one, you should be able to see the results both from the executor_graph as well as the suggestor.

## Project Structure

- `agents/`: Core agent implementations for planning and execution
- `nodes/`: Individual processing nodes for tasks, summaries, and suggestions
- `prompts/`: System prompts and templates
- `states/`: State management and type definitions
- `rag_store/`: Document storage and retrieval functionality

## Development

This project uses several tools to maintain code quality:

- Black for code formatting
- isort for import sorting
- pre-commit hooks for automated checks
- Poetry for dependency management


## License

MIT License - See LICENSE file for details

## Author
Shima Rashidi <shima.rashidi7@gmail.com>
