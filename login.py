import convert
import time

log_as = "" 

def user_login():
    admin = True
    success = False
    user_file = convert.open_file("user.csv")
    
    #Fungsi login
    print(">>login ")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    time.sleep(0.5)
    print("Loading")
    found = False
    time.sleep(0.5)
    for data in user_file:
        if(data[1] == username):
            if(data[4] == password):
                if(data[5] == "admin"):
                    print("Welcome admin")
                    print("Currently log in as admin")
                else:
                    log_as = data[2]
                    print("Welcome " + log_as)
                    print("Currently log in as " + log_as)
                    admin = False 
                success = True            
            else:
                print("Password salah")
            found = True
            break

    if(not found):
        time.sleep(0.5)
        print("Username belum terdaftar")
    
    return admin, success

def user_register():
    user_file = convert.open_file("user.csv")
    print(">>Register")
    name = input("Masukkan nama: ")
    username = input("Masukkan username: ")
    
    while(True):
        print("Validating username\nPlease wait")
        time.sleep(0.5)
        check = False
        
        for data in user_file:
            if(data[1] == username):
                print("User already registered.")
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
    print("User registered succesfully!")

def get_username():
    return log_as

