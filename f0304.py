import time
#Bagian ini semua input dijamin valid, jadi gak sah input validation, CMIIW

def find_gadget_rarity(gadget_file):
    #Asumsi masukan selalu benar
    rarity = input("Masukkan rarity: ")
    
    found = False

    for i in range(len(gadget_file)):
        if(i != 0):
            if(gadget_file[i][4] == rarity):
                time.sleep(0.5)

                print("Nama : " + gadget_file[i][1])
                print("Deskripsi : " + gadget_file[i][2])
                print("Jumlah : " + str(gadget_file[i][3]) + " buah")
                print("Rarity : " + gadget_file[i][4])
                print("Tahun ditemukan : " + str(gadget_file[i][5]))

                found = True
                
    if(not found):
        print("Tidak terdapat gadget dengan rarity " + rarity)

def find_gadget_years(gadget_file):
    
    #Pakai asumsi di soal, yaitu input selalu benar
    tahun = int(input("Masukkan tahun : "))
    sign = input("Masukkan kategori: ")

    # Bagian ini untuk ngubah inputnya, biar jadi operator, buat fungsi 3 nggak perlu kok, langsung loopnya sama found aja
    op = {'>': (lambda x,y : x > y), '>=' : (lambda x, y: x >= y), '<' : (lambda x, y: x < y), '<=' : (lambda x,y : x <= y), '=' : (lambda x, y: x == y)}
    
    found = False
    print("Hasil pencarian: ")

    for i in range(len(gadget_file)):
        #Untuk i == 0, itu headernya dan gak perlu dicek
        if(i != 0):
            if(op[sign](gadget_file[i][5], tahun)):
                time.sleep(0.5)

                print("Nama : " + gadget_file[i][1])
                print("Deskripsi : " + gadget_file[i][2])
                print("Jumlah : " + str(gadget_file[i][3]) + " buah")
                print("Rarity : " + gadget_file[i][4])
                print("Tahun ditemukan : " + str(gadget_file[i][5]))

                found = True    
    
    if(not found):
        print("Tidak terdapat gadget dengan syarat tahun ditemukan " + sign + " " + str(tahun))
