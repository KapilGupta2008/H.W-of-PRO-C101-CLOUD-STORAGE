import os;
import shutil;
path = input("enter the name of the directory to be sorted: ")

listOfFiles= os.listdir(path)

for i in listOfFiles:
    name,ext = os.path.splitext(i)
    ext =ext[1:]
    if(ext==''):
        continue
    if os.path.exists(path+'/'+ext):
        shutil.move(path+'/'+i,path+'/'+ext+'/'+i)
    else:
        os.mkdir(path+'/'+ext)
        shutil.move(path+'/'+i,path+'/'+ext+'/'+i)