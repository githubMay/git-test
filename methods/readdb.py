#!/usr/bin/env Python
# coding=utf-8

from .db import *
'''import psycopg2
print('start inquiring the information!')
conn=psycopg2.connect(host="localhost",database="postgres",user="postgres",password="")
cur = conn.cursor() '''

def select_table(table, column, condition, value ):
    sql = "select " + column + " from " + table + " where " + condition + "='" + value + "'"
    cur.execute(sql)
    lines = cur.fetchall()
    print('ending inquiring!')
    return lines