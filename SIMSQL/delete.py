import sqlite3

con = sqlite3.connect('karyawan.db')
statement = """
    DELETE FROM karyawan
    WHERE nama = ?;
"""
nama = 'Luqman'
cur = con.cursor()
#cur.execute(statement)
rows = cur.execute(statement,(nama,))
print(rows.rowcount)
con.commit()
