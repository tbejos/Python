_author__ =  "Txanton Bejos"

import os
import re
import pathlib

def run():
    spath = str(os.getcwd())

    for root, dirs, files in os.walk(spath):
        for dir in dirs:
            print("***")
            print(dir)
            print("***")
            # start(os.path.abspath(dir))
            start(os.path.join(root, dir))


badwords = ["x264", "x265", "BluRay", "YIFY", "YTS AG", "YTS AM", "BrRip", "WEBRip"]
pattern = re.compile(r'.[0-9]{4}.')  # String of numbers length 4
res = re.compile(r'[0-9]{3,4}p')


def start(path):
    print("###")
    for file in os.listdir(path):
        if file[0] == "." or file[0:2] == "__":
            continue
        print(file)
        newName = file
        newName = newName.replace("_", " ")
        newName = newName.replace("[", "").replace("]", "")

        beginning = re.search(pattern, newName)
        if beginning:
            year = newName[beginning.start() + 1: beginning.end() - 1]
            newName = newName[:beginning.start()] + " (" + year + ") " + \
                      newName[beginning.end():]

        # We do this afterwards because if the movie title has a year in it then
        # this will make sure we don't modify it
        newName = newName.replace(".", " ", file.count(".") - 1)
        for word in badwords:
            newName = newName.replace(word, "")
        # Remove any trailing spaces between resolution and file extension
        resol = re.search(res, newName)
        if resol and newName.rfind(".") >= 0:
            newName = newName[:resol.end()] + pathlib.Path(file).suffix
        newName = ' '.join(newName.split())
        os.rename(os.path.join(path, file), os.path.join(path, newName))
        print(newName)
    print("###")

def main():
    run()

if __name__ == "__main__":
    main()
