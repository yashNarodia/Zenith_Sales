from sqlite3 import Row
import mysql.connector as sql

mydb = sql.connect(host="localhost",
user= "root",
password ="admin",
database="zenithsales")
l=[]
mycursor =mydb.cursor()
mycursor.execute("select * from metalInput ;" )
partynames=mycursor.fetchall()
for names in partynames:
    l.append(names[0])

print(l)