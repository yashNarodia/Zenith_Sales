from sqlite3 import Row
import mysql.connector as sql

mydb = sql.connect(host="localhost",
user= "root",
password ="admin",
database="trial")

mycursor =mydb.cursor()
mycursor.execute("select * from trail;" )
datas =  mycursor.fetchall()
mycursor.execute("SELECT count(*) FROM information_schema.columns WHERE table_name ='trail';")
col=mycursor.fetchone()
mycursor.execute("SELECT count(*) FROM trail ")
rows=mycursor.fetchone()

print(col[0])
print(rows[0])
for data in datas:
    print(data[0])