from crewai import Crew, Process
from agents import researcher, writer, editor, fact_checker
from tasks import research_task, writing_task, editing_task, fact_check_task
import os
from datetime import datetime

def run_research_crew(topic: str):
    """Run the full multi-agent pipeline for a given topic."""
    
    crew = Crew(
        agents=[researcher, writer, editor, fact_checker],
        tasks=[research_task, writing_task, editing_task, fact_check_task],
        process=Process.sequential,  # Runs in order
        verbose=True,                   # Show detailed logs
        memory=False,                  # Agents remember context
        max_rpm = 3
    )
    
    # Kick off with the topic
    result = crew.kickoff(inputs={"topic": topic})
    
    # Save output to file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    filename = f"outputs/report_{timestamp}.md"
    os.makedirs("outputs", exist_ok=True)
    
    with open(filename, "w", encoding = "utf-8") as f:
        f.write(f"# Research Report: {topic}\n\n")
        f.write(f"Generated: {datetime.now().strftime('%B %d, %Y')}\n\n")
        f.write(str(result))
    
    return str(result), filename

# Test it from command line
if __name__ == "__main__":
    topic = "AI trends in Indian fintech 2026"
    result, path = run_research_crew(topic)
    print(f"\n✅ Report saved to: {path}")
