# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 11:04:47 2020

@author: Flyin
"""


import os
import multiprocessing 
from reduce import reduce_main

def file_map(colNods, namedirdata = "input_files_test", namedirinnod = "D:\университет\Epam\docker\MapReduce\input_files_test"):
    arraySize = []
    for i in range(colNods):
        arraySize.append([[],0])
    #print(arraySize)
    #Get work dir
    path = os.getcwd()
    #Get list of names work files
    files = os.listdir(path+"\\"+namedirdata) 
    #Create colNods lists of paths work files in nodes, with the nearest sum sizes
    for file in files:
        pathFile = namedirinnod+"\\"+file
        sizeFile = os.path.getsize(path+"\\"+namedirdata+"\\"+ file)
        arraySize.sort(key = lambda x: x[1])
        arraySize[0][1] += sizeFile
        arraySize[0][0].append(pathFile)
    return arraySize

def count(colNods):
    count = 0
    i = 0
    while i < colNods:
        file = str(i) + ".txt"
        f = open(file,"r")
        lines = f.readlines()
        for line in lines:
            count += int(line[:-1])
        i += 1
    return count
            
if __name__ == '__main__':
    namedirinnodIn = "D:\университет\Epam\docker\MapReduce\input_files_test"
    namedirinnodOut = "D:\университет\Epam\docker\MapReduce\\"
    colNods = int(input("How much nodes? "))
    arraySize = file_map(colNods=colNods, namedirdata = "input_files_test",namedirinnod=namedirinnodIn)
    i = 0 
    procs = []
    while i < colNods:
        manager = multiprocessing.Manager()
        arrayFiles = manager.list()
        arrayFiles = arraySize[i][0]
        proc = multiprocessing.Process(target=reduce_main, args=(arrayFiles,i,namedirinnodOut,))
        procs.append(proc)
        proc.start()
        i += 1
    for proc in procs:
        proc.join()
    print("Col bit == 1: ", str(count(colNods)))


