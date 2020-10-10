import mysql.connector
import os

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="python"
)


def insert_data(db):
    ID = input("Masukan ID : ")
    Nama = input("Masukan Nama Lengkap : ")
    Kelahiran = input("Masukan Tanggal Lahir y/m/d :")
    val = (ID, Nama, Kelahiran)
    cursor = db.cursor()
    sql = "Insert Into biodata (ID,Nama,Kelahiran) Values (%s,%s,%s)"
    cursor.execute(sql, val)
    db.commit()
    print("{} Data Berhasil ditambahkan".format(cursor.rowcount))


def show_data(db):
    cursor = db.cursor()
    sql = "Select * from biodata"
    cursor.execute(sql)
    results = cursor.fetchall()

    if cursor.rowcount < 0:
        print("tidak ada")
    else:
        for data in results:
            print(data)


def update_data(db):
    cursor = db.cursor()
    show_data(db)
    Id = input("Masukan Id yang akan dirubah : ")
    Nama = input("Rubah Nama : ")
    Kelahiran = input("Rubah Kelahiran : ")
    sql = "Update biodata set Nama=%s , Kelahiran=%s Where ID=%s"
    val = (Nama, Kelahiran, Id)
    cursor.execute(sql, val)
    db.commit()
    print("{} data berhasil diubah".format(cursor.rowcount))


def delete_data(db):
    cursor = db.cursor()
    show_data(db)
    Id = input("Masukan Id yang akan dihapus : ")
    sql = "DELETE FROM biodata WHERE ID=%s"
    val = (Id,)
    cursor.execute(sql, val)
    db.commit()
    print("{} data berhasil dihapus".format(cursor.rowcount))


def show_menu(db):
    print("===Aplikasi Database Python===")
    print("1. Insert Data")
    print("2. Tampilkan Data")
    print("3. Rubah Data")
    print("4. Hapus Data")
    print("0. Keluar")
    print("------------------------------")

    menu = input("Pilih Menu = ")
    os.system("cls")

    if menu == "1":
        insert_data(db)
    elif menu == "2":
        show_data(db)
    elif menu == "3":
        update_data(db)
    elif menu == "4":
        delete_data(db)
    elif menu == "0":
        exit()
    else:
        print("Input Salah")


if __name__ == "__main__":
    while (True):
        show_menu(db)
