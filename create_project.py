from pathlib import Path

#Current working directory
root= Path(".")

#FOlder to create

folders= [
    "app/api",
    "app/core",
    "app/rag",
    "app/services",
    "data",
    "templates",
    "static",
    "tests",
    "uploads",
]

files= [
    "app/main.py",
    "ingest_samples.py",
    "run.py",
    ".env",
]

#Create folder
for folder in folders:
    folder_path= root / folder
    folder_path.mkdir(parents=True, exist_ok=True)

#Create files
for file in files:
    file_path= root / file
    file_path.touch(exist_ok=True)

print("Project structure created successfully.")