from setuptools import setup, find_packages
from typing import List

Hypen_e_dot = "-e ."

def get_requirement(file_path:str)-> List[str]:
    requirements=[]
    with open(file_path, 'r') as f:
        requirements=f.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if Hypen_e_dot in requirements:
            requirements.remove(Hypen_e_dot)

setup(
name="ML_project",
version="0.0.1",
author="aaditya",
packages=find_packages(),
install_requires=get_requirement('requirement.txt')
)