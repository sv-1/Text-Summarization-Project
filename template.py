## Inside template we'll write all the logic to create files.
import os 
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO, format='[%asctime)s]:%(message)s:')

project_name="textSummarizer"

list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging//__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml"
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    

]

## Above are the files of that we'll be creating, now below is the logic, how these files will be created

for filepath in list_of_files:
    filepath = Path(filepath) # this loop will iteratievely see the above files  

    filedir, filename=os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file{filename}")
        
    if(not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
       with open(filepath,'w') as f:
        pass
       logging.info(f"Creating empty file: {filepath}")