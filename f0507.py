import validation

#Need to discuss
#1. Yang menghapus, kalau misal item tidak ada, perlu di loop inputnya gak
#2. Cek sapa tau ada kasus kelewat

#Asumsi buat semua fungsi ini, misal id nya gak ada dan gadget, input nya harus gadget terus
def add_item(all_data):
    #Asumsi nya bakal di loop terus sampai id valid, jadi cuma ada 2 kemungkinan akhirmya
    #yaitu awalan G atau C 
    id = validation.id_validation()

    if(id[0] == "G"):
        valid = False
        file = all_data[1]
        #Bagian ini diubah
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
            year = validation.input_validation("integer", "Masukkan tahun: ", [])
            
            new_gadget = []
            new_gadget.append(id)
            new_gadget.append(name)
            new_gadget.append(desc)
            new_gadget.append(jumlah)
            new_gadget.append(rarity)
            new_gadget.append(year)

            file.append(new_gadget)
            print("Item {} berhasil ditambahkan".format(name))
            
        else:
            print("Fungsi memambah item dibatalkan")
        return file, all_data[2]            
    
    elif(id[0] == "C"):
        file = all_data[2]
        valid = False
        #Bagian ini diubah
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
            print("Item {} berhasil ditambahkan".format(name))

        else:
            print("Fungsi memambah item dibatalkan")    
        return all_data[1], file        

def remove_item(all_data):
    id = validation.id_validation()
    
    if(id[0] == "G"):
        file = all_data[1]
        #Bagian ini kebawah diubah
        while True:
            found = False
            #Proses pencarian gadget
            for data in file:
                if(data[0] == id):

                    cek = validation.input_validation("string", "Apakah anda yakin ingin menghapus " + data[1] + " ? (Y/N)", ["y", "n"])
                    found = True
                    #cek dijamin sudah berupa y atau n    
                    if(cek.upper() == "Y"):
                        file.remove(data)
                        break
                    else:
                        break
                
            if(not found):
                print("Item tidak ada")
                pilihan = validation.input_validation("string", "Apakah ingin menginput ulang ID? (Y/N)", ["y", "n"])
                if(pilihan.lower() == "y"):
                    id = validation.id_validation()
                else:
                    break
            else:
                break
        
        return file, all_data[2]
    
    elif(id[0] == "C"):
        file = all_data[2]
        #Bagian ini kebawah diubah
        while True:
            found = False
            for data in file:
                if(data[0] == id):
            
                    cek = validation.input_validation("string", "Apakah anda yakin ingin menghapus " + data[1] + " ? (Y/N)", ["y", "n"])
                    found = True
                    
                    if(cek.upper() == "Y"):
                        file.remove(data)
                        break
                    else:
                        break
                        
            if(not found):
                print("Item tidak ada")
                pilihan = validation.input_validation("string", "Apakah ingin menginput ulang ID? (Y/N)", ["y", "n"])
                if(pilihan.lower() == "y"):
                    id = validation.id_validation()
                else:
                    break
            else:
                break
        
    
        return all_data[1], file

def ubah_jumlah(all_data):
    id = validation.id_validation()
    
    if(id[0] == "G"):
        file = all_data[1]
        #Gak pakai jumlah validation soalnya bisa < 0
        #Bagian ini ke bawah diubah
        while True:       
            found = False
            jumlah = validation.input_validation("integer", "Masukkan jumlah: ", [])
            for data in file:
                if(data[0] == id):
                    while True:
                        if(data[3] + jumlah < 0):
                            print("{} ".format(abs(jumlah)) + data[1] + " gagal dibuang karena stok kurang. Stok sekarang : {} (< {})".format(data[3], abs(jumlah)))
                            pilihan = validation.input_validation("string", "Apakah ingin menginput ulang jumlah? (Y/N)", ["y", "n"])
                            
                            if(pilihan.lower() == "y"):
                                jumlah = validation.input_validation("integer", "Masukkan jumlah: ", [])
                            else:
                                break
                        else:
                            data[3] = data[3] + jumlah
                            #Perintah format buat modif string, ngisi yang dikurung pake argumen dalem formatnya
                            if(jumlah < 0):
                                print("{} ".format(abs(jumlah)) + data[1] + " berhasil dibuang. Stok sekarang : {}".format(data[3]))
                            else:
                                print("{} ".format(jumlah) + data[1] + " berhasil ditambahkan. Stok sekarang : {} ".format(data[3]))
                            break    
                    
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

        return file, all_data[2]
    
    elif(id[0] == "C"):
        file = all_data[2]
        #Bagian ini ke bawah diubah
        while True:
            jumlah = validation.input_validation("integer", "Masukkan jumlah: ", []) 
            found = False
            for data in file:
                if(data[0] == id):
                    while True:
                        print(type(data[3]))
                        if(data[3] + jumlah < 0):
                            print("{} ".format(abs(jumlah)) + data[1] + " gagal dibuang karena stok kurang. Stok sekarnag : {} (< {})".format(data[3], abs(jumlah)))
                            pilihan = validation.input_validation("string", "Apakah ingin menginput ulang jumlah? (Y/N)", ["y", "n"])
                            
                            if(pilihan.lower() == "y"):
                                jumlah = validation.input_validation("integer", "Masukkan jumlah: ", [])
                            else:
                                break
                        else:
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