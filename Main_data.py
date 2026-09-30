import input
import json
from datetime import datetime

class Users:
   def __init__(self,nama,alamat,gula,beras,uang,dll):
       self.nama =nama
       self.alamat =alamat
       self.gula =gula
       self.beras =beras
       self.uang =uang
       self.dll =dll
       self.status =True
     
   @classmethod
   def from_dict(cls,data):
       data_ =cls(data["nama"],data["alamat"],data["gula"],data["beras"],data["uang"],data["dll"])
       data_.status =data["status"]
       return data_
   def to_dict(self):
       return {
          "nama":self.nama,
          "alamat":self.alamat,
          "gula":self.gula,
          "beras":self.beras,
          "uang":self.uang,
          "dll":self.dll,
          "status":self.status
       }
  

class Simpan:
   def __init__(self,file):
       self.file =file
       self.data_base =self.load_file()
   def tambah(self,data):
       self.data_base.append(data)
     
   def hapus(self,data_hapus):
       for L in self.data_base:
           if L.nama ==data_hapus:
              L.status =False
              print(f"data milik {data_hapus} berhasil di hapus")
              return
       print(f"data {data_hapus} tidak di temukan")
       
   def veref_(self,username):
       if len(self.data_base) ==0:
          print("data masih kosong")
          return
       for u in self.data_base:
           if u.status and u.nama ==username:
              return True
    
       print("data tidak di temukan")
       return False
      
            
             
   def update(self,nama,atribut,nilai_baru):
       if len(self.data_base) ==0:
          print("tidak ada data yang bisa di ubah")
          return
       for a in self.data_base:
          if a.status and a.nama ==nama:
             if hasattr(a,atribut):
                setattr(a,atribut,nilai_baru)
                print("data berhasi di ubah")
                return
             else:
                print(f"{atribut} pada {nama} tidak di temukan")
                return
       print(f"{nama} tidak di temukan")
     
                
             
       
       
   def tampilkan(self):
       if len(self.data_base) ==0:
          print("data masih kosong")
          return
       for z in self.data_base:
           if z.status:
              print(f"{z.nama:<10} | {z.alamat:<10} | {z.gula} | {z.beras} | {z.uang} | {z.dll:<10}")
         
   def simpan_data(self):
       try:
         with open(self.file, "w", encoding="utf-8") as file:
              simpan =[y.to_dict() for y in self.data_base]
              json.dump(simpan,file,indent=4)
           
       except Exception as e:
            print(f"error:{e}")
      
   def load_file(self):
       try:
         with open(self.file, "r", encoding="utf-8") as file:
              data_mentah =json.load(file)
              return [Users.from_dict(x) for x in data_mentah]
       except FileNotFoundError:
            return []
       except Exception as e:
            print(f"error:{e}")
            

         
def kolom():
    print("1.tambah user")
    print("2.tampilkan data")
    print("3.keluar")
    print("4.update data")
  
def pilihan():
    print("1.gula")
    print("2.beras")
    print("3.uang")
    print("4.alamat")
    print("5.dll")
    print("6.nama")
def dict_n():
    return {
      "1":"gula",
      "2":"beras",
      "3":"uang",
      "4":"alamat",
      "5":"dll",
      "6":"nama"
    }

sb =Simpan("data_base.json")
while True:
   kolom()
   pilih_ =input.pilih()
   if pilih_ ==1:
      nama_ =input.pertanyaan_1()
      alamat_ =input.pertanyaan_2()
      gula_ =input.pertanyaan_3()
      beras_ =input.pertanyaan_4()
      uang_ =input.pertanyaan_5()
      dll_ =input.pertanyaan_6()
      simpan =Users(nama_,alamat_,gula_,beras_,uang_,dll_)
      sb.tambah(simpan)
      sb.simpan_data()
      print("data berhasil di simpan")
     
   elif pilih_ ==2:
        sb.tampilkan()
     
   elif pilih_ ==3:
        print("keluar dari program")
        break
   elif pilih_ ==4:
        name_ =input.pertanyaan_1()
        if not sb.veref_(name_):
           continue
        else:
           pilihan()
           condisi =input.pilih_2()
           dict_ =dict_n()
           if condisi in dict_:
              isi_attr =dict_[condisi]
              nilai_new =input.pertanyaan_7()
              sb.update(name_,isi_attr,nilai_new)
              sb.simpan_data()
           else:
              print(f"{condisi} tidak ada terdafdar dalam data")
   elif pilih_ ==5:
        delete_ =input.pertanyaan_8()
        sb.hapus(delete_)
        sb.simpan_data()
   
        
      
        
        
          
           
           
        
   
     
     
    