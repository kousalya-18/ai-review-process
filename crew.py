import os


from crewai import LLM
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import (
	URLReadTool
)






@CrewBase
class InternshipManagementSystemPhase1ScreeningCrew:
    """InternshipManagementSystemPhase1Screening crew"""

    
    @agent
    def intern_screening_agent(self) -> Agent:
        
        
        return Agent(
            config=self.agents_config["intern_screening_agent"],
            
            
            tools=[				URLReadTool()],
            
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-5.6-luna",
                
                
            ),
            
        )
        
    

    
    @task
    def read_intern_record_from_google_sheet(self) -> Task:
        return Task(
            config=self.tasks_config["read_intern_record_from_google_sheet"],
            markdown=False,
            
            
        )
    
    @task
    def screen_intern_and_produce_evaluation_report(self) -> Task:
        return Task(
            config=self.tasks_config["screen_intern_and_produce_evaluation_report"],
            markdown=False,
            
            
        )
    

    @crew
    def crew(self) -> Crew:
        """Creates the InternshipManagementSystemPhase1Screening crew"""

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,

            chat_llm=LLM(model="openai/gpt-5.6-luna"),
        )


