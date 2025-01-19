from functools import lru_cache

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


def should_continue(state):
    """This function is used to determine whether to continue or not.

    :param state: The state of the agent.
    :return: Whether to continue or not.
    """
    messages = state["messages"]
    last_message = messages[-1]
    # If there are no tool calls, then we finish
    if not last_message.tool_calls:
        return "end"
    # Otherwise continue
    else:
        return "continue"
