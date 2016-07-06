# Author: Txanton Bejos
import os

# for all files in source folder
for file in os.listdir(os.getcwd()):
    #if "_" present in file name
    if file.find("_") >= 0:
        newName = file.replace("_", " ")
        #Rename file with same name replacing underscores with spaces
        os.rename(file, newName)
