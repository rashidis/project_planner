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
            [9:23 AM] Client 1 [Marketing Director]: Wanted to get started on the customer success stories section. Our core focus is showing the real-world impact of our security solutions. Initial thoughts are featuring 5-6 stories, with a mix of industries and use cases.
            [10:47 AM] Content Specialist: I can start identifying key customers. Already have a few in mind from recent wins - particularly strong stories from Apex Manufacturing and Memorial Healthcare.
            [11:15 AM] Client 2 [Marketing Manager]: Love those two. Apex's 75% reduction in security incidents would make a great headline. Can we also look at some finance sector customers? Sales is pushing hard for more enterprise stories.
            [2:34 PM] Copy Specialist: Looking at my upcoming schedule. When are we aiming to launch this?
            [3:15 PM] Content Specialist: Leadership wants this live by end of February. Need to schedule interviews - would next week work for you?
            [4:45 PM] Design Specialist: Just reviewed some competitor case studies. Their story formats are pretty standard. Think we could stand out with a more dynamic approach to presenting the metrics and results.
            [January 13, 2025]
            [8:47 AM] Webflow Specialist: Could do some interesting things with scrolling animations and progressive reveal. Need to be careful about performance though. @Design Specialist - what's your vision here?
            [9:32 AM] Client 1 [Marketing Director]: Before we get too deep into design - let's make sure we have the right customers lined up. @Content Specialist can you share the full list of potential stories?
            [10:15 AM] Content Specialist: Here's what I'm thinking:
            """
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
