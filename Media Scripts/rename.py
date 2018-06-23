_author__ =  "Txanton Bejos"

import os
import re
import pathlib
import argparse

# Argument Flags
parser = argparse.ArgumentParser()
parser.add_argument("--verbose", action='store_true',
    help="Output the files and changes")
parser.add_argument("--test", '-t', action='store_true',
    help="Will run the script without renaming files, for use with verbose flag")
parser.add_argument("--input", "-i",
    help="Allow for passing in the " "destination source folder")
args = parser.parse_args()

# RegEx and Files/Filetypes
list = open('blacklist.txt')
blacklist = [line.rstrip('\n') for line in list]
pattern = re.compile('[\s.][0-9]{4}[\s.]')
res = re.compile('[0-9]{3,4}?p')
include = ['.mp4', '.srt', '.mkv', '.avi']

def run():
    if args.input:
        spath = str(args.input)
    else:
        spath = str(os.getcwd())

    start(spath)
    for root, dirs, files in os.walk(spath):
        for dir in dirs:
            if dir[0] == "." or dir[0:2] == "__":
                continue
            start(os.path.realpath(os.path.join(root, dir)))

        # Display Tree of Files
        if args.verbose:
            level = root.replace(spath, '').count(os.sep)
            indent = ' ' * 4 * (level)
            print('{}{}/'.format(indent, os.path.basename(root)))
            subindent = ' ' * 4 * (level + 1)
            for f in files:
                print('{}{}'.format(subindent, f))

def start(path):
    for file in os.listdir(path):
        if pathlib.Path(file).suffix not in include:
            continue

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
        for word in blacklist:
            newName = newName.replace(word, "")

        while '  ' in newName:
            newName = newName.replace('  ', ' ')

        # Remove any trailing spaces between resolution and file extension
        resol = re.search(res, newName)
        if resol and newName.rfind(".") > 0:
            newName = newName[:resol.end()] + pathlib.Path(file).suffix

        if not args.test:
            os.rename(os.path.join(path, file), os.path.join(path, newName))

def main():
    run()

if __name__ == "__main__":
    main()
