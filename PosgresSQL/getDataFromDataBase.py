# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 11:09:37 2020

@author: Flyin
"""

import psycopg2



def connetion_with_data_base(database="Movies",user="Sql",password="Sql",host="127.0.0.1", port="5432"):
    con = psycopg2.connect(
        dbname=database,
        user=user,
        password=password,
        host=host)
    return con


def text_scan_data(cur, scancolumn, line, table = "movie_mini",
                   showncolums = "movie_title, actor_1_name, genres, imdb_score",
                   orderby = "imdb_score", way = ""):
    sql = """SELECT """+showncolums+"""
            FROM """+table+"""
            WHERE """+scancolumn+""" @@ plainto_tsquery('"""+line+"""')
            ORDER BY """ + orderby + " " + way
    cur.execute(sql) 
    rows = cur.fetchall()
    return rows

    
    

if __name__ == '__main__':
    
    try:
        con = connetion_with_data_base()
        print("Database 'Movies' opened successfully")
    except Exception:
        print("Database 'Movies' didn't open successfully")
        input()
        sys.exit()
    cur = con.cursor()
    print("Print 1, if you scan in column genres")
    print("Print 2, if you scan in column movie_title")
    column = input()
    print("Print how much lines, you want to see at the same time")
    shownLine = int(input())
    print("Print what you need to scan")
    line = input()
    if column == '1':
        column = "genres"
    elif column == '2':
        column = "movie_title"
    rows = text_scan_data(cur = cur, scancolumn = column, 
                          line = line, way = "DESC")
    con.close()
    i = 1
    print("Print 0 or exit to finish work")
    for row in rows:
        print("  ".join(map(str,row)))
        i += 1
        if i == shownLine:
            i = 0 
            l = input()
            if l == "0" or l == "exit":
                sys.exit()
        
    print ("Count of lines: ", len(rows)) 

    
    
    
    
    
    
