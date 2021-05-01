import f0102
import f0304 
import f0507
import f0810
import f1113
import f1416 
import argparse
import os
import time
import validation

#Need to discuss
# 1. Kemungkinan yang ada di argparse
# 2. Pesan yang diprint di argparse

#Free to improve
# 1. Tambahin available command 

def start():
    global all_data 
    #Bisa buka link https://note.nkmk.me/en/python-script-file-path/ buat os fungsinya
    filepath = os.path.dirname(__file__)
    file_name = ["user.csv", "gadget.csv", "consumables.csv", "consumable_history.csv", "gadget_borrow_history.csv", "gadget_return_history.csv"]
    parser = argparse.ArgumentParser()

    parser.add_argument("name", nargs = "?", action = "store")
    args = parser.parse_args()
    
    #Aku ganti asumsi buat nyesuaian yang di demo
    #Jadi nama folder yang dimasukkan itu nama folder yang menyimpan file csv nya, dengan syarat filenya itu anak dari folder besarnya
    #folder besarnya nih folder yang ada file pythonnya

    if(args.name == None):
        #Perbaikan pesan biar lebih rapi
        parser.error("Please input folder name first")
    else:
        if not os.path.exists("{}\\{}".format(filepath, args.name)):
            print("Wrong folder, nothing_loaded")
        else:
            complete = True
            for i in range(6):
                if not os.path.exists("{}\\{}\\{}".format(filepath, args.name, file_name[i])):
                    complete = False
            
            if(complete):
                print("Welcome to party sire")
                
                all_data = f1416.load(args.name)
                main_program()

def main_program():
    global all_data
    choice = ["login", "help"]
    comm = validation.input_validation("string", "Command: ", choice)
    
    while(comm == "help"):
        f1416.help("all")
        comm = validation.input_validation("string", "Command: ", choice)
    else:
        user, id_user = f0102.user_login(all_data[0])
        #Selama belum bisa log in, bakal keluar fungsi login terus
        while(user == "incorrect"):
            time.sleep(0.5)
            
            print("Login ulang")
            user, id_user = f0102.user_login(all_data[0])
   
    while True:     
        if(user == "admin"):
            #Available command
            choices = ["register", "login", "carirarity", "caritahun", "tambahitem", 
            "hapusitem", "ubahjumlah", "riwayatpinjam", "riwayatkembali", "riwayatambil", "save", "help", "exit"]
            command = validation.input_validation("string", "Command: ", choices)
            
            #lower gunanya buat ngubah jadi huruf kecil semua
            if (command.lower() == "login"):
                user, id_user = f0102.user_login(all_data[0])
                while(user == "incorrect"):
                    time.sleep(0.5)
                    print("Login ulang")
                    user, id_user = f0102.user_login(all_data[0])

            elif(command.lower() == "register"):
                all_data[0] = f0102.user_register(all_data[0])
            elif(command.lower() == "carirarity"):
                f0304.find_gadget_rarity(all_data[1])
            elif(command.lower() == "caritahun"):
                f0304.find_gadget_years(all_data[1])
            elif(command.lower() == "tambahitem"):
                all_data[1], all_data[2] = f0507.add_item(all_data)
            elif(command.lower() == "hapusitem"):
                all_data[1], all_data[2] = f0507.remove_item(all_data)
            elif(command.lower() == "ubahjumlah"):
                all_data[1], all_data[2] = f0507.ubah_jumlah(all_data)
            elif(command.lower() == "riwayatpinjam"):
                f1113.look_gadget_borrow(all_data)
            elif(command.lower() == "riwayatkembali"):
                f1113.look_gadget_return(all_data)
            elif(command.lower() == "riwayatambil"):
                f1113.look_history_consumables(all_data)
            elif(command.lower() == "save"):
                f1416.save(all_data)
            elif(command.lower() == "exit"):
                f1416.exit(all_data)
                break
            else:
                f1416.help(user)
        
        else: 
            #Available Command
            choices = ["login", "carirarity", "caritahun", "pinjam", 
            "kembalikan", "minta", "save", "help", "exit"]
            command = validation.input_validation("string", "Command: ", choices)

            if (command.lower() == "login"):
                user, id_user = f0102.user_login(all_data[0])
                while(user == "incorrect"):
                    time.sleep(0.5)

                    print("Login ulang")
                    user, id_user = f0102.user_login(all_data[0])

            elif(command.lower() == "carirarity"):
                f0304.find_gadget_rarity(all_data[1])
            elif(command.lower() == "caritahun"):
                f0304.find_gadget_years(all_data[1])
            elif(command.lower() == "pinjam"):
                all_data[4] = f0810.gadget_borrow(id_user, all_data)
            elif(command.lower() == "kembalikan"):
                all_data[4], all_data[5] = f0810.return_gadget(id_user, all_data)
            elif(command.lower() == 'minta'):
                all_data[3] = f0810.req_consumables(id_user, all_data)
            elif(command.lower() == "save"):
                f1416.save(all_data)
            elif(command.lower() == "exit"):
                f1416.exit(all_data)
                break
            else:
                f1416.help(user)

if __name__ == "__main__":
    start()

#function len(x: array of integer) -> integer
#{fungsi untuk menghitung panjang arrray}

#procesudr argparse()
#{Prosedur untuk membaca argumen dari terminal}