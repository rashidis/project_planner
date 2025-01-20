# AI Project Planner

An intelligent AI-powered assistant designed to streamline project planning and team collaboration through automated task extraction and smart suggestions.

## Features

- **Automated Task Extraction**: Converts meeting transcripts and chat logs into structured task lists
- **Smart Summarization**: Generates concise meeting summaries with key points and decisions
- **Improvement Suggestions**: Provides actionable recommendations based on historical project data
- **Multi-Model Support**: Works with both OpenAI and Anthropic models
- **RAG Integration**: Leverages Pinecone for context-aware responses

## Prerequisites

- Python 3.11+
- Poetry for dependency management
- Pinecone API key
- OpenAI or Anthropic API key

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
```

## Usage
This system provides two main functionalities for processing text data:

1. **Task Extraction Mode**: Extracts tasks and action items from a meeting transcript or chat log.
2. **Planning Mode**: Facilitates planning based on a given query or set of messages.

### 1. Task Extraction Mode
Extract actionable tasks and insights from a meeting transcript or chat log.

#### Example:
```python
from agents import executor_graph

# Replace with your meeting transcript or chat log
chat_log = "your meeting transcript or chat log here"

# Invoke the task extraction process
result = executor_graph.invoke({
    "chat_log": chat_log
})

# Print or process the result
print(result)
```

### 2. Planning Mode
Generate plans or solutions based on a provided query or list of messages.

#### Example:
```python
from agents import planner_graph

# Replace with your query or list of messages
messages = ["your query here"]

# Invoke the planning process
result = planner_graph.invoke({
    "messages": messages
})

# Print or process the result
print(result)
```


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
