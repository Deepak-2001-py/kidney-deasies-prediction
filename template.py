import os 
from pathlib import Path
import logging

#logging strigs
logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')
project_name="ccnClassifier"

list_of_files=["github/workflows/.giteep",
               f"src/{project_name}/__init__.py",
               f"src/{project_name}/components/__init__.py",
               f"src/{project_name}/utils/__init__.py",
               f"src/{project_name}/config/__init__.py",
               f"src/{project_name}/config/configuration.py",
               f"src/{project_name}/pipeline/__init__.py",
               f"src/{project_name}/entity/__init__.py",
               f"src/{project_name}/constants/__init__.py",
               "config/sonfig.yaml",
               "dvc.yaml",
               "params.yaml",
               "requirements.txt",
               "research/trials.ipynb",
               "tempalates/index.html"
               ]


for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath) 
    
    
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directory:{filedir} for file {filename}")
    
    if (not os.path.exists(filepath))or (os.path.getsize(filepath)==0):
        with open(filepath,"w")as f:
            pass 
        logging.info(f"creating empty file file: {filepath}")
        
    else:
        logging.info(f"{filename} is already exists")
            
        