# standard template files for a Python project's folder structure . 

import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "Text_summarisation"

files = [
    ".github/workflows/.gitkeep",
    "src/__init__.py",

    # src folder 
    "src/components/__init__.py",
    "src/components/model_trainer.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",

    "src/pipeline/predict_pipeline.py",
    "src/pipeline/train_pipeline.py",

    "src/exceptions.py",
    "src/logger.py",
    "src/utils.py",

    #artifacts folder for saving trained models, logs etc. 
    "artifacts/temp.txt",

    # Notebooks for experimenting and testing    
    "notebook/trials.ipynb",
    "notebook/data/data.csv",

    "app.py",
    "main.py",
    "requirement.txt",
    "setup.py",

]
    # f"src/{project_name}/utils/__init__.py",
    # f"src/{project_name}/utils/common.py",
    # f"src/{project_name}/logging/__init__.py",
    # f"src/{project_name}/config/__init__.py",
    # f"src/{project_name}/config/configuration.py",
    # f"src/{project_name}/entity/__init__.py",
    # f"src/{project_name}/constants/__init__.py",
    # "Dockerfile",


for filepath in files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")


    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} is already exists")
