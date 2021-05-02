#fungsi untuk mengubah data menjadi string yang siap untuk disimpan
def array_to_string(need_save):
    new_string = ""
    for data in need_save:
        inside_new = [str(inside) for inside in data ]
        new_string += ";".join(inside_new)
        new_string += "\n"
    return new_string

#Fungsi untuk mengubah isi data, untuk pengecekan dilakukan di programnya nanti langsung
def modify(array, index, colom, new):
    array[index][colom] = new
    return array

def array_to_reality(third_data, name):
    #Asumsi
    #Untuk file user, semuanya string
    #Untuk file gadget, jumlah(3) dan tahun(5) integer
    #Untuk file consumable, jumlah(3) integer
    #Untuk file gadget_borrow jumlah(4) integer
    #Untuk file consumbale history, jumlah(4)

    #Bagian ini yang diubah
    if(name.find("user.csv") != -1):
        return third_data
    else:
        for j in range(len(third_data)):
            if(j != 0):
                if(name.find("gadget.csv") != -1):
                    third_data[j][3] = int(third_data[j][3])
                    third_data[j][5] = int(third_data[j][5])
                elif(name.find("consumables.csv") != -1):
                    third_data[j][3] = int(third_data[j][3])
                elif(name.find("gadget_borrom_history.csv") != -1):
                    third_data[j][4] = int(third_data[j][4])
                elif(name.find("consumables_history.csv") != -1):
                    third_data[j][4] = int(third_data[j][4])
        return third_data

#Ini fungsi yang gunanya ngubah data jadi array, udah kepisah tapi belum diubah jadi integer atau float
def data_to_array(first_data):
    second_data = [first.replace("\n", "") for first in first_data]
    third_data = []

    for datas in second_data:
        separated_data = []
        new_word = ""

        for i in range(len(datas)):
            if(datas[i] != ";"):
                new_word += datas[i]
            else:
                new_word.strip()
                separated_data.append(new_word)
                new_word = ""
        #Ini perlu satu kali append lagi karena word yang terakhir belum masuk        
        new_word.strip()
        separated_data.append(new_word)
        third_data.append(separated_data)

    return third_data

#Ini fungsi yang akan dipanggil di modul lainnya kalau mau mbuka file
def open_file(name):
    #Asumsi x adalah nama file
    file = open(name, "r")
    first_data = file.readlines()
    file.close()
    
    if(first_data[len(first_data) - 1] == []):
        first_data.pop(len(first_data) - 1)
        
    almost_finish_data = data_to_array(first_data)
    finish_data = array_to_reality(almost_finish_data, name)
    return finish_data

def save_file(name, new_file):
    file = open(name, "w")
    ready = array_to_string(new_file)
    file.write(ready)
    file.close()

def create_new(name, new_file):
    file = open(name, "a")
    ready = array_to_string(new_file)
    file.write(ready)
    file.close()