from typing import Literal, TypedDict

from langgraph.graph import StateGraph

from nodes import extract_tasks, summarise, start
from states import AgentState


class GraphConfig(TypedDict):
    """Configuration type for the graph workflow.

    This TypedDict defines the configuration schema for the workflow graph,
    specifying which language model to use for the agent.
    """

    model_name: Literal["openai", "anthropic"]


workflow = StateGraph(AgentState)
workflow.add_node("start", start)
workflow.add_node("task_extractor", extract_tasks)
workflow.add_node("summariser", summarise)

workflow.set_entry_point("start")

workflow.add_edge("start", "task_extractor")
workflow.add_edge("start", "summariser")

executor_graph = workflow.compile()
