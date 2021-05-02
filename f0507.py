import validation
import time

#Fungsi 5, 6, dan 7

def add_item(all_data):
    #Asumsi nya bakal di loop terus sampai id valid, jadi cuma ada 2 kemungkinan akhirmya
    #yaitu awalan G atau C 

    id = validation.id_validation()

    if(id[0] == "G"):
        valid = False
        file = all_data[1]
        
        time.sleep(0.5)
        while True:
            found = False
            for data in file:
                if(data[0] == id):
                    found = True
                    print("ID item sudah ada")
                    break
            
            if(not found):
                valid = True
                break
            else:
                time.sleep(0.5)
                
                pilihan = validation.input_validation("string", "Apakah ingin menginput ulang ID? (Y/N)", ["y", "n"])
                if(pilihan.lower() == "y"):
                    id = validation.id_validation()
                else:
                    break

        if(valid):
            #Tidak ada batasan untuk nama dan deskripsi selain uji dasar
            name = validation.input_validation("string", "Masukkan nama: ", [])
            desc = validation.input_validation("string", "Masukkan deskirpsi: ", [])
            jumlah = validation.jumlah_validation()
            rarity = validation.input_validation("string", "Masukkan rarity: ", ["c", "b", "a", "s"])
            
            while True:
                year = validation.input_validation("integer", "Masukkan tahun: ", [])
                if(year <= 0):
                    print("Tahun harus >= 0")
                else:
                    break

            new_gadget = []
            new_gadget.append(id)
            new_gadget.append(name)
            new_gadget.append(desc)
            new_gadget.append(jumlah)
            new_gadget.append(rarity)
            new_gadget.append(year)

            file.append(new_gadget)
            time.sleep(0.5)
            print("\nItem {} berhasil ditambahkan".format(name))
            
        else:
            time.sleep(0.5)
            print("Fungsi memambah item dibatalkan")
        return file, all_data[2]            
    
    elif(id[0] == "C"):
        file = all_data[2]
        valid = False
 
        time.sleep(0.5)
        while True:
            found = False
            for data in file:
                if(data[0] == id):
                    found = True
                    print("ID item sudah ada")
                    break
            
            if(not found):
                valid = True
                break
            else:
                time.sleep(0.5)
                
                pilihan = validation.input_validation("string", "Apakah ingin menginput ulang ID? (Y/N)", ["y", "n"])
                if(pilihan.lower() == "y"):
                    id = validation.id_validation()
                else:
                    break
        
        if(valid):
            #Tidak ada batasan untuk nama dan deskripsi selain uji dasar
            name = validation.input_validation("string", "Masukkan nama: ", [])
            desc = validation.input_validation("string", "Masukkan deskirpsi: ", [])
            jumlah = validation.jumlah_validation()
            rarity = validation.input_validation("string", "Masukkan rarity: ", ["c", "b", "a", "s"])            
                
            new_gadget  = []            
                        
            new_gadget.append(id)
            new_gadget.append(name)
            new_gadget.append(desc)
            new_gadget.append(jumlah)
            new_gadget.append(rarity)

            file.append(new_gadget) 

            time.sleep(0.5)   
            print("\nItem {} berhasil ditambahkan".format(name))

        else:
            time.sleep(0.5)
            print("Fungsi memambah item dibatalkan")    
        return all_data[1], file        

def remove_item(all_data):
    #Asumsi nya bakal di loop terus sampai id valid, jadi cuma ada 2 kemungkinan akhirmya
    #yaitu awalan G atau C
    id = validation.id_validation()
    
    if(id[0] == "G"):
        file = all_data[1]
        borrow = all_data[4]
        dup = file

        while True:
            found = False
            #Proses pencarian gadget
            for data in file:
                if(data[0] == id):
                    
                    time.sleep(0.5)
                    cek = validation.input_validation("string", "\nApakah anda yakin ingin menghapus " + data[1] + " ? (Y/N)", ["y", "n"])
                    found = True

                    #pilihan dijamin sudah berupa y atau n     
                    if(cek.upper() == "Y"):
                        time.sleep(0.5)
                        
                        print("Item {} berhasil dihapus".format(data[1]))
                        file.remove(data)
                        
                        borrowed = False
                        for bor in borrow:
                            if(id == bor[2]):
                                borrowed = True
                                break

                        if(not borrowed):
                           dup.remove(data)
                        break
                    else:
                        break
                
            if(not found):
                print("Item tidak ada")
                time.sleep(0.5)
                
                pilihan = validation.input_validation("string", "Apakah ingin menginput ulang ID? (Y/N)", ["y", "n"])
                if(pilihan.lower() == "y"):
                    id = validation.id_validation()
                else:
                    break
            else:
                break
        
        return file, all_data[2],dup
    
    elif(id[0] == "C"):
        file = all_data[2]
        dup = file
        minta = all_data[3]

        while True:
            found = False
            for data in file:
                if(data[0] == id):
                    
                    time.sleep(0.5)
                    cek = validation.input_validation("string", "\nApakah anda yakin ingin menghapus " + data[1] + " ? (Y/N)", ["y", "n"])
                    found = True
                    
                    #pilihan dijamin sudah berupa y atau n  
                    if(cek.upper() == "Y"):
                        time.sleep(0.5)
                        
                        print("Item {} berhasil dihapus".format(data[1]))
                        file.remove(data)
                        
                        minta = False
                        for mint in minta:
                            if(id == mint[2]):
                                minta = True
                                break

                        if(not minta):
                           dup.remove(data)
                        
                        break
                    else:
                        break
                        
            if(not found):
                print("Item tidak ada")
                
                time.sleep(0.5)
                pilihan = validation.input_validation("string", "Apakah ingin menginput ulang ID? (Y/N)", ["y", "n"])
                if(pilihan.lower() == "y"):
                    id = validation.id_validation()
                else:
                    break
            else:
                break
        
    
        return all_data[1], file, dup

def ubah_jumlah(all_data):
    #Asumsi nya bakal di loop terus sampai id valid, jadi cuma ada 2 kemungkinan akhirmya
    #yaitu awalan G atau C
    id = validation.id_validation()
    
    if(id[0] == "G"):
        file = all_data[1]

        while True:       
            found = False
            jumlah = validation.input_validation("integer", "Masukkan jumlah: ", [])
            for data in file:
                if(data[0] == id):
                    while True:
                        if(data[3] + jumlah < 0):
                            
                            time.sleep(0.5)
                            print("{} ".format(abs(jumlah)) + data[1] + " gagal dibuang karena stok kurang. Stok sekarang : {} (< {})".format(data[3], abs(jumlah)))
                            pilihan = validation.input_validation("string", "Apakah ingin menginput ulang jumlah? (Y/N)", ["y", "n"])
                            
                            #pilihan dijamin sudah berupa y atau n  
                            if(pilihan.lower() == "y"):
                                jumlah = validation.input_validation("integer", "Masukkan jumlah: ", [])
                            else:
                                break
                        else:
                            time.sleep(0.5)
                            data[3] = data[3] + jumlah
                            
                            if(jumlah < 0):
                                print("{} ".format(abs(jumlah)) + data[1] + " berhasil dibuang. Stok sekarang : {}".format(data[3]))
                            else:
                                print("{} ".format(jumlah) + data[1] + " berhasil ditambahkan. Stok sekarang : {} ".format(data[3]))
                            break    
                    
                    found = True  
            
            if(not found):
                print("Item tidak ditemukan")

                time.sleep(0.5)
                pilihan = validation.input_validation("string", "Apakah ingin menginput ulang ID? (Y/N)", ["y", "n"])
                
                #pilihan dijamin sudah berupa y atau n  
                if(pilihan.lower() == "y"):
                    id = validation.id_validation()
                else:
                    break
            else:
                break

        return file, all_data[2]
    
    elif(id[0] == "C"):
        file = all_data[2]

        while True:
            jumlah = validation.input_validation("integer", "Masukkan jumlah: ", []) 
            found = False
            for data in file:
                if(data[0] == id):
                    while True:
                        print(type(data[3]))
                        if(data[3] + jumlah < 0):
                            
                            time.sleep(0.5)
                            print("{} ".format(abs(jumlah)) + data[1] + " gagal dibuang karena stok kurang. Stok sekarnag : {} (< {})".format(data[3], abs(jumlah)))
                            pilihan = validation.input_validation("string", "Apakah ingin menginput ulang jumlah? (Y/N)", ["y", "n"])
                            
                            #pilihan dijamin sudah berupa y atau n 
                            if(pilihan.lower() == "y"):
                                jumlah = validation.input_validation("integer", "Masukkan jumlah: ", [])
                            else:
                                break
                        else:
                            time.sleep(0.5)
                            data[3] = data[3] + jumlah
                            
                            if(jumlah < 0):
                                print("{} ".format(abs(jumlah)) + data[1] + " berhasil dibuang. Stok sekarnag : {}".format(data[3]))
                            else:
                                print("{} ".format(jumlah) + data[1] + " berhasil ditambahkan. Stok sekarnag : {} ".format(data[3]))
                        
                        found = True
            
            if(not found):
                print("Item tidak ditemukan")
                pilihan = validation.input_validation("string", "Apakah ingin menginput ulang ID? (Y/N)", ["y", "n"])
                if(pilihan.lower() == "y"):
                    id = validation.id_validation()
                else:
                    break
            else:
                break
            
        return all_data[1], file
