from functools import lru_cache
from loguru import logger
import os

from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI


@lru_cache(maxsize=4)
def _get_model(model_name: str):
    """This function is used to get the model for the agent.

    :param model_name: The name of the model to use.
    :return: The model to use.
    """
    if model_name == "openai":
        model = ChatOpenAI(temperature=0, model_name="gpt-4o-mini")
    elif model_name == "anthropic":
        model = ChatAnthropic(
            temperature=0, model_name="claude-3-sonnet-20240229"
        )
    else:
        raise ValueError(f"Unsupported model type: {model_name}")

    return model


from pinecone import Pinecone
from pinecone_plugins.assistant.models.chat import Message

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])
assistant = pc.assistant.Assistant(assistant_name="projectretriver")


def retriever_tool(query: str) -> str:
    """retriever tool which uses a pinecone assistant to respond to the query based on stored documents

    :param query: input query
    :return: response generated from the rag system
    """
    logger.info(f"[retriever_tool] query is:{query}")

    msg = Message(content=str(query))
    resp = assistant.chat(messages=[msg])
    logger.info(f"[retriever_tool] resp is:{resp}")

    return resp["message"]["content"]
