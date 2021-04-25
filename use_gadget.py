import convert
import time

def find_gadget_rarity():
    file = convert.open_file("gadget.csv")
    #Diasumsi masukan selalu benar
    rarity = input("Masukkan rarity: ")
    
    found = False
    for i in range(len(file)):
        if(i != 0):
            if(file[i][4] == rarity):
                time.sleep(0.5)
                found = True
                print("Nama : " + file[i][1])
                print("Deskripsi : " + file[i][2])
                print("Jumlah : " + str(file[i][3]) + " buah")
                print("Rarity : " + file[i][4])
                print("Tahun ditemukan : " + str(file[i][5]))

    if(not found):
        print("Tidak terdapat gadget dengan rarity " + rarity)

def find_gadget_years():
    file = convert.open_file("gadget.csv")
    #Pakai asumsi di soal, yaitu input selalu benar
    tahun = int(input("Masukkan tahun : "))
    sign = input("Masukkan kategori: ")

    # Bagian ini untuk ngubah inputnya, biar jadi operator, buat fungsi 3 nggak perlu kok, langsung loopnya sama found aja
    op = {'>': (lambda x,y : x > y), '>=' : (lambda x, y: x >= y), '<' : (lambda x, y: x < y), '<=' : (lambda x,y : x <= y), '=' : (lambda x, y: x == y)}
    found = False
    for i in range(len(file)):
        #Untuk i == 0, itu headernya dan gak perlu dicek
        if(i != 0):
            if(op[sign](file[i][5], tahun)):
                time.sleep(0.5)
                found = True
                print("Nama : " + file[i][1])
                print("Deskripsi : " + file[i][2])
                print("Jumlah : " + str(file[i][3]) + " buah")
                print("Rarity : " + file[i][4])
                print("Tahun ditemukan : " + str(file[i][5]))
    
    if(not found):
        print("Tidak terdapat gadget dengan syarat tahun ditemukan " + sign + " " + str(tahun))
