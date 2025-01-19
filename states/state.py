from langgraph.graph import MessagesState


class AgentState(MessagesState):
    tasks: list
    summary: str
