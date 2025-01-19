from langchain.prompts import ChatPromptTemplate

TASK_EXTRACTION_PROMPT = ChatPromptTemplate.from_template(
    """
You are an AI assistant designed to break down marketing and team conversations
and extract agreed-upon tasks based on the following chat log.

Your output must:
1. List only tasks that were agreed upon or assigned during the conversation.
2. Exclude any tasks that were declined or dismissed.
3. Clearly group tasks by their assignee, if specified.
4. Include timelines, deadlines, or any specific details mentioned for each task.

Chat Log:
{chat_log}

Please analyze the conversation and extract tasks in the following JSON structure:
*tasks
with each task having the structure as:

**"description": "Task description",
**"deadline": "Task deadline",
** "assignee": "Task assignee",
** "other_details": "Other task-specific details"


Ensure each task has all required fields filled out, using "Not specified" if information is missing.
"""
)
