from typing import List, TypedDict

from langchain_core.messages import SystemMessage

from prompts import TASK_EXTRACTION_PROMPT
from states import AgentState

from .utils import _get_model


class Task(TypedDict):
    description: str
    deadline: str
    assignee: str
    other_details: str


class TaskExtractorOutput(TypedDict):
    tasks: list[Task]


def extract_tasks(state: AgentState, config: dict) -> AgentState:
    """This function is used to extract tasks from the text.

    :param state: The state of the agent.
    :param config: The configuration of the agent.
    :return: The tasks extracted from the text.
    """
    chat_log = state["messages"][-1]
    print(chat_log)

    model_name = config.get("configurable", {}).get("model_name", "openai")
    model = _get_model(model_name)

    messages = [SystemMessage(content=TASK_EXTRACTION_PROMPT.format(chat_log=chat_log))]
    response = model.with_structured_output(TaskExtractorOutput).invoke(messages)

    print(response)

    # We return a list, because this will get added to the existing list
    return {"tasks": response}
