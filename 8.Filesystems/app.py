from pathlib import Path
"""
#Absolute path: path from the root directory
ex: c:\Program files\Windows

#Relative path: A path starting from the current directory
"""

path = Path("ecommerce")
print(path.exists)
if not path.exists:
    path.mkdir #Create the Directory
else:
    print("Directory Already Exists")
    path.rmdir #delete the fiDirectoryle
    print("Directory deleted")





