from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

from dotenv import load_dotenv
import os

from crewai_tools import SerperDevTool, ScrapeWebsiteTool

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

llm = LLM(model=os.getenv("MODEL"),
          api_key=groq_api_key,  )

search_tool = SerperDevTool()

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class Project1():
    """Project1 crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def goal_analyzer(self) -> Agent:
        return Agent(
            config=self.agents_config['goal_analyzer'], # type: ignore[index]
            llm=llm,
            max_iter=3,
            max_rpm=15
        )

    @agent
    def curriculum_planner(self) -> Agent:
        return Agent(
            config=self.agents_config['curriculum_planner'], # type: ignore[index]
            llm=llm,
            max_iter=5,
            max_rpm=15
        )
    
    @agent
    def resource_suggester(self) -> Agent:
        return Agent(
            config=self.agents_config['resource_suggester'], # type: ignore[index]
            llm=llm,
            tools=[search_tool], 
            max_iter=7,
            max_rpm=15
        )
    
    @agent
    def practice_problem_generator(self) -> Agent: 
        return Agent(
            config=self.agents_config['practice_problem_generator'],
            llm=llm,
            max_iter=5,
            max_rpm=15
        )

    @agent
    def learning_plan_consolidator(self) -> Agent: 
        return Agent(
            config=self.agents_config['learning_plan_consolidator'],
            llm=llm,
            max_iter=3,
            max_rpm=15
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def goal_analysis(self) -> Task:
        return Task(
            config=self.tasks_config['goal_analysis'], # type: ignore[index]
        )

    @task
    def curriculum_planning(self) -> Task:
        return Task(
            config=self.tasks_config['curriculum_planning'], # type: ignore[index]
            output_file='report.md'
        )
    
    @task
    def resource_suggestion(self) -> Task:
        return Task(
            config=self.tasks_config['resource_suggestion'], # type: ignore[index]
        )

    @task
    def problem_generation(self) -> Task: # New task method, name matches tasks.yaml key
        return Task(
            config=self.tasks_config['problem_generation'],
        )

    @task
    def final_plan_assembly(self) -> Task: # New task method, name matches tasks.yaml key
        return Task(
            config=self.tasks_config['final_plan_assembly'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Project1 crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            llm=llm,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
