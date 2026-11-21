import json
import sys
from pathlib import Path
from difflib import SequenceMatcher
import Module.input as vld
from helper.waktu import time

file_dir =Path(
    "/storage/emulated/0/proyek data kajatan/Service"
)

sys.path.insert(0, str(file_dir))
from Service.kelas import Ini
from Service.service import Ssimpan
from Service.database import Data

format_wkt ="%H-%M %d %m %Y %A"

class Simpan:
   def __init__(self):
       self.data_base =Ssimpan.load()
     
   def tambah(self,data):
       self.data_base.append(data)
     
   def skors(self,user,dta):
       return SequenceMatcher(
          None,
          user,
          dta
          
      ).ratio()
         
       
       
   def simple_serch(self,nama: str,trestold=0.5) -> int:
       data_hasil =[]
       for item in self.data_base:
           skor =self.skors(nama,item.nama)

           if item.status and skor >=trestold:
              data_hasil.append((item,skor))
       data_hasil.sort(key=lambda p:p[1], reverse=True)
       return data_hasil
     
   def tampilkan_search(self,usernama: str) -> None:
       hasil =self.simple_serch(usernama)
       if not hasil:
          print(f"tidak ada data yang cocok dengan {usernama}")
       else:
         for hsl in hasil:
             nama =hsl[0]
             print(f"{nama.nama:<10} | {nama.alamat:<10} | {nama.gula} | {nama.beras} | {nama.uang:<10} | {nama.dll}")
           
           
           
       

          
         
           

       
       
         
          
     
             
                 
                
          
       
          
               
              
   def hapus(self,data_hapus: str) -> None:
       for L in self.data_base:
           if L.nama ==data_hapus:
              L.status =False
              print(f"data milik {data_hapus} berhasil di hapus")
              return
       print(f"data {data_hapus} tidak di temukan")
       
   def veref_(self,username: str) -> bool:
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
     
   def isi(self,nama: str,alamat: str,waktu: str) -> None:
       usr =Ini(nama,alamat,waktu)
       self.tambah(usr)
       acept= Ssimpan.simpan_dta(self.data_base)
       if acept:
          print("data berhasil di simpan")
      
       
   def tampilkan(self):
       if len(self.data_base) ==0:
          print("data masih kosong")
          return
       for z in self.data_base:
           if z.status:
              print(f"{z.nama:<10} | {z.alamat:<10} | {z.gula} | {z.beras} | {z.uang} | {z.dll:<10}")
   
     
def kolom():
    print("1.tambah user")
    print("2.tampilkan data")
    print("3.keluar")
    print("4.update data")
    print("5.hapus data")
    print("6.cari data")
  
  
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

sb =Simpan()
if __name__=="__main__":
   data_s =Data()
   while True:
      kolom()
      pilih_ =vld.pilih()
      if pilih_ ==1:
         nama_ =vld.pertanyaan_1()
         alamat_ =vld.pertanyaan_2()
         beras_ =vld.pertanyaan_4()
         gula_ =vld.pertanyaan_3()
         uang_ =vld.pertanyaan_5()
         dll_ =vld.pertanyaan_6()
         his_time =time(format_wkt)
         data_s.tambah(nama_,alamat_,beras_,gula_,uang_,dll_)
         sb.isi(nama_,alamat_,his_time)
     
      elif pilih_ ==2:
          sb.tampilkan()
     
      elif pilih_ ==3:
           data_s.tutup()
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
      elif pilih_ ==6:
           user_name =vld.pertanyaan_1()
           data_s.luru(user_name)
           
             
        
     
   
        
      
        
        
          
           
           
        
   
     
     
    