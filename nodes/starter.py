from states import ExecutorState


def start(state: ExecutorState) -> ExecutorState:
    """Work as the starting point to pass on the state to all parallel nodes"""
    return state
