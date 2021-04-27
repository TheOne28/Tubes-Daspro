import convert
import time
import csv
import argparse
Username_admin = ["Eren2020"]
Password_admin = ["damedame123"]
log_as = "" 

def procedure_menu() :
    print("Daftar Menu pilihan : ")
    print("--------------------------------------------------------")
    print("1. Register akun ")
    print("2. Pencarian gadget berdasarkan rarity ")
    print("3. Pencarian gadget berdasarkan tahun ditemukan ")
    print("4. Tambah item ")
    print("5. hapus Gadget atau Consumable ")
    print("6. Mengubah Jumlah Gadget atau Consumable pada Inventory ")
    print("7. Meminjam gadget ")
    print("8. Mengembalikan gadget ")
    print("9. Meminta consumable ")
    print("10. Melihat Riwayat Peminjaman Gadget ")
    print("11. Melihat Riwayat Pengembalian Gadget ")
    print("12. Melihat riwayat pengambilan consumable ")
    print("13. Help")
    print("14. Exit")
    print("--------------------------------------------------------")
    
def procedure_kesempatan_login():
    print("Maaf sepertinya anda bukan user/admin")
    print("---------------------------------------------------------")
    print("Kesempatan login anda habis")

def Help():
    print("======================= Help =================================")
    print("Register - untuk melakukan register user baru")
    print("login - untuk melakukan login ke dalam sistem")
    print("tambah item -untuk melakukan penambahan item")
    print("Pencarian gadget berdasarkan rarity - untuk melakukan pencarian gadget dengan berdasarkan rarity")
    print("Pencarian gadget berdasarkan tahun - untuk melakukan pencarian gadget dengan berdasarkan tahun")
    print("Hapus gadget atau consumabke - untuk melakukan penghapusan gadget atau consumable dari sistem")
    print("Mengubah jumlah gadget atau consumable pada inventory - untuk mengubah jumlah dari gadget atau consumable yang diinginkan pada inventory")
    print("Meminjam gadget - untuk melakukan peminjaman pada gadget yang diinginkan")
    print("Mengembalikan gadget - untuk melakukan pengembalian gadget yang telah dipinjam sebelumnya")
    print("Meminta consumable - untuk melakukan permintaan consumable")
    
def load_data()
  if __name__ == "__main__" :
    parser = argparse.ArgumentParser(description="Masukkan nama folder")
    parser.add_argument(nama_folder, type=str, help="nama folder")
    args = parser.parse_args()
    print("loading")
    time.sleep(0.5)
    for folder in new_folder :
      if nama_folder == new_folder :
        print("Selamat datang di kantong Ajaib")
      else :
        print("Maaf file tidak ada")
        
def save_data():
    user_file = convert.open_file("user.csv")
    folder_penyimpanan = input("Masukkan nama folder penyimpanan : ") 
    new_folder = []
    new_folder.append(folder_penyimpanan)
    new_folder.append(user_file)
    print("Saving...")
    time.sleep(1)
    print("Data telah tersimpan pada folder ", folder_penyimpanan)

def id_check(id):
    valid = True
    for i in range(1, len(id)):
        if(ord(id[i]) < 48 or ord(id[i]) > 57):
            valid = False
            print("ID tidak valid") 
            break    
    return valid

def date_validation(date):
    in_valid = True
    for i in range(len(date)):
        if(i == 2 or i == 5 ):
            if(date[i] != "/"):
                in_valid = False
                break
            else:
                if(ord(date[i]) < 48 or ord(date[i] )> 57):
                    in_valid = False
                    break
                
    if(in_valid):
        month = int(date[3:5])
        if(month > 12):
            in_valid = False
        else:
            day31 = ["1","3","5", "7", "8", "10", "12"]
            day = int(date[0:2])
            if(month in day31):
                if(day > 31):
                    in_valid = False
                elif(month == 2):
                    year = int(date[6:10])
                    if(year % 400 == 0 or ((year % 100 != 0) and (year % 4 == 0))):
                        if(day > 29):
                            in_valid = False
                        else:
                            if(day > 28):
                                in_valid = False
                    else:
                        if(day > 30):
                            in_valid = False

    return in_valid

def jumlah_validation():
    jumlah_valid = True
    try:
        jumlah = int(input("Masukkan jumlah: "))
        if(jumlah < 0):
            jumlah_valid = False
            jumlah = 0
            print("Jumlah barang harus >= 0")
    except ValueError:
        jumlah_valid = False
        jumlah = 0
        print("Jumlah harus berupa bilangan bulat")
    return jumlah_valid, jumlah

def user_login(username, password):
    admin = True
    success = False
    user_file = convert.open_file("user.csv")
    
    #Fungsi login
    for i in range(3):
        print("------------------------------------------------------------")
        print(">>login ")
        time.sleep(0.5)
        print("Loading")
        found = False
        time.sleep(0.5)
        for data in user_file:
            if(data[1] == username):
                if(data[4] == password):
                    if(data[5] == "admin"):
                        print("Selamat datang admin",)
                        print("Currently log in as admin")
                        break
                    else:
                        log_as = data[2]
                        print("Welcome ", log_as)
                        print("Currently log in as ", log_as)
                        admin = False
                        break
                    succes == True
                else:
                    if i < 2 :
                        time.sleep(0.5)
                        print("Password salah")
                    else :
                        rocedure_kesempatan_login()
                        quit
                found = True
                break

        if(not found):
            if i < 2 :
                time.sleep(0.5)
                print("Username belum terdaftar")
            else :
                procedure_kesempatan_login()
                quit
    
    return admin, success

def user_register():
    user_file = convert.open_file("user.csv")
    print(">>Register")
    name = input("Masukkan nama: ")
    username = input("Masukkan username: ")
    
    while(True):
        print("Tunggu sebentar, kami sedang memvalidasi username")
        time.sleep(0.5)
        check = False
        
        for data in user_file:
            if(data[1] == username):
                print("Username sudah dipakai")
                print("Silahkan masukkan username lain")
                check = True
                break
        if(check):
            username = input("Masukkan username: ")
        else:
            break
        
    password = input("Masukkan password: ")
    address = input("Masukkan alamat: ") 

    time.sleep(0.5)    
    
    new_user = []
    user_id = int(user_file[len(user_file) - 1][0]) + 1
    new_user.append(user_id)
    new_user.append(username)
    new_user.append(name)
    new_user.append(address)
    new_user.append(password)
    new_user.append("user")

    user_file.append(new_user) 
    user_ready = convert.array_to_string(user_file)
    convert.save_file("user.csv", user_ready)            
        
    time.sleep(0.5)
    print("User berhasil diregister !")    
    
def get_username():
    return log_as

def find_gadget_rarity():
    file = convert.open_file("gadget.csv")
    #Diasumsi masukan selalu benar
    rarity = input("Masukkan rarity: ")
    
    found = False
    for i in range(len(file)):
        if(i != 0):
            if(file[i][4] == rarity):
                time.sleep(0.5)
                found = True
                print("Nama : " + file[i][1])
                print("Deskripsi : " + file[i][2])
                print("Jumlah : " + str(file[i][3]) + " buah")
                print("Rarity : " + file[i][4])
                print("Tahun ditemukan : " + str(file[i][5]))

    if(not found):
        print("Tidak terdapat gadget dengan rarity " + rarity)

def find_gadget_years():
    file = convert.open_file("gadget.csv")
    #Pakai asumsi di soal, yaitu input selalu benar
    tahun = int(input("Masukkan tahun : "))
    sign = input("Masukkan kategori: ")

    # Bagian ini untuk ngubah inputnya, biar jadi operator, buat fungsi 3 nggak perlu kok, langsung loopnya sama found aja
    op = {'>': (lambda x,y : x > y), '>=' : (lambda x, y: x >= y), '<' : (lambda x, y: x < y), '<=' : (lambda x,y : x <= y), '=' : (lambda x, y: x == y)}
    found = False
    for i in range(len(file)):
        #Untuk i == 0, itu headernya dan gak perlu dicek
        if(i != 0):
            if(op[sign](file[i][5], tahun)):
                time.sleep(0.5)
                found = True
                print("Nama : " + file[i][1])
                print("Deskripsi : " + file[i][2])
                print("Jumlah : " + str(file[i][3]) + " buah")
                print("Rarity : " + file[i][4])
                print("Tahun ditemukan : " + str(file[i][5]))
    
    if(not found):
        print("Tidak terdapat gadget dengan syarat tahun ditemukan " + sign + " " + str(tahun))
    
def add_item():
    ID = input("Masukkan ID: ")
    if(ID[0] == "G"):
        valid = validation.id_check(ID)
        
        if(valid):
            file = convert.open_file("gadget.csv")
            found = False
            for data in file:
                if(data[0] == ID):
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

                        new_gadget.append(ID)
                        new_gadget.append(name)
                        new_gadget.append(desc)
                        new_gadget.append(jumlah)
                        new_gadget.append(rarity)
                        new_gadget.append(year)

                        file.append(new_gadget)
                    else:
                        print("Rarity tidak sesuai")

    elif(ID[0] == "C"):
        valid = validation.id_check(ID)
        
        if(valid):
            file = convert.open_file("consumables.csv")
            found = False
            for data in file:
                if(data[0] == ID):
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
                        new_gadget.append(ID)
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
    ID = input("Masukkan ID item: ")
    if(ID[0] == "G"):
        valid = validation.id_check(ID)
    
        if(valid):
            file = convert.open_file("gadget.csv")
            found = False
            for data in file:
                if(data[0] == ID):
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
    elif(ID[0] == "C"):
        valid = validation.id_check(ID)

        if(valid):
            file = convert.open_file("consumables.csv")
            found = False
            for data in file:
                if(data[0] == ID):
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
    ID = input("Masukkan ID item: ")
    if(ID[0] == "G"):
        valid = validation.id_check(ID)
        
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
                    if(data[0] == ID):
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
    elif(ID[0] == "C"):
        valid = validation.id_check(ID)
        
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
                    if(data[0] == ID):
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

def gadget_borrow(id_peminjam):
    ID = input("Masukkan ID : ")
    if(ID[0] == "G"):
        valid = validation.id_check(ID)
                
        if(valid):
            file1 = convert.open_file("gadget_borrow_history.csv")
            file2 = convert.open_file("gadget.csv")
            in_valid = True
            for data in file1:
                if(data[1] == id_peminjam and data[2] == ID):
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
                            if(data[0] == ID):
                                if(data[3] >= jumlah):
                                    new_history = []
                                    #Asumsi id nya diurut dari 1
                                    if(len(file1) == 1):
                                        new_history.append(1)
                                    else:
                                        new_history.append(int(file1[len(file1) - 1][0]) + 1 )
                                    new_history.append(id_peminjam)
                                    new_history.append(ID)
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
    ID = input("Masukkan ID: ")
    if(ID[0] == "C"):
        valid = validation.id_check(ID)
        
        if(valid):
            in_valid, jumlah = validation.jumlah_validation()
            
            if(in_valid) :
                date = input("Masukkan tanggal permintaan: ")
                in_valid = validation.date_validation(date)

                if(in_valid):
                    file1 = convert.open_file("consumables_history.csv")
                    file2 = convert.open_file("consumables.csv")
                    for data in file2:
                        if(data[0] == ID):
                            if(data[3] >= jumlah):
                                new_history = []
                                #Asumsi id nya diurut dari 1
                                if(len(file1) == 1):
                                    new_history.append(1)
                                else:
                                    new_history.append(int(file1[len(file1) - 1][0]) + 1 )
                                new_history.append(id_pengambil)
                                new_history.append(ID)
                                new_history.append(date)
                                new_history.append(jumlah)

                                file1.append(new_history)
                                data[3] -= jumlah

                                print("Item {} (x{}) berhasil dipinjam !".format(data[1], jumlah))
                            else:
                                print("Stok tidak mencukupi")
    else:
        print("ID tidak valid")

def find_indx_max(file1):
    indx = 1
    max = file1[1][3]
    
    #dd/mm/yyyy
    for i in range(len(file1)):
        year1 = int(max[6:])
        month1 = int(max[3:6])
        day1 = int(max[0:2])

        year2 = int(file1[i][3][6:])
        month2 = int(file1[i][3][3:6])
        day2 = int(file1[i][3][0:2])

        if(year2 > year1):
            max = file1[i]
            indx = i
        elif(year2 == year1):
            if(month2 > month1):
                max = file1[i]
                indx = i 
            elif(month2 == month1):
                if(day2 > day1):
                    max = file1[i]
                    indx = i

    return indx

def selection_sort(file1, file2, file3):
    sorted = []

    while(len(sorted) < len(file1) or len(sorted) < 10):
        index = find_indx_max(file1)
        raw = file1[index]

        for data in file2:
            if(data[0] == raw[1]):
                raw[1] = data[2]
                break
        
        for data in file3:
            if(data[0] == raw[2]):
                raw[2] = data[1]
        
        sorted.append(raw)
        file1.pop(index)

    return sorted
    
def look_gadget_borrow():
    file1 = convert.open_file("gadget_borrow_history.csv")
    file2 = convert.open_file("user.csv")
    file3 = convert.open_file("gadget.csv")
    
    sorted = selection_sort(file1, file2, file3)

    if(len(sorted) <= 5):
        for data in sorted:
            print("ID peminjaman: {}".format(data[0]))
            print("Nama pengambil: {}".format(data[1]))
            print("Nama gadget: {}".format(data[2]))
            print("Tanggal peminjaman: {}".format(data[3]))
            print("Jumlah: {}".format(data[4]))
    else:
        for i in range(5):
            print("ID peminjaman: {}".format(sorted[i][0]))
            print("Nama pengambil: {}".format(sorted[i][1]))
            print("Nama gadget: {}".format(sorted[i][2]))
            print("Tanggal peminjaman: {}".format(sorted[i][3]))
            print("Jumlah: {}".format(sorted[i][4]))
            
            while(True):
                cek = input("Apakah anda ingin melihat 5 data berikutnya ? ")
                if(cek == "Y"):
                    for j in range(5, 10):
                        print("ID peminjaman: {}".format(sorted[j][0]))
                        print("Nama pengambil: {}".format(sorted[j][1]))
                        print("Nama gadget: {}".format(sorted[j][2]))
                        print("Tanggal peminjaman: {}".format(sorted[j][3]))
                        print("Jumlah: {}".format(sorted[j][4]))
                    break
                elif(cek == "N"):
                    break
                else:    
                    print("Input tidak valid")

def look_gadget_return():
    file1 = convert.open_file("gadget_return_history.csv")
    file2 = convert.open_file("user.csv")
    file3 = convert.open_file("gadget.csv")
    
    sorted = selection_sort(file1, file2, file3)

    if(len(sorted) <= 5):
        for data in sorted:
            print("ID pengembalian: {}".format(data[0]))
            print("Nama pengambil: {}".format(data[1]))
            print("Nama gadget: {}".format(data[2]))
            print("Tanggal pengembalian: {}".format(data[3]))
    else:
        for i in range(5):
            print("ID pengembalian: {}".format(sorted[i][0]))
            print("Nama pengambil: {}".format(sorted[i][1]))
            print("Nama gadget: {}".format(sorted[i][2]))
            print("Tanggal pengembalian: {}".format(sorted[i][3]))
            
            while(True):
                cek = input("Apakah anda ingin melihat 5 data berikutnya ? ")
                if(cek == "Y"):
                    for j in range(5, 10):
                        print("ID pengembalian: {}".format(sorted[j][0]))
                        print("Nama pengambil: {}".format(sorted[j][1]))
                        print("Nama gadget: {}".format(sorted[j][2]))
                        print("Tanggal pengembalian: {}".format(sorted[j][3]))
                    break
                elif(cek == "N"):
                    break
                else:    
                    print("Input tidak valid")

def look_history_consumables():
    file1 = convert.open_file("consumable_history.csv")
    file2 = convert.open_file("user.csv")
    file3 = convert.open_file("consumables.csv")
    
    sorted = selection_sort(file1, file2, file3)

    if(len(sorted) <= 5):
        for data in sorted:
            print("ID pengambilan: {}".format(data[0]))
            print("Nama pengambil: {}".format(data[1]))
            print("Nama Consumable: {}".format(data[2]))
            print("Tanggal pengambilan: {}".format(data[3]))
            print("Jumlah: {}".format(data[4]))
    else:
        for i in range(5):
            print("ID pengambilan: {}".format(sorted[i][0]))
            print("Nama pengambil: {}".format(sorted[i][1]))
            print("Nama Consumables: {}".format(sorted[i][2]))
            print("Tanggal pengambilan: {}".format(sorted[i][3]))
            print("Jumlah: {}".format(sorted[i][4]))
            
            while(True):
                cek = input("Apakah anda ingin melihat 5 data berikutnya ? ")
                if(cek == "Y"):
                    for j in range(5, 10):
                        print("ID pengambilan: {}".format(sorted[j][0]))
                        print("Nama pengambil: {}".format(sorted[j][1]))
                        print("Nama Consumables: {}".format(sorted[j][2]))
                        print("Tanggal pengambilan: {}".format(sorted[j][3]))
                        print("Jumlah: {}".format(sorted[j][4]))
                    break
                elif(cek == "N"):
                    break
                else:    
                    print("Input tidak valid")


load_data()
print("------------------------------------------------------------")
print("Selamat datang di sistem inventarisasi gadget dan consumable")
print("------------------------------------------------------------")
print("silahkan login terlebih dahulu")
username = input("Masukkan username: ")
password = input("Masukkan password: ")
user_login(username, password)
procedure_menu()
pilih = int(input("Pilih menu : "))
if pilih == 1 :
    if admin == True :
        user_register()
    else :
        print("Maaf anda bukan admin")
elif pilih == 2 :
    find_gadget_rarity()
elif pilih == 3 :
    find_gadget_years()
elif pilih == 4 :
    if admin == True :
        add_item()
    else :
        print("Maaf anda bukan admin")
elif pilih == 5 :
    if admin == True :
        remove_item()
    else :
        print("Maaf anda bukan admin")
elif pilih == 6 :
    if admin == True :
        ubah_jumlah()
    else :
        print("Maaf anda bukan admin")
elif pilih == 7 :
    if admin == False :
        ID_peminjam = user_id
        gadget_borrow(ID_peminjam)
    else :
        print("Maaf admin tidak bisa meminjam barang")
elif pilih == 8 :
    if admin == False :
        id_pinjam = 
        return_gadget(id_pinjam)
    else :
        print("Maaf admin tidak bisa mengembalikan barang")
elif pilih == 9 :
    if admin == False :
        id_pengambil = user_id
        req_consumables(id_pengambil)
    else :
        print("Maaf admin tidak bisa meminta consumable")
elif pilih == 10 :
    if admin == True :
        look_gadget_borrow()
    else :
        print("Maaf anda bukan admin")
elif pilih == 11:
    if admin == True :
        look_gadget_return()
    else :
        print("Maaf anda bukan admin")
elif pilih == 12 :
    if admin == True :
        look_history_consumables()
    else :
        print("Maaf anda bukan admin")
elif pilih == 13 :
    
    
    
        
        
        
                
            
                    
                
                
        
