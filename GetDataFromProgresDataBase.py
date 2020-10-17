# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 10:30:50 2020

@author: Flyin
"""
import psycopg2
import datetime

def connetionWhithDataBase(database="Epam",user="Sql",password="Sql",host="127.0.0.1", port="5432"):
    con = psycopg2.connect(
        dbname=database,
        user=user,
        password=password,
        host=host)
    return con

def getDataRange():
    scan = True
    print("Give the first date please (format yyyy-mm-dd)")
    while scan:
        data1 = input()    
        data1 = data1.split('-')
        #print (data1)
        try:
            data1 = datetime.date(int(data1[0]),int(data1[1]),int(data1[2]))
            print ("First date: ", data1)
            scan = False
        except Exception:
            print("Give the first date please (format yyyy-mm-dd)")
    scan = True
    print("Give the last date please (format yyyy-mm-dd)")
    while scan:
        data2 = input()    
        data2 = data2.split('-')
        #print (data1)
        try:
            data2 = datetime.date(int(data2[0]),int(data2[1]),int(data2[2]))
            print ("Last date: ", data2)
            scan = False
        except Exception:
            print("Give the first date please (format yyyy-mm-dd)")
    if data2>data1:
        print("Your date range", data1, "-", data2)
        return data1, data2
    else:
        print("Your date range", data2, "-", data1)
        return data2, data1
        
def getTableDateInRange(cur,data1,data2):
    
    sql = """select productname, count(productname) as amountofissues, 
            (count(productname) FILTER (WHERE timelyresponse = 'Yes')) as counttimelyresponse,
        	(count(productname) FILTER (WHERE consumerdisputed = 'Yes')) as countconsumerdisputed
        FROM
            consumercomplaints
        WHERE
            (datareceived >= '"""+str(data1)+ "' AND datareceived <='" + str(data2)+"""')
        group by productname order by amountofissues desc"""
    #sql = "select * FROM consumercomplaints"
        
    cur.execute(sql)
    rows = cur.fetchall()
    #print(len(rows))
    
    print("%25s %20s %20s %20s" % ("productname"," amountofissues"," counttimelyresponse"," countconsumerdisputed"))
    for row in rows:
        print("%25s %20s %20s %20s" % (row[0],row[1],row[2],row[3]) )

def getCompanyName():
    print("Print company name:")
    companyName = input()
    return companyName

def getTableOnCompany(cur,companyName):
    sql = """WITH companyTable AS
        (select *
        FROM consumercomplaints
        where company = '"""+companyName+"""'),
        
        stateTable as
        (select statename, count(statename) as colState
        FROM companyTable
        group by statename order by colState desc limit 1)
        
        select *
        from companyTable as t1
        inner join stateTable as t2 on t1.statename = t2.statename"""
    cur.execute(sql) 
    rows = cur.fetchall()
    for row in rows:
        print("  ".join(map(str,row)), "\n\n")
    print ("Count of lines: ", len(rows)) 
    
def maingetTableDateInRange():
    con = connetionWhithDataBase()
    cur = con.cursor()
    data1, data2 = getDataRange()
    getTableDateInRange(cur,data1,data2)
    con.close()

def maingetTableOnCompany():
    con = connetionWhithDataBase()
    cur = con.cursor()
    companyName = getCompanyName()
    getTableOnCompany(cur,companyName)
    con.close()   



if __name__ == '__main__':
    print ("1: is issues statistic in date range")
    print ("2: is issues statistic with company")
    print ("0: exit")
    scan = True
    while scan:
        i = input()
        if i == "0":
            scan = False
        elif i == "1":
            maingetTableDateInRange()
        elif i == "2":
            maingetTableOnCompany()
            
    