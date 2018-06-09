__author__ =  "Txanton Bejos"

import os
import renamer

spath = str(os.getcwd())

for root, dirs, files in os.walk(spath):
    for dir in dirs:
        print("***")
        print(dir)
        print("***")
        renamer.start(dir)
