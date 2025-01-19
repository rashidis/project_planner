from typing import Literal, TypedDict


class GraphConfig(TypedDict):
    """Configuration type for the graph workflow.

    This TypedDict defines the configuration schema for the workflow graph,
    specifying which language model to use for the agent.
    """

    model_name: Literal["openai", "anthropic"]
