# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 11:47:45 2020

@author: Flyin
"""


import psycopg2
import sys

def connetion_with_data_base(database="Movies",user="Sql",password="Sql",host="127.0.0.1", port="5432"):
    con = psycopg2.connect(
        dbname=database,
        user=user,
        password=password,
        host=host)
    return con

def line_adaptation(line):
    if line[0:2]=='",':
        line = line[2:]
    line = line.replace('""',"'")
    arrayInter = line.split('"')
    i = 0
    array=[]
    while i<len(arrayInter):
        if i % 2 == 0:
            array2=arrayInter[i].split(',')
            j = 0
            while j<len(array2):
                if (i == 0) and (j == 0):
                    array.append(array2[j])
                elif (i == len(arrayInter)-1) and (j == len(array2)-1):
                    array.append(array2[j])
                elif (j != 0) and (j != len(array2)-1):
                    array.append(array2[j])
                j += 1
        else:
            array.append(arrayInter[i])
        i += 1
    return array


def array_in_table(cur, sql, array):
    j = 0
    while j< len(array):
        if array[j]=="":
                array[j]="NULL"
        j += 1      
    cur.execute(sql,(array[11],array[10],array[9].replace('|',", "),array[25]))



if __name__ == '__main__':
    print("Programme to work with database")
    sql = "INSERT INTO Movie_mini (movie_title, actor_1_name, genres, imdb_score) VALUES (%s, %s, %s, %s)"
    try:
        con = connetion_with_data_base()
        print("Database opened successfully")
    except Exception:
        print("Database didn't open successfully")
        input()
        sys.exit()
    cur = con.cursor()
    pathInPutFile = "movie_metadata.csv"
    inPutFile = open(pathInPutFile,"r", encoding='utf-8')
    i=0
    array = []
    lastLine = ""
    # doPrint = True
    for line in inPutFile:
        line = line.replace('\n',"")
        line = line.replace('В\xa0'," ")
        if len(array) != 28:
            line = lastLine+line
            # doPrint = True
        array = line_adaptation(line)
        if len(array) != 28:
            lastLine = line
        elif i != 0:
            array_in_table(cur, sql, array)
        i += 1
    con.commit()
    print("Data uploads in Table")
    con.close()
    # print("все по 18")