# Author: Txanton Bejos
import os
import re

# Webrip
badwords = ["x264", "x265", "BluRay", "YIFY", "YTS AG", "YTS AM", "BrRip"]
pattern = re.compile(r'.[0-9]{4}.')  # String of numbers length 4

for file in os.listdir(os.getcwd()):
    newName = file
    newName = newName.replace("_", " ")
    newName = newName.replace("[", "").replace("]", "")

    beginning = re.search(pattern, newName)
    if beginning:
        year = newName[beginning.start() + 1: beginning.end() - 1]
        newName = newName[:beginning.start()] + ".(" + year + ")." + \
                  newName[beginning.end():]

    # We do this afterwards because if the movie title has a year in it then
    # this will make sure we don't modify it
    newName = newName.replace(".", " ", file.count(".") - 1)
    for word in badwords:
        newName = newName.replace(word, "")
    newName = ' '.join(newName.split())
    # Remove any trailing spaces between resolution and file extension
    fileExtension = newName.rfind(".")
    newName = newName[:fileExtension].rstrip() + newName[fileExtension:]
    os.rename(file, newName)
