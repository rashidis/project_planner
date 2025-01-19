from typing import TypedDict
from langgraph.graph import MessagesState


class PlannerState(TypedDict):
    generated_output: str


class ExecutorState(MessagesState):
    chat_log: str
    tasks: list
    summary: str
