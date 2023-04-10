import os
from pathlib import Path
import logging

while True:
    project_name = input("Enter your project name: ")
    if project_name != "":
        break

logging.info(f"Creating project by name: {project_name}")

list_of_files = [
    ".github/workflows/.gitkeep",
    ".github/workflows/main.yaml",
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/config/__init__.py",
    f"{project_name}/constant/__init__.py",
    f"{project_name}/entity/__init__.py",
    # f"{project_name}/exception/__init__.py",
    # f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/utils/__init__.py",
    "config/config.yaml",
    "schema.yaml",
    "requirements.txt",
    # "setup.py",
    "main.py",
    "README.md"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    # print("filepath:", filepath)
    # print("filedir:", filedir)
    # print("filename:", filename)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating a new directory at : {filedir} for file: {filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        print("path:", os.path.exists(filepath))
        print("size:", os.path.getsize(filepath))
        print("if condition:", filepath)

        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating a new file: {filename} for path: {filepath}")
        print("file_created:", filepath)
        print()
    else:
        print("path:", os.path.exists(filepath))
        print("size:", os.path.getsize(filepath))
        print("else condition:", filepath)
        logging.info(f"file is already present at: {filepath}")
        print()



