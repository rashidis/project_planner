import asyncio
from loguru import logger

from langgraph_sdk import get_client
from langchain_core.messages import HumanMessage


async def main():
    """Main function to run the client"""
    # only pass the url argument to get_client() if you changed the default port when calling langgraph up
    client = get_client(url="http://localhost:8123")

    # Using the graph deployed with the name "agent"
    assistant_id = "planner"
    new_thread = await client.threads.create(metadata={"user_id": "123"})
    logger.info("Thread created:", new_thread)

    chat_log = """Marketing Project Chat Log
            Project: Customer Success Stories Website Section
            [January 12, 2025]
            [9:23 AM] Client 1 [Marketing Director]: Need to start on customer success stories section. Looking for 5-6 stories.
            [10:47 AM] Content Specialist: I'll identify key customers - have strong stories from Apex Manufacturing and Healthcare.
            [2:34 PM] Copy Specialist: When's our target launch date?
            [3:15 PM] Content Specialist: Leadership wants this live by end of February."""

    # Define the input for the assistant
    input_data = {"messages": HumanMessage(content=""), "chat_log": chat_log}

    # Stream the assistant's responses
    async for chunk in client.runs.stream(
        new_thread["thread_id"],
        assistant_id,
        input=input_data,
        stream_mode="updates",
    ):
        logger.info(f"Receiving new event of type: {chunk.event}...")
        logger.info(chunk.data)
        logger.info("\n\n")


if __name__ == "__main__":
    # Run the async function
    asyncio.run(main())
