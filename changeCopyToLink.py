# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 18:18:34 2020

@author: Saprunov Gleb

version 2.0
"""
import os
import sys

def make_list_of_files(directory,arrFiles):

    files = os.listdir(directory) 
    #print(files)
    for file in files:
        #Make full path for each file and directory
        filePath = directory + "\\" + file
        if os.path.isdir(filePath):
            #print("Директория ", filePath)
            #For directory use recursion 
            make_list_of_files(filePath,arrFiles)
        elif os.path.isfile(filePath):
            #print("Файл ", filePath)
            #For each file make array and put there full path and size
            arrPromFile = [filePath, os.path.getsize(filePath)]
            #print(arrPromFile)
            #This array add to array of all files
            arrFiles.append(arrPromFile)
        
def link_copy(arrFiles):
    #print (arrFiles)
    i=0
    arrLinkedFiles=[]
    #Here we take each file in arrFiles in sequence.
    while i < (len(arrFiles)-1):
        j=1
        #Here we take each file further on the array
        while (j+i)<len(arrFiles):
            #If size is the same, open files to compare
            if arrFiles[i][1] == arrFiles[i+j][1]:
                fileI = open(arrFiles[i][0],"rb")
                fileJ = open(arrFiles[i+j][0],"rb")
                #print(fileI.read())
                #print(fileJ.read())
                #If they are the same we change i+j file to link
                if fileI.read()==fileJ.read():
                    fileJ.close()
                    os.remove(arrFiles[i+j][0])
                    os.link(arrFiles[i][0],arrFiles[i+j][0])
                    #We remove this file out the arrFiles
                    arrFiles.pop(i+j)
                    #We add fule path of link to array
                    arrLinkedFiles.append(arrFiles[i+j][0])
                else:
                    #Here we add 1, because we need to change 2 file.
                    #If 2 file is the same of the 1, his path get away from
                    #array, else number of 2 file in array grows on 1.
                    j += 1
                fileI.close()
                fileJ.close()
            #If size not the same stop stop taking the following files
            else:
                break
        i += 1
    #We show added links, and amount of them.
    print(arrLinkedFiles,len(arrLinkedFiles))
                
                
                
                
def change_copy_to_link(directory="D:\Testdir"):
    if os.path.isdir(directory):
        #Make array for full paths files
        arrFiles=[]
        make_list_of_files(directory,arrFiles)
        #Sort array by size o files
        arrFiles.sort(key = lambda x: x[1])
        #Link copies
        link_сopy(arrFiles)
    else:
        print("Pass the full path of an existing directory")

if __name__ == '__main__':
    # With the argument you should give full path to directory,  
    # within which all the same files will be linked, including subfolders
    change_copy_to_link(sys.argv[1])


#changeCopyToLink("D:\Testdir")
