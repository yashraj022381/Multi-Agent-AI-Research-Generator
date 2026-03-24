from crewai import Task
from agents import researcher, writer, editor, fact_checker

# Task 1 — Research
research_task = Task(
    description="""
    Research the topic: {topic}
    
    Find: latest develoments, key statistics,
    major players, challenges and future outlook.
    Use 3 sources maximum. Be concise.
    """,
    expected_output="""A comprehensive research brief with:
    - 5 - 8 Key findings (10-15 bullet points)
    - Key statistics 
    - Majors players/trends
    - Sources used""",
    agent=researcher
)

# Task 2 — Write (uses research as context)
writing_task = Task(
    description="""
    Write a full professional report on: {topic}
    
    Use these sections:
    1. Executive Summary (200 words)
    2. Introduction and Background
    3. Current Landscape (3-4 sections)
    4. Key Trends and Drivers
    5. Challenges and Risks
    6. Opportunities and Future Outlook
    7. Conclusion
    
    
    Keep it under 600 words total.
    """,
    expected_output="""A well-structured Markdown report with proper headers,
    approximately 600 words, professional tone.""",
    agent=writer,
    context=[research_task]   # Gets researcher's output
)

# Task 3 — Edit
editing_task = Task(
    description="""
    Review and improve the written report. Focus on:
    - Clarity: Is every sentence easy to understand?
    - Conciseness: Remove any repetition or filler words
    - Impact: Strengthen weak sentences
    - Formatting: Ensure consistent Markdown formatting
    
    Return the FULL improved report, not just comments.
    """,
    expected_output="""The complete edited report in Markdown format,
    improved for clarity, flow, and professional polish.""",
    agent=editor,
    context=[writing_task]
)

# Task 4 — Fact Check
fact_check_task = Task(
    description="""
    Review the edited report for factual accuracy. For each major claim:
    1. Mark as ✅ VERIFIED, ⚠️ UNVERIFIED, or ❌ INCORRECT
    2. Add a brief note when verification fails
    3. Suggest corrections for any inaccurate claims

    Return final report with a brief  Fact-Check Summary.
    """,
    expected_output="""The final polished report with fact-check notes
    integrated and a Fact-Check Summary section appended.""",
    agent=fact_checker,
    context=[editing_task]
)
