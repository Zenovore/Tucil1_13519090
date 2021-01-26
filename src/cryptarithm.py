#!/usr/bin/python3

import datetime

konstanta = ['1','0','2','3','4','5','6','7','8','9']
def clean_string(pisang):
    clean=''
    for string in pisang:
        for i in range(len(string)):
            if (string[i] not in clean) and (string[i] != "+") and (string[i] != " "):
                clean += string[i]     
    return clean

def open_file(namafile):
    char = ""
    cek = True
    with open(namafile) as f:
        lines = f.readlines()

    for line in lines :
        line = line.rstrip("\n")
        if (line.startswith('-')) :
            char += " = "
            cek = False
        elif (line == ""):
            char += "\n"
            cek = True
        else:
            if "+" in line :
                line = line.replace("+","")
                char += line 
            else :
                char += line 
                if cek :
                    char += " + "
    return char

def sum_list(lista):
    jumlah = 0
    for i in range(len(lista)-1):
        jumlah += int(lista[i])
    return jumlah

def permutasi(apel): # Kode permutasi untuk mencari semua kemungkinan dari suatu list apel
    if len(apel) == 0:
        yield []
    elif len(apel) == 1:
        yield apel
    else:
        for i in range(len(apel)):
            # Rekursi dilakukan tanpa elemen ke i, sehingga hasil permutasi didapatkan seluruhnya
            for p in permutasi(apel[:i] + apel[i+1:]):
                # Mengeluarkan salah satu hasil permutasi, tanpa keluar dari fungsi
                yield([apel[i]] + p)

# Program Utama
char = open_file('../test/soal.txt')
count = 0
countsoal = 1
for soal in char.strip().splitlines():
# loop untuk setiap soal pada soal.txt
    AdaHasil = False
    apel,hasil = soal.split(" = ")        
    jeruk = apel.split(" + ")
    jeruk.append(hasil)
    count = 0
    begin_time = datetime.datetime.now()
    print("Soal ke ",countsoal)
    countsoal += 1
    if (len(clean_string(jeruk)) <= 10 ):
        for perm in permutasi(konstanta):
        # Melakukan loop terhadap setiap permutasi
            jambu = dict(zip(clean_string(jeruk),perm[:len(clean_string(jeruk))]))
            # Membuat kamus untuk setiap huruf unik, dan menggabungkannya dengan hasil permutasi
            listbaru = []
            cek = True
            for string in jeruk:
            # Proses konversi huruf -> angka
                angka =""
                for i in string:
                    angka += str(jambu[i])
                listbaru.append(angka)
            jumlah = sum_list(listbaru)
            count += 1
            if ((jumlah == int(listbaru[len(listbaru)-1]))) :
            # Pengecekan apakah kemungkinan solusi benar
                for i in range(len(listbaru)):
                    if (int(listbaru[i][0]) == 0):
                    # Mengecek jika huruf pertama pada soal bernilai 0
                        cek = False
                if cek:
                # Mencetak hasilnya pada layar
                    for j in range(len(listbaru)):
                        if (j == len(listbaru)-1):
                            print("-------+")
                        print(jeruk[j]," : ",end="")
                        print(listbaru[j])
                    print("Jumlah Kasus yang diuji : ",count)
                    print("Waktu yang digunakan : ",datetime.datetime.now() - begin_time)
                    print()
                    AdaHasil = True
                    break
    if (not AdaHasil):
        if (int(len(clean_string(jeruk)) > 10)):
            print("Maaf Jumlah Huruf unik lebih dari 10")
            print()
        else:
            print("Tidak ada solusi untuk soal ini")
            print()