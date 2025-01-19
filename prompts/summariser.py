from langchain.prompts import ChatPromptTemplate


SUMMARISER_PROMPT = ChatPromptTemplate.from_template(
    """
You are an AI assistant specialised in summarising meeting discussions.
Given a transcript of a meeting as chat log, your task is to:

Chat Log:
{chat_log}

Summarise the key points discussed: Provide a concise overview of the main topics covered.
Identify and list clear next steps: Highlight actionable items, including responsibilities,
deadlines (if mentioned), and other relevant details.
"""
)
