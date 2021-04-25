import convert
import validation

def add_item():
    id = input("Masukkan ID: ")
    if(id[0] == "G"):
        valid = validation.id_check(id)
        
        if(valid):
            file = convert.open_file("gadget.csv")
            found = False
            for data in file:
                if(data[0] == id):
                    found = True
                    print("ID item sudah ada")
                    break
            
            if(not found):
                new_gadget = []
                name = input("Masukkan nama: ")
                desc = input("Masukkan deskripsi: ")
                jumlah_valid, jumlah = validation.jumlah_validation()
                
                if(jumlah_valid):
                    rarity = input("Masukkan rarity: ")
                    avaiable_rarity = ["C", "B", "A", "S"]
                    if(rarity in avaiable_rarity):
                        year = input("Masukkan tahun ditemukan: ")

                        new_gadget.append(id)
                        new_gadget.append(name)
                        new_gadget.append(desc)
                        new_gadget.append(jumlah)
                        new_gadget.append(rarity)
                        new_gadget.append(year)

                        file.append(new_gadget)
                    else:
                        print("Rarity tidak sesuai")

    elif(id[0] == "C"):
        valid = validation.id_check(id)
        
        if(valid):
            file = convert.open_file("consumables.csv")
            found = False
            for data in file:
                if(data[0] == id):
                    found = True
                    print("ID item sudah ada")
                    break
            
            if(not found):
                new_gadget = []
                name = input("Masukkan nama: ")
                desc = input("Masukkan deskripsi: ")
                jumlah_valid, jumlah = validation.jumlah_validation()
        
                if(jumlah_valid):
                    rarity = input("Masukkan rarity: ")
                    avaiable_rarity = ["C", "B", "A", "S"]
                    if(rarity in avaiable_rarity):
                        new_gadget.append(id)
                        new_gadget.append(name)
                        new_gadget.append(desc)
                        new_gadget.append(jumlah)
                        new_gadget.append(rarity)

                        file.append(new_gadget)    
                    else:
                        print("Rarity tidak tersedia")
    else:
        print("ID tidak valid")


def remove_item():
    id = input("Masukkan ID item: ")
    if(id[0] == "G"):
        valid = validation.id_check(id)
    
        if(valid):
            file = convert.open_file("gadget.csv")
            found = False
            for data in file:
                if(data[0] == id):
                    found = True
                    cek = input("Apakah anda yakin ingin menghapus " + data[1] + " ? ")
                    if(cek == "Y"):
                        file.remove(data)
                        break
                    elif(cek == "N"):
                        break
                    else:
                        print("Input tidak valid")
                        break
            
            if(not found):
                print("Item tidak ada")
    elif(id[0] == "C"):
        valid = validation.id_check(id)

        if(valid):
            file = convert.open_file("consumables.csv")
            found = False
            for data in file:
                if(data[0] == id):
                    found = True
                    cek = input("Apakah anda yakin ingin menghapus " + data[1]  + " ? ")
                    if(cek == "Y"):
                        file.remove(data)
                        break
                    elif(cek == "N"):
                        break
                    else:
                        print("Input tidak valid")
                        break
            
            if(not found):
                print("Item tidak ada")
    else:
        print("ID tidak valid")

def ubah_jumlah():
    id = input("Masukkan ID item: ")
    if(id[0] == "G"):
        valid = validation.id_check(id)
        
        if(valid):
            file = convert.open_file("gadget.csv")
            jumlah = 0 
            try:
                jumlah = int(input("Masukkan jumlah : "))
            except ValueError:
                print("Jumlah harus berupa bilangan bulat")
            else:
                found = False
                for data in file:
                    if(data[0] == id):
                        found = True
                        if(data[3] + jumlah < 0):
                            print("{} ".format(abs(jumlah)) + data[1] + " gagal dibuang karena stok kurang. Stok sekarnag : {} (< {})".format(data[3], abs(jumlah)))
                        else:
                            data[3] = data[3] + jumlah
                            if(jumlah < 0):
                                print("{} ".format(abs(jumlah)) + data[1] + " berhasil dibuang. Stok sekarnag : {}".format(data[3]))
                            else:
                                 print("{} ".format(jumlah) + data[1] + " berhasil ditambahkan. Stok sekarnag : {} ".format(data[3]))
                
                if(not found):
                    print("Item tidak ditemukan")
    elif(id[0] == "C"):
        valid = validation.id_check(id)
        
        if(valid):
            file = convert.open_file("consumables.csv")
            jumlah = 0 
            try:
                jumlah = int(input("Masukkan jumlah : "))
            except ValueError:
                print("Jumlah harus berupa bilangan bulat")
            else:
                found = False
                for data in file:
                    if(data[0] == id):
                        found = True
                        if(data[3] + jumlah < 0):
                            print("{} ".format(abs(jumlah)) + data[1] + " gagal dibuang karena stok kurang. Stok sekarnag : {} (< {})".format(data[3], abs(jumlah)))
                        else:
                            data[3] = data[3] + jumlah
                            if(jumlah < 0):
                                print("{} ".format(abs(jumlah)) + data[1] + " berhasil dibuang. Stok sekarnag : {}".format(data[3]))
                            else:
                                 print("{} ".format(jumlah) + data[1] + " berhasil ditambahkan. Stok sekarnag : {} ".format(data[3]))
                
                if(not found):
                    print("Item tidak ditemukan")
    else:
        print("ID tidak valid")