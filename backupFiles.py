import os;
import shutil;

source = input("enter the source folder name: ")
destination  = input("enter the destination folder name: ")

source = source + "/"
destibnation = destination +'/'

listOfFiles = os.listdir(source)

for i in listOfFiles:
    shutil.copy((source+i), destination)