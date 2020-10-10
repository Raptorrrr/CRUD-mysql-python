import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="python"
)

cursor = db.cursor()
ID = 18081010123
Nama = "Nafa"
Kelahiran = "1999-09-01"
val = (ID, Nama, Kelahiran)
sql = "INSERT INTO biodata (Id,Nama,Kelahiran) VALUES (%s,%s,%s)"
cursor.execute(sql, val)
db.commit()

print("{} data ditambahkan".format(cursor.rowcount))
