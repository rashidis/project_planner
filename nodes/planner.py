from loguru import logger
from typing import TypedDict, Literal
from langgraph.types import Command
from langchain_core.messages import SystemMessage

from states import PlannerState
from prompts import GENERATOR_PROMPT, SUGGESTOR_PROMPT, INTENT_DETECTION_PROMPT
from .utils import _get_model, retriever_tool


class Improvement(TypedDict):
    details: str
    actions: str


class SuggestorOutput(TypedDict):
    improvements: list[Improvement]


class IntentDetectionOutput(TypedDict):
    intent: Literal["generic", "followup"]


def plan(state: PlannerState, config: dict) -> Command:
    """This function is used tosummarise the meeting highlights from the text.

    :param state: The state of the agent.
    :param config: The configuration of the agent.
    :return: The tasks extracted from the text.
    """
    logger.info(f"[plan node] state {state}")
    if state.get("chat_log", []):
        logger.info(
            f"[plan node] chat_log detected, calling executor_graph to process the log"
        )
        return Command(goto="executor_graph")

    logger.info(
        f"[plan node] chat_log not detected, calling generator to generate a response"
    )
    instruction = "Output a response to user question."
    return Command(goto="generator", update={"instruction": instruction})


def intent_dection(model, user_message: str) -> str:
    """A small agent to do an intent_detection between geenric and followup questions

    :param model: the llm model as the agent
    :param user_message: the user query to be classified
    :return: the user intent"""
    intent = model.with_structured_output(IntentDetectionOutput).invoke(
        INTENT_DETECTION_PROMPT.format(query=user_message)
    )["intent"]
    logger.info(f"intent is {intent}")
    return str(intent).lower()


def generate(state: PlannerState, config: dict) -> PlannerState:
    """Generate a response to user input

    :param state: The state of the agent.
    :return: The state of the agent with the added response
    """
    user_message = state["messages"][-1]  # last message is the user input
    instruction = state.get("instruction", "")
    tasks = state.get("tasks", "")
    summary = state.get("tasks", "")
    improvements = state.get("improvements", "")
    logger.info(f"[tasksk]{tasks}")
    model_name = config.get("configurable", {}).get("model_name", "openai")
    model = _get_model(model_name)

    intent = intent_dection(model, user_message)

    if intent == "followup" or not tasks:
        logger.info(
            "[generate node] the user query intent in followup, outputting a followup response"
        )
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
    elif intent == "generic" or tasks:
        logger.info(
            "[generate node] the user query intent in generic, outputting a generic response"
        )
        logger.info(
            f"[generate node] {instruction + ' : ' + user_message.content}"
        )
        response = model.invoke(
            [{"role": "system", "content": instruction + user_message.content}]
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
