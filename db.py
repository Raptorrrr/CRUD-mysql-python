import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="Python"
)

cursor = db.cursor()
sql = "INSERT INTO biodata (Id,Nama,Kelahiran) VALUES (%s,%s,%s)"
val = ("18081010123", "Iqbal", "2000-09-01")

db.commit()

print("{} data ditambahkan".format(cursor.rowcount))
