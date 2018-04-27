# Author: Txanton Bejos
import os

for file in os.listdir(os.getcwd()):
    if file.find("_") >= 0:
        newName = file.replace("_", " ")
        os.rename(file, newName)
    elif file.find(".") > 0:
        newName = file.replace(".", " ", file.count(".") - 1)
        os.rename(file, newName)

