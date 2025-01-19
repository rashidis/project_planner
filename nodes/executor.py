from typing import TypedDict, Literal

from langchain_core.messages import SystemMessage

from prompts import TASK_EXTRACTION_PROMPT, SUMMARISER_PROMPT
from states import ExecutorState
from .utils import _get_model


class Task(TypedDict):
    description: str
    status: Literal["backlog", "ready_to_work", "in_progress"]
    deadline: str
    assignee: str
    task_updates: str
    other_details: str


class TaskExtractorOutput(TypedDict):
    tasks: list[Task]


def start(state: ExecutorState) -> ExecutorState:
    """Work as the starting point to pass on the state to all parallel nodes"""
    return state


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


def extract_tasks(state: ExecutorState, config: dict) -> ExecutorState:
    """This function is used to extract tasks from the text.

    :param state: The state of the agent.
    :param config: The configuration of the agent.
    :return: The tasks extracted from the text.
    """
    chat_log = state["chat_log"]
    print(chat_log)

    model_name = config.get("configurable", {}).get("model_name", "openai")
    model = _get_model(model_name)

    messages = [
        SystemMessage(content=TASK_EXTRACTION_PROMPT.format(chat_log=chat_log))
    ]
    response = model.with_structured_output(TaskExtractorOutput).invoke(
        messages
    )

    print(response)

    return {"tasks": response}
