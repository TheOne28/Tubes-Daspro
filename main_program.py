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

#Fungsi utamma

def start():
    
    global all_data #array yang mencakup semua data
    filepath = os.path.dirname(__file__)
    file_name = ["user.csv", "gadget.csv", "consumables.csv", "consumable_history.csv", "gadget_borrow_history.csv", "gadget_return_history.csv"]
    parser = argparse.ArgumentParser()

    parser.add_argument("name", nargs = "?", action = "store")
    args = parser.parse_args()
    
    if(args.name == None):
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
                print("Welcome to program")
                
                all_data = f1416.load(args.name)
                main_program()

def main_program():
    global all_data
    choice = ["login", "help"]

    time.sleep(0.5)
    comm = validation.input_validation("string", "\nCommand: ", choice)
    
    time.sleep(0.5)
    while(comm == "help"):
        f1416.help("all")
        comm = validation.input_validation("string", "\nCommand: ", choice)
    else:
        time.sleep(0.5)
        user, id_user = f0102.user_login(all_data[0])
        #Selama belum bisa log in, bakal keluar fungsi login terus
        while(user == "incorrect"):
            time.sleep(0.5)
            
            print("Login ulang")
            user, id_user = f0102.user_login(all_data[0])
   
    while True:     
        if(user == "admin"):
            choices = ["register", "login", "carirarity", "caritahun", "tambahitem", 
            "hapusitem", "ubahjumlah", "riwayatpinjam", "riwayatkembali", "riwayatambil", "save", "help", "exit"]
            command = validation.input_validation("string", "\nCommand: ", choices)
            
            time.sleep(0.5)
            if (command.lower() == "login"):
                time.sleep(0.5)
               
                user, id_user = f0102.user_login(all_data[0])
                while(user == "incorrect"):
                    time.sleep(0.5)
                    print("Login ulang")
                    user, id_user = f0102.user_login(all_data[0])

            elif(command.lower() == "register"):
                print("\n>>register")
                time.sleep(0.5)
                
                all_data[0] = f0102.user_register(all_data[0])
            elif(command.lower() == "carirarity"):
                print("\n>>carirarity")
                time.sleep(0.5)
                
                f0304.find_gadget_rarity(all_data[1])
            elif(command.lower() == "caritahun"):
                print("\n>>caritahun")
                time.sleep(0.5)
                
                f0304.find_gadget_years(all_data[1])
            elif(command.lower() == "tambahitem"):
                print("\n>>tambahitem")
                all_data[1], all_data[2] = f0507.add_item(all_data)
            elif(command.lower() == "hapusitem"):
                print("\n>>hapusitem")
                time.sleep(0.5)
                
                all_data[1], all_data[2] = f0507.remove_item(all_data)
            elif(command.lower() == "ubahjumlah"):
                print("\n>>ubahjumlah")
                all_data[1], all_data[2] = f0507.ubah_jumlah(all_data)
            elif(command.lower() == "riwayatpinjam"):
                print("\n>>riwayatpinjam")
                time.sleep(0.5)
                
                f1113.look_gadget_borrow(all_data)
            elif(command.lower() == "riwayatkembali"):
                print("\n>>riwayatkembali")
                f1113.look_gadget_return(all_data)
            elif(command.lower() == "riwayatambil"):
                print("\n>>riwayatambil")
                time.sleep(0.5)
                
                f1113.look_history_consumables(all_data)
            elif(command.lower() == "save"):
                print("\Saving...")
                time.sleep(0.5)
                
                f1416.save(all_data)
            elif(command.lower() == "exit"):
                print("\n>>Exit")
                time.sleep(0.5)
                
                f1416.exit(all_data)
                break
            else:
                f1416.help(user)
        
        else: 
            choices = ["login", "carirarity", "caritahun", "pinjam", 
            "kembalikan", "minta", "save", "help", "exit"]
            command = validation.input_validation("string", "\nCommand: ", choices)

            if (command.lower() == "login"):
                print("\n>>login")
                time.sleep(0.5)
                
                user, id_user = f0102.user_login(all_data[0])
                while(user == "incorrect"):
                    time.sleep(0.5)

                    print("Login ulang")
                    user, id_user = f0102.user_login(all_data[0])

            elif(command.lower() == "carirarity"):
                print("\n>>carirarity")
                time.sleep(0.5)
                
                f0304.find_gadget_rarity(all_data[1])
            elif(command.lower() == "caritahun"):
                print("\n>>caritahun")
                time.sleep(0.5)
                
                f0304.find_gadget_years(all_data[1])
            elif(command.lower() == "pinjam"):
                print("\n>>pinjam")
                time.sleep(0.5)
                
                all_data[4] = f0810.gadget_borrow(id_user, all_data)
            elif(command.lower() == "kembalikan"):
                print("\n>>kembalikan")
                time.sleep(0.5)
                
                all_data[4], all_data[5] = f0810.return_gadget(id_user, all_data)
            elif(command.lower() == 'minta'):
                print("\n>>minta")
                time.sleep(0.5)
                
                all_data[3] = f0810.req_consumables(id_user, all_data)
            elif(command.lower() == "save"):
                print("\Saving...")
                time.sleep(0.5)
                
                f1416.save(all_data)
            elif(command.lower() == "exit"):
                print("\n>>Exit")
                time.sleep(0.5)
                
                f1416.exit(all_data)
                break
            else:
                f1416.help(user)

if __name__ == "__main__":
    start()

