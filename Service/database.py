import sqlite3
from rapidfuzz.distance import Levenshtein

class Data:
   def __init__(self):
       self.con =sqlite3.connect("data_kajatan.db")
       self.creat()
       self.con.row_factory=sqlite3.Row
       self.con.create_function(
            "ukur",
            2,
            Levenshtein.distance
       )

   def creat(self):
       self.con.execute("""
            CREATE TABLE IF NOT EXISTS record (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nama VARCHAR(20) NOT NULL,
                alamat VARCHAR(30) NOT NULL,
                beras REAL DEFAULT 0,
                gula REAL DEFAULT 0,
                uang INT DEFAULT 0,
                dll TEXT DEFAULT 'kosong'
            )"""
       )

   def tambah(self,nama: str,alamat: str,beras: int,gula: int,uang: int,dll: str):
       self.con.execute("""
            INSERT INTO record (nama,alamat,beras,gula,uang,dll)
            VALUES (?,?,?,?,?,?)
            """,
            (nama,alamat,beras,gula,uang,dll)
       )
       self.con.commit()

   def luru(self,nama: str):
       cursor =self.con.cursor()
       cursor.execute("""
           SELECT *, ukur(nama,?) AS skor
           FROM record
           WHERE ukur(nama,?) <= 3
           ORDER BY skor ASC
           """,
           (nama,nama)
       )
       hasil =cursor.fetchall()
       for row in hasil:
           print(
              row["nama"],
              row["alamat"],
              row["beras"],
              row["gula"],
              row["uang"],
              row["dll"]
           )
         
   def tutup(self):
       self.con.close()
     
if __name__=="__main__":
   gile =Data()
   