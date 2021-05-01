import os
import convert
import validation

#Need to discuss
#1. Dicek lagi urutan filenya, biar gak bingung atau dijelasin di help
#2. Cek lagi asumsi nama filenya

def load():
    #Fungsi load disini kupake cuma buat ngeload semua data nya
    #Idenya, semua data dijadiin di satu array di all_data
    all_data = []

    #Asumsi nama file tetap
    all_data.append(convert.open_file("user.csv")) #All_data[0]
    all_data.append(convert.open_file("gadget.csv"))#All_data[1]
    all_data.append(convert.open_file("consumables.csv"))#All_data[2]
    all_data.append(convert.open_file("consumable_history.csv"))#All_data[3]
    all_data.append(convert.open_file("gadget_borrow_history.csv"))#All_data[4]
    all_data.append(convert.open_file("gadget_return_history.csv"))#All_data[5]

    return all_data

def save(all_data):
    folder_name = validation.input_validation("string", "Masukkan nama folder penyimpanan: ", [])
    path = os.path.dirname(__file__)

    file_name = ["user.csv", "gadget.csv", "consumables.csv", "consumable_history.csv", "gadget_borrow_history.csv", "gadget_return_history.csv"]
    
    while True:
        if not os.path.exists("{}\\{}".format(path, folder_name)):
            try:
                os.makedirs("{}\\{}".format(path, folder_name))
            except OSError:
                print("Nama folder tidak valid")
                folder_name = validation.input_validation("string", "Masukkan nama folder penyimpanan: ", [])
            else:
                break
        else:
            break

    for i in range(6):
        if os.path.exists("{}\\{}\\{}".format(path, folder_name, file_name[i])):
            convert.save_file("{}\\{}\\{}".format(path, folder_name, file_name[i]), all_data[i])
        else:
            convert.create_new("{}\\{}\\{}".format(path, folder_name, file_name[i]), all_data[i])

#Pake punya gilang
def help():
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

def exit(all_data):
    cek = validation.input_validation("string", "Apakah anda mau melakukan penyimpanan file yang diubah? (Y/N)", ["y", "n"])

    if(cek.upper() == "Y"):
        save(all_data)
