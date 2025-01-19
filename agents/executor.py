from langgraph.graph import StateGraph

from settings import GraphConfig
from nodes import extract_tasks, summarise, start
from states import ExecutorState


workflow = StateGraph(ExecutorState, config_schema=GraphConfig)
workflow.add_node("start", start)
workflow.add_node("task_extractor", extract_tasks)
workflow.add_node("summariser", summarise)

workflow.set_entry_point("start")

workflow.add_edge("start", "task_extractor")
workflow.add_edge("start", "summariser")

executor_graph = workflow.compile()
