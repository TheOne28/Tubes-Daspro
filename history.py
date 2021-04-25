import convert
import validation
    
def gadget_borrow(id_peminjam):
    id = input("Masukkan ID: ")
    if(id[0] == "G"):
        valid = validation.id_check(id)
                
        if(valid):
            file1 = convert.open_file("gadget_borrow_history.csv")
            file2 = convert.open_file("gadget.csv")
            in_valid = True
            for data in file1:
                if(data[0] == id_peminjam and data[1] == id):
                    in_valid = False
                    print("Peminjaman barang ini masih dilakukan")
            if(in_valid):
                date = input("Masukkan tanggal peminjaman: ")
                in_valid = validation.date_validation(date)

                if(not in_valid):
                    print("Masukan tanggal tidak sesuai format")
                else:
                    in_valid, jumlah = validation.jumlah_validation()                    
                    if(in_valid):
                        for data in file2:
                            if(data[0] == id):
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

                                    file1.append(new_history)
                                    data[3] -= jumlah

                                    print("Item {} (x{}) berhasil dipinjam !".format(data[1], jumlah))
                                else:
                                    print("Stok tidak mencukupi")
    else:
        print("ID tidak valid")

def return_gadget(id_pinjam):
    file1 = convert.open_file("gadget_borrow_history.csv")
    file2 = convert.open_file("gadget.csv")
    file3 = convert.open_file("gadget_return_history.csv")
    
    borrowed_gadget = []
    borrowed_id = []
    borrowed_count = []
    for i in range(len(file1)):
        if(i != 0):
            for data in file2:
                if(data[0] == file1[i][2]):
                    print("{}. {}".format(i,data[1]))
                    borrowed_gadget.append(data[i][1])
                    borrowed_id.append(data[0])
                    borrowed_count.append(file1[i][4])
                    break
    pinjam = 0
    in_valid = False
    try:
        pinjam = int(input("Masukkan nomor peminjaman: "))
        if(pinjam) not in range(1, len(borrowed_gadget) + 1):
            print("Nomor pinjaman tidak valid")
            in_valid = True
    except ValueError:
        print("Nomor peminjaman tidak valid")
        in_valid = True
    
    if(not in_valid):
        in_valid = True
        date = input("Masukkan tanggal pengembalian: ")
        in_valid = validation.date_validation(date)

        if(in_valid):
            new_return = []
            if(len(file3) == 1):
                new_return.append(1)
            else:
                new_return.append(int(file3[len(file3) - 1][0]) + 1 )
            new_return.append(id_pinjam)
            new_return.append(borrowed_id[pinjam - 1])
            new_return.append(date)

            file3.append(new_return)
            print("Iten {}(x{}) berhsil dikembalikan".format(borrowed_gadget[pinjam - 1], borrowed_count[pinjam - 1]))
        else:
            print("Masukan tanggal pengembalian tidak valid")

def req_consumables(id_pengambil):
    id = input("Masukkan ID: ")
    if(id[0] == "C"):
        valid = validation.id_check(id)
        
        if(valid):
            in_valid, jumlah = validation.jumlah_validation()
            
            if(in_valid) :
                date = input("Masukkan tanggal permintaan: ")
                in_valid = validation.date_validation(date)

                if(in_valid):
                    file1 = convert.open_file("consumables_history.csv")
                    file2 = convert.open_file("consumables.csv")
                    for data in file2:
                        if(data[0] == id):
                            if(data[3] >= jumlah):
                                new_history = []
                                #Asumsi id nya diurut dari 1
                                if(len(file1) == 1):
                                    new_history.append(1)
                                else:
                                    new_history.append(int(file1[len(file1) - 1][0]) + 1 )
                                new_history.append(id_pengambil)
                                new_history.append(id)
                                new_history.append(date)
                                new_history.append(jumlah)

                                file1.append(new_history)
                                data[3] -= jumlah

                                print("Item {} (x{}) berhasil dipinjam !".format(data[1], jumlah))
                            else:
                                print("Stok tidak mencukupi")
    else:
        print("ID tidak valid")