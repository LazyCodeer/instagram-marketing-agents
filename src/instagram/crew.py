import sys
import os

# sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
# from instagram_agent.tools.search import SearchTools
from instagram.tools.search import SearchTools

# Uncomment the following line to use an example of a custom tool
# from instagram.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

@CrewBase
class InstagramCrew():
    """Instagram crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'


    @agent
    def market_researcher(self) -> Agent:
        return Agent(
			config=self.agents_config['market_researcher'],
			tools=[
				SearchTools.search_internet,
				SearchTools.search_instagram,
				SearchTools.open_page,
       		],
			verbose=True
		)

    @agent
    def content_strategist(self) -> Agent:
        return Agent(
			config=self.agents_config['content_strategist'],
			tools=[],
			verbose=True
		)

    @agent
    def visual_creator(self) -> Agent:
        return Agent(
			config=self.agents_config['visual_creator'],
			tools=[],
			verbose=True
		)

    @agent
    def copywriter(self) -> Agent:
        return Agent(
			config=self.agents_config['copywriter'],
			tools=[],
			verbose=True
		)

    @task
    def market_research(self) -> Task:
        return Task(
			config=self.tasks_config['market_research'],
			agent=self.market_researcher,
			output_file='output/market_research.md',
		)

    @task
    def content_strategy(self) -> Task:
        return Task(
			config=self.tasks_config['content_strategy'],
			agent=self.content_strategist,
		)

    @task
    def visual_content_creation(self) -> Task:
        return Task(
			config=self.tasks_config['visual_content_creation'],
			agent=self.visual_creator,
		)

    @task
    def copywriting(self) -> Task:
        return Task(
			config=self.tasks_config['copywriting'],
			agent=self.copywriter,	
		)

    @task
    def report_final_content_strategy(self) -> Task:
        return Task(
			config=self.tasks_config['report_final_content_strategy'],
			agent=self.researcher,
			output_file='output/final_content_strategy.md',
		)

    @crew
    def crew(self) -> Crew:
        """Creates the Instagram crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
