from loguru import logger
from typing import TypedDict
from langgraph.types import Command
from langchain_core.messages import SystemMessage

from states import PlannerState
from prompts import GENERATOR_PROMPT, SUGGESTOR_PROMPT
from .utils import _get_model, retriever_tool


class Improvement(TypedDict):
    details: str
    actions: str


class SuggestorOutput(TypedDict):
    improvements: list[Improvement]


def plan(state: PlannerState, config: dict) -> Command:
    """This function is used tosummarise the meeting highlights from the text.

    :param state: The state of the agent.
    :param config: The configuration of the agent.
    :return: The tasks extracted from the text.
    """
    if state.get("chat_log", []):
        logger.info(
            f"[plan node] chat_log detected, calling executor_graph to process the log"
        )
        return Command(goto="executor_graph")

    logger.info(
        f"[plan node] chat_log not detected, calling generator to generate a response"
    )
    instruction = "generate a response to user questions"
    return Command(goto="generator", update={"instruction": instruction})


def generate(state: PlannerState, config: dict) -> PlannerState:
    """Generate a response to user input

    :param state: The state of the agent.
    :return: The state of the agent with the added response
    """
    instruction = state.get("instruction", "")
    user_message = state["messages"][-1]  # last message is the user input
    tasks = state.get("tasks", "")
    summary = state.get("tasks", "")
    improvements = state.get("improvements", "")

    model_name = config.get("configurable", {}).get("model_name", "openai")
    model = _get_model(model_name)

    response = model.invoke(
        [
            {
                "role": "system",
                "content": GENERATOR_PROMPT.format(
                    user_message=user_message,
                    instruction=instruction,
                    tasks=tasks,
                    summary=summary,
                    improvements=improvements,
                ),
            }
        ]
    )
    logger.info(f"[generate node] response is {response}")
    return {"messages": [response]}


def suggest(state: PlannerState, config: dict) -> PlannerState:
    """This function is used to retrieve relevant scenarios from repo and suggest points of
     improvement on the tasks.

    :param state: The state of the agent.
    :param config: The configuration of the agent.
    :return: The tasks extracted from the text.
    """
    tasks = state["tasks"]
    summary = state["summary"]

    model_name = config.get("configurable", {}).get("model_name", "openai")
    model = _get_model(model_name)

    retrieval_results = [retriever_tool(task) for task in tasks]

    messages = [
        SystemMessage(
            content=SUGGESTOR_PROMPT.format(
                retrieval_results=retrieval_results,
                tasks=tasks,
                summary=summary,
            )
        )
    ]
    improvements = model.with_structured_output(SuggestorOutput).invoke(
        messages
    )

    logger.info("[suggest] improvements {improvements}")

    return {"improvements": improvements}
