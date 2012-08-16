import csv
import json
import sqlite3
import sys

conn=sqlite3.connect(sys.argv[1])
cursor=conn.cursor()
cursor.execute("select value from data")
values=cursor.fetchall()
print values

