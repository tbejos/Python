# Author: Txanton Bejos
import os
import subprocess

for file in os.listdir(os.getcwd()):
    if file[-3:] == "mkv" and file[-7:] != "new.mkv":
        print(file[:file.rfind(".")])
        command = ["ffmpeg", "-i", file, "-c:v", "copy", "-c:a", "aac", "-b:a", "384k", file[:-4]+" - new.mkv"]
        subprocess.call(command)
