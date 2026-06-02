"""
Tool definitions for the AI Business Analyst System
"""
from crewai_tools import tool
import requests
import json


def create_research_tools():
    """
    Create research and information gathering tools
    
    Returns:
        list: List of tool functions
    """
    
    @tool
    def search_industry_standards(industry: str, topic: str) -> str:
        """
        Search for industry standards and best practices
        
        Args:
            industry: The industry to search for
            topic: The specific topic or standard
            
        Returns:
            str: Information about industry standards
        """
        return f"Industry standards for {industry} regarding {topic}: [Standards information would come from external APIs]"
    
    @tool
    def research_technologies(tech_stack: str) -> str:
        """
        Research specific technologies and their capabilities
        
        Args:
            tech_stack: Technologies to research
            
        Returns:
            str: Information about the technologies
        """
        return f"Research findings for {tech_stack}: [Technology information would come from external APIs]"
    
    @tool
    def check_compliance_requirements(industry: str, region: str) -> str:
        """
        Check compliance and regulatory requirements
        
        Args:
            industry: The industry
            region: Geographic region
            
        Returns:
            str: Compliance requirements
        """
        return f"Compliance requirements for {industry} in {region}: [Compliance data would come from regulatory databases]"
    
    return [search_industry_standards, research_technologies, check_compliance_requirements]


def create_analysis_tools():
    """
    Create analysis and calculation tools
    
    Returns:
        list: List of tool functions
    """
    
    @tool
    def calculate_roi(investment: float, annual_benefit: float, years: int) -> str:
        """
        Calculate Return on Investment
        
        Args:
            investment: Initial investment amount
            annual_benefit: Annual benefit amount
            years: Number of years
            
        Returns:
            str: ROI calculation results
        """
        roi = ((annual_benefit * years - investment) / investment) * 100
        payback_period = investment / annual_benefit if annual_benefit > 0 else float('inf')
        
        return f"""ROI Analysis:
        - Investment: ${investment:,.2f}
        - Annual Benefit: ${annual_benefit:,.2f}
        - ROI ({years} years): {roi:.2f}%
        - Payback Period: {payback_period:.2f} years
        """
    
    @tool
    def estimate_timeline(task_count: int, complexity: str) -> str:
        """
        Estimate project timeline based on tasks and complexity
        
        Args:
            task_count: Number of tasks
            complexity: Complexity level (low, medium, high)
            
        Returns:
            str: Timeline estimation
        """
        complexity_multipliers = {
            'low': 1.0,
            'medium': 1.5,
            'high': 2.0
        }
        
        multiplier = complexity_multipliers.get(complexity.lower(), 1.5)
        weeks_per_task = 1 * multiplier
        total_weeks = task_count * weeks_per_task
        total_months = total_weeks / 4
        
        return f"""Timeline Estimation:
        - Task Count: {task_count}
        - Complexity: {complexity}
        - Estimated Duration: {total_weeks:.0f} weeks (~{total_months:.1f} months)
        """
    
    @tool
    def assess_resource_requirements(project_scope: str, team_size: int) -> str:
        """
        Assess resource requirements for the project
        
        Args:
            project_scope: Scope of the project
            team_size: Proposed team size
            
        Returns:
            str: Resource requirements assessment
        """
        return f"""Resource Assessment:
        - Project Scope: {project_scope}
        - Proposed Team Size: {team_size} people
        - Estimated Budget: [Calculated based on team size and duration]
        - Required Skills: [Analysis, Development, Testing, Project Management]
        """
    
    return [calculate_roi, estimate_timeline, assess_resource_requirements]


def create_all_tools():
    """
    Create and return all tools
    
    Returns:
        tuple: (research_tools, analysis_tools)
    """
    return create_research_tools(), create_analysis_tools()
