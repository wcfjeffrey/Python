# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 10:01:01 2020

@author: Jeffrey Woo
"""

import os
import csv
import sqlite3
import re

def load_data():
    path_root = r'C:\Users\user\Downloads\python-master\finally'
    dirs = os.listdir(path_root)
    conn = sqlite3.connect(r'C:\Users\user\Downloads\python-master\database.db3')#连接数据库
    c = conn.cursor()
    i=0
    for dir in dirs:
        i+=1
        file_name = dir.split('.')
        file_path =os.path.join(path_root,dir)

        input_filename=file_path
        file = open(input_filename,encoding="gbk",errors="ignore")
        file.readline() #读入第一行，后面的读取将从第二行开始
        reader=csv.reader(file)#打开每一张表
        for row in reader:
            str = re.sub("[A-Za-z0-9\!\%\[\]\,\。\_\ ]", "",file_name[0])#去掉表名中不符合规范的字符
            sql_1="create table if not exists %s"%(str)+"(id varchar(128), \
            Yeas_2017 varchar(128),Yeas_2016 varchar(128),Yeas_2015 varchar(128),\
            Yeas_2014 varchar(128),Yeas_2013 varchar(128))"
            sql_2="INSERT INTO %s"%(str)+" (id,Yeas_2013,Yeas_2014,Yeas_2015,\
            Yeas_2016,Yeas_2017) VALUES (:d1,:d2,:d3,:d4,:d5,:d6)"
            c.execute(sql_1)
            c.execute(sql_2,{'d1':row[0],'d2':row[1],'d3':row[2],'d4':row[3],'d5':row[4],'d6':row[5]})
            conn.commit()
        if (i%10==0):
            print(i)
    c.close()
def main():
    load_data()
main()