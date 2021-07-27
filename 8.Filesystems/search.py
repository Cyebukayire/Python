from pathlib import Path

path = Path() #Takes current directory

#print all directories & files in the path directory
for file in path.glob("*"): 
    print(file)
    
#print all files in the path directory
for file in path.glob("*.*"): 
    print(file)

#print all py files in the path directory
for file in path.glob("*.py"): 
    print(file)