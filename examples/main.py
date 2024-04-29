import sys
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()
crewai_path = os.getenv("LOCAL_CREWAI_PATH")
sys.path.append(crewai_path)
from crewai import Agent, Task, Crew, Process

llm = ChatOpenAI(model="gpt-3.5-turbo")

# Create a researcher agent
researcher = Agent(
    role="Senior Researcher",
    goal="Discover groundbreaking technologies",
    verbose=True,
    llm=llm,
    backstory="A curious mind fascinated by cutting-edge innovation and the potential to change the world, you know everything about tech.",
)

# Task for the researcher
research_task = Task(
    description="Identify the next big trend in AI",
    expected_output="A detailed report on the next big trend in AI",
    agent=researcher,  # Assigning the task to the researcher
)

# Instantiate your crew
tech_crew = Crew(
    agents=[researcher],
    tasks=[research_task],
    process=Process.sequential,  # Tasks will be executed one after the other
)

# Begin the task execution
tech_crew.kickoff()
