from typing import TypedDict
from langgraph.graph import MessagesState


class PlannerState(MessagesState):
    chat_log: str
    tasks: list
    summary: str
    instruction: str
    generated_output: str


class ExecutorState(TypedDict):
    chat_log: str
    tasks: list
    summary: str
