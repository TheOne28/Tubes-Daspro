import time

#Fungsi f03 dan f04
#Untuk bagian ini, input diasumsikan pasti valid

def comparison(operator, first, second):
    #Pengubahan opeator menjadi kondisional
    if(operator == ">"):
        return first > second
    elif(operator == ">="):
        return first >= second
    elif(operator == "<"):
        return first < second
    elif(operator == "<="):
        return first <= second
    else:
        return first == second

def find_gadget_rarity(gadget_file):
    
    rarity = input("Masukkan rarity: ")
    
    found = False
    
    print("Hasil pencarian: ")
    for i in range(len(gadget_file)):
        if(i != 0):
            #Pengecekan gadget yang sesuai
            if(gadget_file[i][4] == rarity):
                time.sleep(0.5)
                
                print("\n")
                print("Nama : " + gadget_file[i][1])
                print("Deskripsi : " + gadget_file[i][2])
                print("Jumlah : " + str(gadget_file[i][3]) + " buah")
                print("Rarity : " + gadget_file[i][4])
                print("Tahun ditemukan : " + str(gadget_file[i][5]))
  
                found = True
                
    if(not found):
        print("Tidak terdapat gadget dengan rarity " + rarity)

def find_gadget_years(gadget_file):
    
    tahun = int(input("Masukkan tahun : "))
    sign = input("Masukkan kategori: ")

    found = False
    print("Hasil pencarian: ")
    
    for i in range(len(gadget_file)):
        if(i != 0):
            #Pengecekan gadget yang sesuai
            if(comparison(sign, gadget_file[i][5], tahun)):
                time.sleep(0.5)

                print("\n")
                print("Nama : " + gadget_file[i][1])
                print("Deskripsi : " + gadget_file[i][2])
                print("Jumlah : " + str(gadget_file[i][3]) + " buah")
                print("Rarity : " + gadget_file[i][4])
                print("Tahun ditemukan : " + str(gadget_file[i][5]))

                found = True    
    
    if(not found):
        print("Tidak terdapat gadget dengan syarat tahun ditemukan " + sign + " " + str(tahun))
