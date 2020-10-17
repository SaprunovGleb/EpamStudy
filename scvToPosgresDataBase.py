# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 13:59:57 2020

@author: Flyin
"""

import psycopg2
import sys

def connetionWhithDataBase(database="Epam",user="Sql",password="Sql",host="127.0.0.1", port="5432"):
    con = psycopg2.connect(
        dbname=database,
        user=user,
        password=password,
        host=host)
    return con

def lineAdaptation(line):
    l=1
    if line[0:2]=='",':
        line = line[2:]
    line = line.replace('""',"'")
    massProm = line.split('"')
    i=0
    mass=[]
    while i<len(massProm):
        if i % 2 == 0:
            mass2=massProm[i].split(',')
            j=0
            while j<len(mass2):
                if i == 0 and j == 0:
                    mass.append(mass2[j])
                elif i == len(massProm)-1 and j ==len(mass2)-1:
                    mass.append(mass2[j])
                elif j!=0 and j!=len(mass2)-1:
                    mass.append(mass2[j])
                j+=1
        else:
            mass.append(massProm[i])
        i+=1
    # if len(mass)!=18 and len(mass)!=6:
    #     print(line)
    #     print(mass," ",len(mass)," ",t)
    #     l = input()

    # if l=="0":
    #     sys.exit()
    return mass

def massInTable(cur, sql, mass):
    j=0
    while j< len(mass):
        if mass[j]=="":
                mass[j]="NULL"
        j+=1      
    cur.execute(sql,(mass[0],mass[1],mass[2],mass[3],mass[4],mass[5],mass[6],mass[7],mass[8],mass[9],
                     mass[10],mass[11],mass[12],mass[13],mass[14],mass[15],mass[16],mass[17]))

if __name__ == '__main__':
    print("Programme to work with database")
    sql = "INSERT INTO consumercomplaints (datareceived, productname, subproduct, issue, subissue, consumercomplaintnarrative, companypublicresponse, company, statename, zipcode, tags, consumerconsentprovided, submittedvia, datesenttocompany, companyresponsetoconsumer, timelyresponse, consumerdisputed, complaintid) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    try:
        con = connetionWhithDataBase()
        print("Database opened successfully")
    except Exception:
        print("Database didn't open successfully")
        input()
        sys.exit()
    cur = con.cursor()
    pathInPutFile="P9-ConsumerComplaints.csv"
    inPutFile=open(pathInPutFile)
    i=0
    mass=[]
    lastLine = ""
    # doPrint = True
    for line in inPutFile:
        line = line.replace('\n',"")
        if len(mass) != 18:
            line = lastLine+line
            # doPrint = True
        mass = lineAdaptation(line)
        #print(mass)
        if len(mass) != 18:
            lastLine = line
        elif i!=0:
            lastLine = ""
            print(i)
            if i == 13355:
                print(line, mass, len(mass), "\n")

            massInTable(cur, sql, mass)
            
        # if doPrint:
        #     print(mass, len(mass), "\n")
        #     doPrint = False
        i+=1
    con.commit()
    print("Data uploads in Table")
    con.close()
    # print("все по 18")