from typing import Literal, TypedDict

from langgraph.graph import END, StateGraph

from nodes import extract_tasks
from states import AgentState


class GraphConfig(TypedDict):
    """Configuration type for the graph workflow.

    This TypedDict defines the configuration schema for the workflow graph,
    specifying which language model to use for the agent.
    """

    model_name: Literal["openai", "anthropic"]


workflow = StateGraph(AgentState)
workflow.add_node("task_extractor", extract_tasks)

workflow.set_entry_point("task_extractor")

workflow.add_edge("task_extractor", END)

planner_graph = workflow.compile()
