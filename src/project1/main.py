#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from project1.crew import Project1

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'learning_goal': "I want to learn advanced data analysis techniques using Python, specifically for financial modeling.",
        'current_level': "I have a good understanding of basic Python syntax and some experience with Pandas, but I'm new to advanced statistical libraries and financial-specific applications."
    }
    
    try:
        Project1().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'learning_goal': "I want to learn advanced data analysis techniques using Python, specifically for financial modeling.",
        'current_level': "I have a good understanding of basic Python syntax and some experience with Pandas, but I'm new to advanced statistical libraries and financial-specific applications."
    }
    try:
        Project1().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Project1().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'learning_goal': "I want to learn advanced data analysis techniques using Python, specifically for financial modeling.",
        'current_level': "I have a good understanding of basic Python syntax and some experience with Pandas, but I'm new to advanced statistical libraries and financial-specific applications."
    }
    
    try:
        Project1().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
