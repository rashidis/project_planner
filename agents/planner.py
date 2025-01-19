from typing import Literal, TypedDict

from langgraph.graph import StateGraph, END
from langgraph.types import Command

from nodes import generate, plan
from states import PlannerState
from agents import executor_graph


def call_executor_graph(planner_state: PlannerState) -> Command:
    """Call the exacutor_graph if planner decides it is required

    :param planner_state: The current state of the Planner
    :return: The command containing the next node and the updated state
    """
    executor_graph_input = {"chat_log": planner_state["chat_log"]}
    executor_graph_output = executor_graph.invoke(executor_graph_input)

    return Command(
        goto=END,
        update={
            "tasks": executor_graph_output["tasks"],
            "summary": executor_graph_output["summary"],
            "chat_log": "",
        },
    )


class GraphConfig(TypedDict):
    """Configuration type for the graph workflow.

    This TypedDict defines the configuration schema for the workflow graph,
    specifying which language model to use for the agent.
    """

    model_name: Literal["openai", "anthropic"]


workflow = StateGraph(PlannerState)
workflow.add_node("planner", plan)
workflow.add_node("executor_graph", call_executor_graph)
workflow.add_node("generator", generate)


workflow.set_entry_point("planner")

planner_graph = workflow.compile()
