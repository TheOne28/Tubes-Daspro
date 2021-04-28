import validation
from datetime import datetime

#Need to discuss
#1. Dalam metode nyari maksimum, ada 2 cara pakai library toordinal atau ngubah pakai string
#2. Diminta menampilkan 5 data berikutnya, kalau data kurang dari 5 gimana? Opsi  tersedia gak?

def find_indx_max(file1):
    indx = 1
    max = file1[1][3]

    #Pakai ngubah string
    #Kelemahan : Lebih ribet programnya dan keknya lebih lama
    #Kelebihan : Tidak ada kemungkinan data terlalu besar
    '''
    for i in range(len(file1)):
        year1 = int(max[6:])
        month1 = int(max[3:6])
        day1 = int(max[0:2])

        year2 = int(file1[i][3][6:])
        month2 = int(file1[i][3][3:6])
        day2 = int(file1[i][3][0:2])

        if(year2 > year1):
            max = file1[i]
            indx = i
        elif(year2 == year1):
            if(month2 > month1):
                max = file1[i]
                indx = i 
            elif(month2 == month1):
                if(day2 > day1):
                    max = file1[i]
                    indx = i
    '''

    #Pakai tooordinak
    #Reference: https://pythontic.com/datetime/date/toordinal , https://www.educative.io/edpresso/how-to-convert-a-string-to-a-date-in-python
    # https://www.w3schools.com/python/python_datetime.asp
    #Kelebihan : Lebih simpel kodenya, lebih cepat (?)
    #Kekurangan: Ada kemungkinan data kebesaran (?)

    for i in range(len(file1)):
        date2 = datetime.strptime(file1[i][3], "%d/%m/%Y")
        date1 = datetime.strptime(max, "%d/%m/%Y")
        if(date2.toordinal() > date1.toordinal()):
            max = file1[i][3]
            indx = i
    
    return indx

def selection_sort(file1, file2, file3):
    sorted = []

    while(len(sorted) < len(file1) or len(sorted) < 10):
        index = find_indx_max(file1)
        raw = file1[index]

        for data in file2:
            if(data[0] == raw[1]):
                raw[1] = data[2]
                break
        
        for data in file3:
            if(data[0] == raw[2]):
                raw[2] = data[1]
        
        sorted.append(raw)
        file1.pop(index)

    return sorted

def look_gadget_borrow(all_data):
    file1 = all_data[4]
    file2 = all_data[0]
    file3 = all_data[1]
    
    sorted = selection_sort(file1, file2, file3)

    if(len(sorted) <= 5):
        for data in sorted:
            print("ID peminjaman: {}".format(data[0]))
            print("Nama pengambil: {}".format(data[1]))
            print("Nama gadget: {}".format(data[2]))
            print("Tanggal peminjaman: {}".format(data[3]))
            print("Jumlah: {}".format(data[4]))
    else:
        for i in range(5):
            print("ID peminjaman: {}".format(sorted[i][0]))
            print("Nama pengambil: {}".format(sorted[i][1]))
            print("Nama gadget: {}".format(sorted[i][2]))
            print("Tanggal peminjaman: {}".format(sorted[i][3]))
            print("Jumlah: {}".format(sorted[i][4]))
            
        cek = validation.input_validation("string", "Apakah anda ingin melihat {} data berikutnya ?(Y/N) ".format(len(sorted) - 5), ["y", "n"])
        if(cek.upper() == "Y"):
            for j in range(5, (len(sorted) - 5)):
                print("ID peminjaman: {}".format(sorted[j][0]))
                print("Nama pengambil: {}".format(sorted[j][1]))
                print("Nama gadget: {}".format(sorted[j][2]))
                print("Tanggal peminjaman: {}".format(sorted[j][3]))
                print("Jumlah: {}".format(sorted[j][4]))
        
def look_gadget_return(all_data):
    file1 = all_data[5]
    file2 = all_data[0]
    file3 = all_data[1]
    
    sorted = selection_sort(file1, file2, file3)

    if(len(sorted) <= 5):
        for data in sorted:
            print("ID pengembalian: {}".format(data[0]))
            print("Nama pengambil: {}".format(data[1]))
            print("Nama gadget: {}".format(data[2]))
            print("Tanggal pengembalian: {}".format(data[3]))
    else:
        for i in range(5):
            print("ID pengembalian: {}".format(sorted[i][0]))
            print("Nama pengambil: {}".format(sorted[i][1]))
            print("Nama gadget: {}".format(sorted[i][2]))
            print("Tanggal pengembalian: {}".format(sorted[i][3]))
            
        cek = validation.input_validation("string", "Apakah anda ingin melihat {} data berikutnya ?(Y/N) ".format(len(sorted) - 5), ["y", "n"])
        if(cek.upper() == "Y"):
            for j in range(5, (len(sorted) - 5)):
                print("ID pengembalian: {}".format(sorted[j][0]))
                print("Nama pengambil: {}".format(sorted[j][1]))
                print("Nama gadget: {}".format(sorted[j][2]))
                print("Tanggal pengembalian: {}".format(sorted[j][3]))
            
def look_history_consumables(all_data):
    file1 = all_data[3]
    file2 = all_data[0]
    file3 = all_data[1]
    
    sorted = selection_sort(file1, file2, file3)

    if(len(sorted) <= 5):
        for data in sorted:
            print("ID pengambilan: {}".format(data[0]))
            print("Nama pengambil: {}".format(data[1]))
            print("Nama Consumable: {}".format(data[2]))
            print("Tanggal pengambilan: {}".format(data[3]))
            print("Jumlah: {}".format(data[4]))
    else:
        for i in range(5):
            print("ID pengambilan: {}".format(sorted[i][0]))
            print("Nama pengambil: {}".format(sorted[i][1]))
            print("Nama Consumables: {}".format(sorted[i][2]))
            print("Tanggal pengambilan: {}".format(sorted[i][3]))
            print("Jumlah: {}".format(sorted[i][4]))
            
        cek = validation.input_validation("string", "Apakah anda ingin melihat {} data berikutnya ?(Y/N) ".format(len(sorted) - 5), ["y", "n"])
        if(cek.upper() == "Y"):
            for j in range(5, (len(sorted) - 5)):
                print("ID pengambilan: {}".format(sorted[j][0]))
                print("Nama pengambil: {}".format(sorted[j][1]))
                print("Nama Consumables: {}".format(sorted[j][2]))
                print("Tanggal pengambilan: {}".format(sorted[j][3]))
                print("Jumlah: {}".format(sorted[j][4]))
                