from pathlib import Path

path = Path() #Takes current directory

#print all current files in the path directory

for file in path.glob("*"):
    print(file)
