def pilih():
       while True:
             try:
                 pilih =input("masukan pilihan:").strip()
                 if pilih =="":
                     print("pilihan tidak boleh kosong")
                     continue
                 if not pilih.isdigit():
                     print("pilihan tidak boleh berupa huruf")
                     continue
                 pilih_ =int(pilih)
                 return pilih_
                 
                 
             except Exception as a:
                          print(f"eror:{a}")
                          
                    
def pertanyaan_1():
       while True:
             try:
                 nama =input("masukan nama:").strip().title()
                 if nama.isdigit():
                     print("nama tidak boleh ada unsur huruf")
                     continue
                 if nama =="":
                    print("data tidak boleh kosong!")
                    continue
                   
                 return nama
                 
             except Exception as w:
                     print(f"error:{w}")
def pertanyaan_8():
    while True:
       hapus =input("masukan data nama yang mau di hapus:").title()
       if hapus =="":
          print("pilihan harus di isi!")
          continue
       return hapus
      
def pilih_2():
    while True:
       try:
         pilih_2 =input("pilihlah pilihan di atas:").strip()
         if pilih_2 =="":
            print("data tidak boleh kosong")
            continue
         if pilih_2.isalpha():
            print("pilihan wajib menggunakan angka")
            continue
         return pilih_2
       except Exception as E:
            print(f"error:{E}")
         
def pertanyaan_7():
    while True:
       try:
         new_dta =input("masukan data baru:").strip()
         if new_dta =="":
            return 0
         return new_dta
       except Exception as e:
             print(f"error:{e}")
            
def pertanyaan_6():
    while True:
       try:
         dll =input("apakah ada barang lain?:").strip().title()
         if dll =="":
            input_semen ="data kosong"
            return input_semen
         return dll
       except Exception as e:
            print(f"error:{e}")
      
      
def pertanyaan_5():
       while True:
             try:
                 uang =input("masukan jumlah uang:").strip()
                     
                 if uang.isalpha():
                     print("tidak boleh huruf harus berupa angka!")
                     continue
                     
                 uang_ =int(uang) if uang !="" else 0
                 return uang_
                  
             except Exception as e:
                          print(f"error:{e}")
                                  
def pertanyaan_4():
    while True:
       try:
         beras =input("jumlah beras:").strip()
         if beras.isalpha():
            print("pilihan harus berupa huruf")
            continue
         beras_ =int(beras) if beras !="" else 0
         return beras_
         
         
       except Exception as l:
              print(f"eror:{l}")
          
                          
def pertanyaan_3():
  while True:
    try:
      gula =input("jumlah gula:").strip()
      if gula.isalpha():
         print("input tidak boleh huruf")
         continue
      gula1 =int(gula) if gula !="" else 0
      return gula1
         
        
    except Exception as e:
           print(f"error:{e}")
                           
def pertanyaan_2():
       while True:
             try:
                 alamat =input("alamat:").strip().title()
                 if alamat =="":
                     print("input tidak boleh kosong")
                     continue
                     
                 else: 
                      return alamat
                      
             except  Exception as i:
                           print(f"error:{i}")
                                      
                     
           
                   
       
                    
                   
                  
                  
if __name__ =="__main__":
   pertanyaan_8()
           
              
           