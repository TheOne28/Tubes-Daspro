import time
import validation

#Need to discuss
#1. Pesan pas log in nya (desain ui)
#2. Cek yang asumsi-asumsi
#3. Penempatan sleepnya
#4. Coba cek lagi sapa tau ada case yang aku kelewat

def user_login(user_file):
    
    #Fungsi login
    print(">>login ")

    username = validation.input_validation("string", "Masukkan Username: ", [])
    password = validation.input_validation("string", "Masukkan Password: ", [])
    
    time.sleep(0.5)
    print("Loading")
    
    time.sleep(0.5)
    
    for data in user_file:
        if(data[1] == username) and (data[4] == password ):
            if(data[5] == "admin"):
                print("Welcome admin")
                print("Currently log in as admin")
                return "admin", data[0]
            else:
                print("Welcome " + data[2])
                print("Currently log in as " + data[2])
                return "user", data[0]
        
        elif(data[1] == username):
            print("Password salah")
            return "incorrect", ""
    
    time.sleep(0.5)
    print("Username belum terdaftar")
    return "incorrect", ""
    
    
def user_register(user_file):

    print(">>Register")
    name = validation.input_validation("string", "Masukkan nama: ", [])
    username = validation.input_validation("string", "Masukkan username: ", [])
    
    while(True):
        print("Validating username\nPlease wait")
        time.sleep(0.5)
        check = False
        #Ngecek username dah ada belum        
        for data in user_file:
            if(data[1] == username):
                print("User already registered.")
                print("Silahkan masukkan username lain")
                check = True
                break

        if(check):
            username = validation.input_validation("string", "Masukkan username: ", [])
        else:
            break

    #Asumsi tidak ada batasann untuk alamat dan password    
    password = validation.input_validation("string", "Masukkan password: ", [])
    address = validation.input_validation("string", "Masukkan alamat: ", [])

    time.sleep(0.5)    
    
    new_user = []
    #Asumsi user_id nya urut dari 1 , gak da tambahan depannya
    user_id = int(user_file[len(user_file) - 1][0]) + 1
    
    new_user.append(user_id)
    new_user.append(username)
    new_user.append(name)
    new_user.append(address)
    new_user.append(password)
    new_user.append("user")

    user_file.append(new_user) 
        
    time.sleep(0.5)
    print("User registered succesfully!")
    return user_file
