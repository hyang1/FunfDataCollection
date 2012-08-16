import csv
import json
import sqlite3
import sys
import ast
    
def write(thing):
    writer.writerow(thing)
    
conn=sqlite3.connect(sys.argv[1])
c=conn.cursor()
c.execute("select probe, value from data")
values=c.fetchall()

data=[]
for(probe, json_string)in values:
    d=json.loads(json_string)
    data.append(d)

data=filter(lambda x:'TIMESTAMP'in x, data)
sorted_data=sorted(data,key=lambda x: x['TIMESTAMP'])
probes=set(map(lambda x:x['PROBE'], sorted_data))

probe=[]
for a in probes:
    probe.append(a)
    
instrument=filter(lambda x:x['PROBE']==probe[0], sorted_data)
battery=filter(lambda x:x['PROBE']==probe[1], sorted_data)
accel=filter(lambda x:x['PROBE']==probe[2], sorted_data)

f=open("crap.csv", "wb")
csv_file=csv.writer(f)
csv_file.writerow(["STATUS","MEAN","STANDARD_DEVIATION","MAXIMUM_DEVIATION"])

for item in accel:
    csv_file.writerow([item["MEAN"],item["STANDARD_DEVIATION"],item["MAX_DEVIATION"]])
    
f.close()
    
#stillSet=filter(lambda x:x['STATUS']=='STILL', accel)
#activeSet=filter(lambda x:x['STATUS']=='ACTIVE', accel)


#means=set(map(lambda x:x['MEAN'], accel[0]))
#maxDev=set(map(lambda x:x['MAX_DEVIATION'], accel))
#staDev=set(map(lambda x:x['STANDARD_DEVIATION'], accel))


        
        
 

