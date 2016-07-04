import os


for file in os.listdir(os.getcwd()):
    if file.find("_") >= 0:
        newName = file.replace("_", " ")
        os.rename(file, newName)
