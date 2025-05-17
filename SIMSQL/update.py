import sqlite3

con = sqlite3.connect('karyawan.db')
statement = """
    UPDATE karyawan
    SET
        umur = ?,
        kota = ?
    WHERE nama = ?;
"""
nama = input('Nama :  ')
umur = input('Umur :  ')
kota = input('kota:  ')

cur = con.cursor()
#cur.execute(statement)
rows = cur.execute(statement,(umur,kota,nama,))
print(rows.rowcount)
con.commit()