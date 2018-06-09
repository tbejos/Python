__author__ =  "Txanton Bejos"

import os
import re

# Webrip
badwords = ["x264", "x265", "BluRay", "YIFY", "YTS AG", "YTS AM", "BrRip"]
pattern = re.compile(r'.[0-9]{4}.')  # String of numbers length 4

def start(dir):
    for file in dir:
        if file[0] == "." or file[0:2] == "__":
            continue
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

        # Removes any left over .'s from unrecognized words
        newName = newName.replace(".", " ", file.count(".") - 1)
        newName = ' '.join(newName.split())
        # Remove any trailing spaces between resolution and file extension
        resolution = re.search(res, newName)
        if resolution:
            newName = newName[:resolution.end()] + newName[newName.rfind("."):]
        os.rename(path + os.sep + file, path + os.sep + newName)
