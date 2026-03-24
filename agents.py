from crewai import Agent, LLM
from crewai_tools import TavilySearchTool
from dotenv import load_dotenv
import os

load_dotenv()

# Setup the LLM — Groq is FREE and very fast
llm = LLM(
    model="llama-3.1-8b-instant",       # Best free model on Groq
    api_key=os.getenv("GROQ_API_KEY"),
    base_url = "https://api.groq.com/openai/v1",
    temperature=0.3,
    max_tokens = 1024
)

# Web search tool for researcher
search_tool = TavilySearchTool()
    #api_key=os.getenv("TAVILY_API_KEY"),
    #max_results=5


# ── AGENT 1: Researcher ──────────────────────────
researcher = Agent(
    role="Senior Research Analyst",
    goal="Find accurate, up-to-date information on {topic} from reliable sources",
    backstory="""You are an expert research analyst with 10 years of experience.
    You excel at finding credible sources, identifying key trends, 
    and extracting the most relevant information.""",
    tools=[search_tool],
    llm=llm,
    verbose=True,
    allow_delegation=False
)

# ── AGENT 2: Writer ──────────────────────────────
writer = Agent(
    role="Expert Content Writer",
    goal="Transform research findings into a clear, engaging report on {topic}",
    backstory="""You are a skilled content writer who specializes in making 
    complex topics accessible. You structure information logically and 
    write in a professional yet engaging style.""",
    llm=llm,
    verbose=True,
    allow_delegation=False
)

# ── AGENT 3: Editor ──────────────────────────────
editor = Agent(
    role="Senior Editor",
    goal="Polish and improve the report for clarity, flow, and professionalism",
    backstory="""You are a meticulous editor with an eye for detail.
    You improve sentence structure, eliminate redundancy, ensure 
    consistent tone, and make content more impactful.""",
    llm=llm,
    verbose=True,
    allow_delegation=False
)

# ── AGENT 4: Fact-Checker ────────────────────────
fact_checker = Agent(
    role="Fact-Checking Specialist",
    goal="Verify all claims in the report and flag any inaccuracies or unsupported statements",
    backstory="""You are a rigorous fact-checker who cross-references claims
    against known data. You add confidence ratings to key claims and 
    note when sources are needed.""",
    tools=[search_tool],
    llm=llm,
    verbose=True,
    allow_delegation=False
)
