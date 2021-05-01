import convert
import validation

#Need to discuss
# 1. Kalau misal barang masih dipinjam , perlu di loop input gak?
# 2. Kalau stok tidak mencukupi, loop atau gak
# 3. Asumsi isi is_returned Yes atau No
# 4. Kalau id gak terdaftar gimana
    
def gadget_borrow(id_peminjam, all_data):
    id = validation.id_validation()
    file1 = all_data[4] #Gadget_borrow
    file2 = all_data[1]#Gadget
        
    if(id[0] == "G"):    
        valid = True
        for data in file1:
            #Asumsi gak di loop input
            if(data[0] == id_peminjam and data[1] == id and data[5] == "No"):
                valid = False
                print("Peminjaman barang ini masih dilakukan")
        
        if(valid):
            date = validation.input_validation("string", "Masukkan tanggal peminjaman: ", [])
            date_valid = validation.date_validation(date)
            while(not date_valid):
                print("Masukan tanggal tidak valid")
                date = validation.input_validation("string", "Masukkan tanggal peminjaman: ", [])
                date_valid = validation.date_validation(date)

            jumlah = validation.jumlah_validation()                    
            found = False
            for data in file2:
                if(data[0] == id):
                    found = True
                    if(data[3] >= jumlah):
                        new_history = []
                        #Asumsi id nya diurut dari 1
                        if(len(file1) == 1):
                            new_history.append(1)
                        else:
                            new_history.append(int(file1[len(file1) - 1][0]) + 1 )
                        
                        new_history.append(id_peminjam)
                        new_history.append(id)
                        new_history.append(date)
                        new_history.append(jumlah)
                        new_history.append("No")
                        
                        file1.append(new_history)
                        data[3] -= jumlah

                        print("Item {} (x{}) berhasil dipinjam !".format(data[1], jumlah))
                    else:
                        print("Stok tidak mencukupi")
            if(not found):
                print("ID tidak terdaftar")
    else:
        print("ID tidak valid")
    return file1

def return_gadget(id_user, all_data):
    #Nih keknya agak ngebug wkwkwkwk
    file1 = all_data[4] #Gadget_borrow
    file2 = all_data[1] #Gadget
    file3 = all_data[5] #Gadget_retturn

    borrowed_gadget = [] #Nyimpen gadget
    borrowed_id = [] #Nyimpen id peminjaman
    borrowed_count = [] #Nyimpen jumlah barang yang dipinjam

    for i in range(len(file1)):
        if(i != 0) and (id_user == file1[i][1]):
            borrowed_id.append(file1[i][0])
            borrowed_count.append(file1[i][4])
            
            for data in file2:
                if(data[0] == file1[i][2]):
                    borrowed_gadget.append(data[1])
                    print("{}. {}".format(i,data[1]))
                    break
    
    pinjam = validation.input_validation("integer", "Masukkan nomor peminjaman: ", [])
    
    while(pinjam not in range(1, len(borrowed_gadget) + 1)):
        print("Nomor pinjaman tidak valid")
        pinjam = validation.input_validation("integer", "Masukkan nomor peminjaman: ", [])
    
    date = validation.input_validation("string", "Masukkan tanggal pengembalian: ", [])
    date_valid = validation.date_validation(date)
    
    while(not date_valid):
        print("Masukan tanggal tidak valid")
        date = validation.input_validation("string", "Masukkan tanggal pengembalian: ", [])
        date_valid = validation.date_validation(date)

    #Pengisian gadget_return
    new_return = []
    if(len(file3) == 1):
        new_return.append(1)
    else:
        new_return.append(int(file3[len(file3) - 1][0]) + 1 )
    
    new_return.append(borrowed_id[pinjam - 1])
    new_return.append(date)

    file3.append(new_return)
    
    #Ngubah is_returned
    for data in file1:
        if(data[0] == new_return[1]):
            data[5] = "Yes"
            data[3] += borrowed_count[pinjam - 1]

    print("Iten {}(x{}) berhsil dikembalikan".format(borrowed_gadget[pinjam - 1], borrowed_count[pinjam - 1]))

    return file1, file3    

def req_consumables(id_user, all_data):
    id = validation.id_validation()
    file1 = all_data[3]#Consumable_history
    file2 = all_data[2]#Consumable
    
    if(id[0] == "C"):
        jumlah = validation.jumlah_validation()
        date = validation.input_validation("string", "Masukkan tanggal peminjaman: ", [])
        date_valid = validation.date_validation(date)
    
        while(not date_valid):
            print("Masukan tanggal tidak valid")
            date = validation.input_validation("string", "Masukkan tanggal peminjaman: ", [])
            date_valid = validation.date_validation(date)
        
        found = False            
        for data in file2:
            if(data[0] == id):
                found = True
                if(data[3] >= jumlah):
                    new_history = []
                    #Asumsi id nya diurut dari 1
                    if(len(file1) == 1):
                        new_history.append(1)
                    else:
                        new_history.append(int(file1[len(file1) - 1][0]) + 1 )
                                
                    new_history.append(id_user)
                    new_history.append(id)
                    new_history.append(date)
                    new_history.append(jumlah)

                    file1.append(new_history)
                    data[3] -= jumlah

                    print("Item {} (x{}) berhasil dipinjam !".format(data[1], jumlah))
                #Asumsi jika jumlah gak cukup, program berhenti
                else:
                    print("Stok tidak mencukupi")
        
        if(not found):
            print("ID tidak terdaftar")    
    else:
        print("ID tidak valid")
    
    return file1