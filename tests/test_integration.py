from langchain_core.messages import HumanMessage
from agents import planner_graph, executor_graph

# Sample test data
SAMPLE_CHAT_LOG = """Marketing Project Chat Log
Project: Customer Success Stories Website Section
[January 12, 2025]
[9:23 AM] Client 1 [Marketing Director]: Need to start on customer success stories section. Looking for 5-6 stories.
[10:47 AM] Content Specialist: I'll identify key customers - have strong stories from Apex Manufacturing and Healthcare.
[2:34 PM] Copy Specialist: When's our target launch date?
[3:15 PM] Content Specialist: Leadership wants this live by end of February."""


def test_planner_graph_generic_query():
    """Test planner graph with generic question"""
    input_state = {
        "messages": [HumanMessage(content="What is a project plan?")]
    }

    result = planner_graph.invoke(input_state)

    assert "messages" in result
    assert len(result["messages"]) > 0


def test_executor_graph():
    """Test executor graph for task extraction and summarization"""
    input_state = {"chat_log": SAMPLE_CHAT_LOG}

    result = executor_graph.invoke(input_state)

    assert "tasks" in result
    assert "summary" in result
    tasks = result["tasks"]
    assert len(tasks["tasks"]) > 0


def test_intent_detection():
    """Test the intent detection functionality"""
    from nodes.planner import intent_dection
    from nodes.utils import _get_model

    model = _get_model("openai")

    # Test generic question
    generic_intent = intent_dection(model, "where is my dog")
    assert generic_intent == "generic"

    # Test followup question
    followup_intent = intent_dection(
        model, "what tasks are included in the plan?"
    )
    assert followup_intent == "followup"


def test_suggestion_generation():
    """Test suggestion generation with sample tasks"""
    from nodes.planner import suggest

    sample_state = {
        "tasks": {
            "tasks": [
                {
                    "description": "Identify key customers for success stories",
                    "status": "in_progress",
                    "deadline": "End of February",
                    "assignee": "Content Specialist",
                }
            ]
        },
        "summary": "Team planning customer success stories section with 5-6 stories needed",
    }

    result = suggest(sample_state, {"configurable": {"model_name": "openai"}})

    assert "improvements" in result
    assert isinstance(result["improvements"], dict)
    assert "improvements" in result["improvements"]
    assert len(result["improvements"]["improvements"]) > 0
