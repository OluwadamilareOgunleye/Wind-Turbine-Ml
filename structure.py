import os

folders = [
    "data",
    "cad",
    "src",
    "notebooks"
]

files = [
    "app.py",
    "README.md"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

for file in files:
    with open(file, "w") as f:
        pass

print("Wind Turbine ML project structure created successfully!")