from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """
    Reads a requirements file and returns a list of dependencies.
    """
    with open(file_path) as file_obj:
        requirements = [req.strip() for req in file_obj.readlines() if req.strip()]
        requirements = [req for req in requirements if req != "-e ."]
    return requirements

setup(
    name="mlProject",
    version="0.0.1",
    author="Nikhil",
    author_email="k06@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
