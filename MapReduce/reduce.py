# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 13:06:01 2020

@author: Flyin
"""

import gzip
import sys
import time

def reduce_work(file="D:\университет\Epam\docker\MapReduce\input_files_test\input_file_2019-11-01T11_38_50.645817.gz",
           chunk_size=1024, outFile="1.txt"):
    #timeStart = time.time() 
    f = gzip.open(file, 'rb')
    col=0

    while True: 
        chunk = f.read(chunk_size)
        
        for num in chunk:
            if num != 0:
                byte = bin(num)[2:]
                i = byte.count("1")
                col+=i         
                #if input() == "0":
                    #sys.exit()
        if not chunk:
            break
    f.close()
    #print(time.time() - timeStart)
    #print(col)
    f = open(outFile,"a+")
    f.write(str(col)+"\n")
    f.close()


def reduce_main(arrayFiles,numberProcess,namedirinnod):
    outFile = namedirinnod+str(numberProcess)+".txt"
    f = open(outFile,"w")
    f.close()
    i=0
    N=len(arrayFiles)
    while i < N:
        reduce_work(file=arrayFiles[i],outFile = outFile)
        i += 1
        
if __name__ == '__main__':
    reduce_main(sys.argv[1], sys.argv[2],sys.argv[3])