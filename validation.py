#File untuk validasi

def input_validation(type, out, choices):
    while(True):
        if(type == "string"):
            try:
                masukan = input(out)
            except KeyboardInterrupt:
                print("Masukan tidak diterima")
            else:
                if(len(choices) == 0):
                    return masukan
                #Syarat!
                #Isi dari choices harus berupa string kecil semua

                elif(masukan.lower()  in choices):
                    return masukan
                else:
                    print("Pilihan tidak tersedia")
        elif(type == "integer"):
            try:
                masukan = int(input(out))
            except ValueError:
                print("Masukan harus berupa integer")
            except KeyboardInterrupt:
                print("Masukan harus berupa integer")
            else:
                return masukan


def id_validation():
    #Ngecek apakah ada huruf selain huruf pertama
    while (True):
        id = input_validation("string", "Masukkan ID: ", [])
        if(id[0] == "C" or id[0] == "G"):
            valid = True
            for i in range(1, len(id)):
                if(ord(id[i]) < 48 or ord(id[i]) > 57):
                    print("ID tidak valid") 
                    valid = False
                    break
            
            if(valid):
                return id
        else:
            print("ID tidak valid")

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
    while True:
        jumlah = input_validation("integer", "Masukkan jumlah: ", [])

        if(jumlah >= 0):
            return jumlah
        else:
            print("Jumlah harus > 0")