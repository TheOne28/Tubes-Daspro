import validation
from datetime import datetime
import time

#Fungsi f11, f12, dan f13

def find_indx_max(file1):
    indx = 0

    if(len(file1[0]) == 3): # Kalau file1 = gadget_return
        jml = 2
    else:
        jml = 3
    max = file1[0][jml]
    
    for i in range(1,len(file1)):
        #Proses pengubahan menjadi ordinal
        date2 = datetime.strptime(file1[i][3], "%d/%m/%Y")
        date1 = datetime.strptime(max, "%d/%m/%Y")
        if(date2.toordinal() > date1.toordinal()):
            max = file1[i][jml]
            indx = i
    
    return indx

def selection_sort(file1, file2, file3, file4):
    #Modified selection sort
    sorted = []
    file1.pop(0)

    while True:
        index = find_indx_max(file1)
        raw = file1[index]

        if(len(raw) != 3): #Kalau file1 berupa gadget borrow atau consumableshistory
            for data in file2:
                if(data[0] == raw[1]):
                    raw[1] = data[2]
                    break
            
            for data in file3:
                if(data[0] == raw[2]):
                    raw[2] = data[1]
        else: # Berupa gadget return
            tanggal = raw[2]
            raw.append(tanggal)

            id_user = 0
            id_gadget = 0
            
            for data in file4:
                if(data[0] == raw[1]):
                    id_user = data[1]
                    id_gadget = data[2]
            
            for data in file2:
                if(data[0] == id_user):
                    raw[1] = data[2]
            
            for data in file3:
                if(data[0] == raw[2]):
                    raw[2] = data[1]
        
        sorted.append(raw)
        file1.pop(index)

        if(len(file1) == 0):
            break
        else:
            if(len(sorted) == 10):
                break
    
    return sorted

def look_gadget_borrow(all_data):
    file1 = all_data[4] #Gadget_borrow
    file2 = all_data[0]#User
    file3 = all_data[1]#Gadget
    
    sorted = selection_sort(file1, file2, file3, []) #Disini file4 gak kepake

    if(len(sorted) <= 5):
        for data in sorted:
            
            time.sleep(0.5)
            print("\n")
            print("ID peminjaman: {}".format(data[0]))
            print("Nama pengambil: {}".format(data[1]))
            print("Nama gadget: {}".format(data[2]))
            print("Tanggal peminjaman: {}".format(data[3]))
            print("Jumlah: {}".format(data[4]))
    else:
        for i in range(5):
            
            time.sleep(0.5)
            print("\n")
            print("ID peminjaman: {}".format(sorted[i][0]))
            print("Nama pengambil: {}".format(sorted[i][1]))
            print("Nama gadget: {}".format(sorted[i][2]))
            print("Tanggal peminjaman: {}".format(sorted[i][3]))
            print("Jumlah: {}".format(sorted[i][4]))
            
        cek = validation.input_validation("string", "Apakah anda ingin melihat {} data berikutnya ?(Y/N) ".format(len(sorted) - 5), ["y", "n"])
        #Cek dijamin berupa y atau n
        if(cek.upper() == "Y"):
            for j in range(5, (len(sorted) - 5)):
                
                time.sleep(0.5)
                print("\n")
                print("ID peminjaman: {}".format(sorted[j][0]))
                print("Nama pengambil: {}".format(sorted[j][1]))
                print("Nama gadget: {}".format(sorted[j][2]))
                print("Tanggal peminjaman: {}".format(sorted[j][3]))
                print("Jumlah: {}".format(sorted[j][4]))
        
def look_gadget_return(all_data):
    file1 = all_data[5]#Gadget_Return
    file2 = all_data[0]#User
    file3 = all_data[1]#Gadget
    file4 = all_data[4]#Gadget_borrow
    
    sorted = selection_sort(file1, file2, file3, file4)

    if(len(sorted) <= 5):
        for data in sorted:
            
            time.sleep(0.5)
            print("\n")
            print("ID pengembalian: {}".format(data[0]))
            print("Nama pengambil: {}".format(data[1]))
            print("Nama gadget: {}".format(data[2]))
            print("Tanggal pengembalian: {}".format(data[3]))
    else:
        for i in range(5):
            
            time.sleep(0.5)
            print("\n")
            print("ID pengembalian: {}".format(sorted[i][0]))
            print("Nama pengambil: {}".format(sorted[i][1]))
            print("Nama gadget: {}".format(sorted[i][2]))
            print("Tanggal pengembalian: {}".format(sorted[i][3]))
            
        cek = validation.input_validation("string", "Apakah anda ingin melihat {} data berikutnya ?(Y/N) ".format(len(sorted) - 5), ["y", "n"])
        #Cek dijamin berupa y atau n
        if(cek.upper() == "Y"):
            for j in range(5, (len(sorted) - 5)):
                
                time.sleep(0.5)
                print("\n")
                print("ID pengembalian: {}".format(sorted[j][0]))
                print("Nama pengambil: {}".format(sorted[j][1]))
                print("Nama gadget: {}".format(sorted[j][2]))
                print("Tanggal pengembalian: {}".format(sorted[j][3]))
            
def look_history_consumables(all_data):
    file1 = all_data[3]#Consumables_histtory
    file2 = all_data[0]#User
    file3 = all_data[1]#Gadget
    
    sorted = selection_sort(file1, file2, file3, [])

    if(len(sorted) <= 5):
        for data in sorted:
            
            time.sleep(0.5)
            print("\n")
            print("ID pengambilan: {}".format(data[0]))
            print("Nama pengambil: {}".format(data[1]))
            print("Nama Consumable: {}".format(data[2]))
            print("Tanggal pengambilan: {}".format(data[3]))
            print("Jumlah: {}".format(data[4]))
    else:
        for i in range(5):
            
            time.sleep(0.5)
            print("\n")
            print("ID pengambilan: {}".format(sorted[i][0]))
            print("Nama pengambil: {}".format(sorted[i][1]))
            print("Nama Consumables: {}".format(sorted[i][2]))
            print("Tanggal pengambilan: {}".format(sorted[i][3]))
            print("Jumlah: {}".format(sorted[i][4]))
            
        cek = validation.input_validation("string", "Apakah anda ingin melihat {} data berikutnya ?(Y/N) ".format(len(sorted) - 5), ["y", "n"])
        #cek dijain y atau n
        if(cek.upper() == "Y"):
            for j in range(5, (len(sorted) - 5)):
                
                time.sleep(0.5)
                print("\n")
                print("ID pengambilan: {}".format(sorted[j][0]))
                print("Nama pengambil: {}".format(sorted[j][1]))
                print("Nama Consumables: {}".format(sorted[j][2]))
                print("Tanggal pengambilan: {}".format(sorted[j][3]))
                print("Jumlah: {}".format(sorted[j][4]))
                