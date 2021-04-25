#File untuk validasi

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

