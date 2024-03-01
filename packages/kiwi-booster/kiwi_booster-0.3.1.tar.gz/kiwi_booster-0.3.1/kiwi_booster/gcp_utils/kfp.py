"""
Utility functions for working with Kubeflow Pipelines
"""


def get_requirements(req_path: str) -> list:
    """
    Get a list of requirements from requirements.txt

    Returns:
        requirements (list): List of requirements
    """
    # Get the requirements file and read it line by line, save this into a list
    with open(req_path, "r") as file:
        content = file.read()

    lines = content.splitlines()
    requirements = [line for line in lines if line and not line.startswith("#")]

    return requirements
