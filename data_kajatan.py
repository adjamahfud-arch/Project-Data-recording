|import json
import input

class Human:
      def __init__(self, nama, alamat, hadiah, beras, uang, dll):
            self.nama =nama
            self.alamat =alamat
            self.gula =hadiah
            self.beras =beras
            self.dll =dll
            self.uang =uang
            self.status =True
            
      @classmethod    
      def from_dict(cls, data):  
             data_olah =cls(data["nama"], data["alamat"], data["gula"], data["beras"],data["uang"], data["dll"])
             
             data_olah.status =data["status"]
             return data_olah
           
      def hapus(self):
             self.status =False
             
      def to_dict(self):
             return {
                  "nama": self.nama,
                  "alamat": self.alamat,
                  "gula": self.gula,
                  "beras": self.beras,
                  "uang": self.uang,
                  "status": self.status
             }
            
class Simpan:
      def __init__(self, file):
            self.file_path =file
            self.data_base =self.load_data
      def load_data(self):
             try:
                 with open(self.file_path, "r", encoding="utf-8") as file:
                          data_mentah =json.load(file)
                          return [Human.from_dict(z) for z in data_mentah]
                          
             except FileNotFoundError:
                          return []
                          
             except Exception as k:
                          print(f"error:{k}")
      def tambah(self, data_):
             self.data_base.append(data_)
             
                               
      def simpan_data(self):
             try:
                 with open(self.file_path, "w") as file:
                          ubah =[y.to_dict() for y in self.data_base]
                          
                          json.dump(ubah, file, indent=4)
                          print("data berhasil di simpan")
                 
             except Exception as l:
                          print(f"error:{l}")
                          
                       
      def tampilkan(self):
             if len(self.data_base) == 0:
                 print("belum ada data")
                 return
                 
             for x in self.data_base:
                   if  x.status:
                       print(f"nama:{x.nama:<10} | hadiah:{x.alamat:<8} | hadiah lain:{x.gula} | {x.beras} | {x.uang}")
                       
            
sb =Simpan("data_base.json")
while True:
      print("1.tambah orang")
      print("2.tampilkan data")
      print("3.keluar")
      
      pilihan =input.pilih()
      
      if pilihan == 1:
          nama =input.pertanyaan_1()
          alamat =input.pertanyaan_2()
          gula =input.pertanyaan_3()
          beras =input.pertanyaan_4()
          uang =input.pertanyaan_5()
          
          
          
      elif pilihan == 3:
         print("keluar dari sistem")
         break
         
      
      
     
    
      
      