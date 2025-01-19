from langchain_core.messages import SystemMessage

from prompts import SUMMARISER_PROMPT
from states import ExecutorState

from .utils import _get_model


def summarise(state: ExecutorState, config: dict) -> ExecutorState:
    """This function is used tosummarise the meeting highlights from the text.

    :param state: The state of the agent.
    :param config: The configuration of the agent.
    :return: The tasks extracted from the text.
    """
    chat_log = state["chat_log"]
    print(chat_log)

    model_name = config.get("configurable", {}).get("model_name", "openai")
    model = _get_model(model_name)

    messages = [
        SystemMessage(content=SUMMARISER_PROMPT.format(chat_log=chat_log))
    ]
    response = model.invoke(messages)

    print(response)

    return {"summary": response}
