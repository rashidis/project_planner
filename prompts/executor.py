from langchain.prompts import ChatPromptTemplate


TASK_EXTRACTION_PROMPT = ChatPromptTemplate.from_template(
    """
You are an AI assistant designed to break down marketing and team conversations
and extract agreed-upon tasks based on the following chat log.

Your output must:
1. List only tasks that were agreed upon, assigned during the conversation or is ongoing.
2. Exclude any tasks that were declined or dismissed.
3. Clearly group tasks by their assignee, if specified.
4. Include status, timelines, deadlines, or any specific details mentioned for each task.
5. For `task_updates`, only provide an update for tasks with a status of `in_progress`. Use "Not applicable" or "Not specified" for other fields when information is missing.


Chat Log:
{chat_log}

Please analyse the conversation and extract any future, current or ongoing tasks in the following JSON structure:
{{
    "tasks": [
        {{
            "description": "Task description",
            "status": "backlog | ready_to_work | in_progress",
            "deadline": "Task deadline or 'Not specified'",
            "assignee": "Task assignee or 'Not specified'",
            "task_updates": "Task update if the task is ongoing, or 'Not specified'",
            "other_details": "Other task-specific details or 'Not specified'"
        }}
    ]
}}

Ensure each task has all required fields filled out, using "Not specified" if information is missing.
"""
)


SUMMARISER_PROMPT = ChatPromptTemplate.from_template(
    """
You are an AI assistant specialised in summarising meeting discussions.
Given a transcript of a meeting as chat log, your task is to:

Chat Log:
{chat_log}

Summarise the key points discussed: Provide a concise overview of the main topics covered.
Identify and list clear next steps: Highlight actionable items, including responsibilities,
deadlines (if mentioned), and other relevant details.
"""
)
