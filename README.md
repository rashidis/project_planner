# AI Project Planner

## Overview
The project is an intelligent AI-powered assistant designed to revolutionise marketing operations by automating administrative tasks and enhancing team efficiency. This project showcases a lightweight proof of concept (POC) to demonstrate Pip’s capabilities.

---

## Project Context
This project was developed as part of an interview process to envision and prototype an AI partner for marketing operations. The goal is to illustrate AI's ability to streamline workflows by using multi-agentic systems.

---

## Success Metrics
### Seamless Platform Integration
- Video calls automatically generate transcripts and action items.
- Messages flow directly into project plans.
- Real-time collaboration feeds into Pip’s learning to refine future interactions.

### Intelligent Automation
- Conversations are transformed into structured task lists.
- Chat messages become project updates.
- Meeting discussions yield clear summaries and next steps.
- Platform activity informs project recommendations automatically.

### Enhanced Team Efficiency
- Notes are synced to project plans automatically.
- Updates happen in real-time and are centralised in one location.
- Action items are tracked without manual intervention.
- All platform activity is converted into actionable data.

---

## Challenge: Build a POC
The POC demonstrates an end-to-end flow for Pip’s functionality. It includes:
1. **Input:** A marketing team’s video call transcript or chat conversation.
2. **Processing:** Intelligent parsing and structuring of the information.
3. **Output:** Work products such as tasks, updates, and summaries.
4. **Interface:** A clear and intuitive way for teams to interact with these outputs.

---

## How to Run
### Prerequisites
- Python 3.8+
- Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```
- (Optional) Set up API keys for any external transcription or messaging services used.

### Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```
2. Run the POC script:
   ```bash
   python main.py
   ```
3. Provide an example input (e.g., a transcript or chat log) and observe the output.

### Example Input
**Chat Log:**
```
[9:23 AM] Client 1: Let’s start on the customer success stories section with 5-6 examples across industries.
[10:15 AM] Content Specialist: Scheduling interviews next week.
```

### Example Output
**Tasks Generated:**
- Identify 5-6 customer stories spanning industries.
- Schedule interviews for customer success stories next week.

---

## Roadmap
- **Short-Term:** Refine Pip’s ability to process and structure diverse input formats.
- **Mid-Term:** Integrate Pip with marketing platforms for seamless automation.
- **Long-Term:** Leverage machine learning to enable real-time collaboration and proactive recommendations.

---

## Acknowledgements
This project was created as part of an interview and is a demonstration of the potential for AI-driven marketing operations assistance.
