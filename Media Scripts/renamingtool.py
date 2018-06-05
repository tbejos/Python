# Author: Txanton Bejos
import os

#Webrip
badwords = ["x264", "x265", "BluRay", "YIFY"]

for file in os.listdir(os.getcwd()):
    newName = file
    newName = newName.replace("_", " ")
    newName = newName.replace("[", "").replace("]", "")
    newName = newName.replace(".", " ", file.count(".") - 1)
    for word in badwords:
        newName = newName.replace(word, "")
    newName = ' '.join(newName.split())
    os.rename(file, newName)
