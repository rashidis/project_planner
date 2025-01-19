from states import AgentState


def start(state: AgentState) -> AgentState:
    """Work as the starting point to pass on the state to all parallel nodes"""
    return state
