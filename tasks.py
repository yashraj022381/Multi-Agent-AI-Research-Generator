from crewai import Task
from agents import researcher, writer, editor, fact_checker

# Task 1 — Research
research_task = Task(
   description="""Research the topic: {topic}
    
    Find: latest developments, key statistics, 
    major players, challenges, and future outlook.
    Use 3 sources maximum. Be concise.
    """,
    expected_output="""A brief research summary with:
    - 5-8 key findings
    - Key statistics
    - Major players
    - Sources used""",
    agent=researcher
)

# Task 2 — Write (uses research as context)
writing_task = Task(
   description="""Write a professional report on: {topic}
    
    Use these sections:
    1. Executive Summary
    2. Current Landscape  
    3. Key Trends
    4. Challenges
    5. Conclusion
    
    Keep it under 600 words total.
    """,
    expected_output="A structured Markdown report under 600 words.",
    agent=writer,
    context=[research_task]
)

# Task 3 — Edit
editing_task = Task(
    description="""Polish this report on {topic} for clarity 
    and flow. Fix grammar. Return the full improved report.""",
    expected_output="The improved report in Markdown format.",
    agent=editor,
    context=[writing_task]
)

# Task 4 — Fact Check
fact_check_task = Task(
   description="""Fact-check the report on {topic}. 
    Mark key claims as VERIFIED or UNVERIFIED.
    Return final report with a brief Fact-Check Summary.""",
    expected_output="Final report with Fact-Check Summary appended.",
    agent=fact_checker,
    context=[editing_task]
)
