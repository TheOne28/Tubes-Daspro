import os
import convert
import validation

#fungsi f14, f15, dan f16

path = os.path.dirname(__file__)
file_name = ["user.csv", "gadget.csv", "consumables.csv", "consumable_history.csv", "gadget_borrow_history.csv", "gadget_return_history.csv"]

def load(folder):
    
    #Fungsi load disini kupake cuma buat ngeload semua data nya
    #Idenya, semua data dijadiin di satu array di all_data
    all_data = []

    #Asumsi nama file tetap
    for i in range(6):
        all_data.append(convert.open_file("{}\\{}\\{}".format(path, folder, file_name[i]))) 

    return all_data

def save(all_data):
    folder_name = validation.input_validation("string", "Masukkan nama folder penyimpanan: ", [])
 
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
    print("Data berhasil disimpan di folder {}".format((folder_name)))

def help(user):
   
    if(user == "user"):
        #Load gak dimasukin soalnya bukan command yang tersedia
        #Help untuk user
        print("======================= Help =================================")
        print("login - untuk melakukan login ke dalam sistem")
        print("pinjam - untuk melakukan peminjaman pada gadget yang diinginkan")
        print("kembalikan - untuk melakukan pengembalian gadget yang telah dipinjam sebelumnya")
        print("minta - untuk melakukan permintaan consumable")
        print("save - untuk melakukan peenyimpanan data")
        print("exit - untuk keluar dari program")
        print("help - untuk mengeluarkan bantuan dan perintah yang tersedia")

    elif(user == "admin"):
        #Load gak dimasukin soalnya bukan command yang tersedia
        #Help untuk admin
        print("======================= Help =================================")
        print("Register - untuk melakukan register user baru")
        print("login - untuk melakukan login ke dalam sistem")
        print("tambahitem -untuk melakukan penambahan item")
        print("hapusitem - untuk melakukan penghapusan gadget atau consumable dari sistem")
        print("ubahumlah - untuk mengubah jumlah dari gadget atau consumable yang diinginkan pada inventory")
        print("carirarity- untuk melakukan pencarian gadget dengan berdasarkan rarity")
        print("caritahun- untuk melakukan pencarian gadget dengan berdasarkan tahun")
        print("riwayatpinjam - untuk menampilkan riwayat peminjaman gadget")
        print("riwayatkembali - untuk menampilkan riwayat pengembalian gadget")
        print("riwayatambil - untuk menampilkan riwayat pengambilan consumables")
        print("save - untuk melakukan peenyimpanan data")
        print("exit - untuk keluar dari program")
        print("help - untuk mengeluarkan bantuan dan perintah yang tersedia")

    else:
        #Help sebelum login
        print("======================= Help =================================")
        print("login - untuk melakukan login ke dalam sistem")
        print("help - untuk mengeluarkan bantuan dan perintah yang tersedia")

def exit(all_data):
    cek = validation.input_validation("string", "Apakah anda mau melakukan penyimpanan file yang diubah? (Y/N)", ["y", "n"])
    #cek dijamin berupa y atau n
    if(cek.upper() == "Y"):
        save(all_data)
