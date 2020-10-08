# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 18:18:34 2020

@author: Flyin
"""
import os

def makeListOfFiles(directory,massFiles):

    files = os.listdir(directory) 
    #print(files)
    for file in files:
        filePath = directory + "\\" + file
        if os.path.isdir(filePath):
            #print("Директория ", filePath)
            makeListOfFiles(filePath,massFiles)
        elif os.path.isfile(filePath):
            #print("Файл ", filePath)
            massPromFile = []
            massPromFile.append(filePath)
            massPromFile.append(os.path.getsize(filePath))
            #print(massPromFile)
            massFiles.append(massPromFile)
        
def linkCopy(massFiles):
    #print (massFiles)
    i=0
    massLinkedFiles=[]
    while i < (len(massFiles)-1):
        j=1
        while (j+i)<len(massFiles):
            if massFiles[i][1]==massFiles[i+j][1]:
                fileI= open(massFiles[i][0],"rb")
                fileJ= open(massFiles[i+j][0],"rb")
                #print(fileI.read())
                #print(fileJ.read())
                if fileI.read()==fileJ.read():
                    fileJ.close()
                    os.remove(massFiles[i+j][0])
                    os.link(massFiles[i][0],massFiles[i+j][0])
                    massLinkedFiles.append(massFiles[i+j][0])
                    massFiles.pop(i+j)
                else:
                    j+=1
                fileI.close()
                fileJ.close()
            else:
                break
        i+=1
    print(massLinkedFiles,len(massLinkedFiles))
                
                
                
                
def changeCopyToLink(directory="D:\Testdir"):
    if os.path.isdir(directory):
        massFiles=[]
        makeListOfFiles(directory,massFiles)
        massFiles.sort(key = lambda x: x[1])
        linkCopy(massFiles)
    else:
        print("Передайте значение существующей директории")




#changeCopyToLink("D:\Testdir")
