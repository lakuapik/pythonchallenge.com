#!/usr/bin/env python3

'''
    15 Apr 2017 JKT DHE
    davidadi216@gmail.com
    Solusi untuk Level 2 pythonchallenge.com
    http://www.pythonchallenge.com/pc/def/ocr.html
'''

'''
    clue:
        view-source code htmlnya,
        akan melihat :

        <!--
        %%$@_$^ .... bla bla bla --!>

    tugas:
        menemukan karakter langka di dalam data tersebut
'''

#data sudah disimpan di lvl2.txt, tinggal membukanya
data = open('lvl2.txt').read()

#menghitung jumlah karakter yg sama
jumlahKarakter = {}
for karakter in data:
    jumlahKarakter[karakter] = jumlahKarakter.get(karakter, 0)+1

print(jumlahKarakter)
print('\n')

'''
    hasil:
    {'[': 6108, 'i': 1, '+': 6066, '$': 6046, 'l': 1, '{': 6046, '^': 6030, '*': 6034, '!': 6079, 'y': 1, 't': 1, 'a': 1, 'e': 1, '(': 6154, '\n': 1220, '@': 6157, ']': 6152, '_': 6112, '&': 6043, '}': 6105, '#': 6115, 'u': 1, '%': 6104, ')': 6186, 'q': 1}

    karakter langka adalah yang hanya 1 kali;
'''

#print karakter yang hanya tampil 1 kali
for x in jumlahKarakter.keys():
    if jumlahKarakter[x] == 1:
        print(x, end='')

print('\n')

'''
    hasilnya : taeqyuli / laiinya
    tinggal ditebak urutannya menjadi "equality"
'''

'''
    Cara 2: memakai str.isalpha()
    karena pada dasarnya karakter yang langka pada cara pertama adalah huruf alfabet semua
    kita bisa menggunakan str.isalpha() untuk mengecek apakah karakter tersebut adalah huruf alfabet
'''

#print karakter yang merupakan alfabet
for karakter in range(0, len(data)):
    if data[karakter].isalpha():
        print(data[karakter], end ='')

print('\n')

'''
    menggunakan cara kedua langsung menampilkan jawabannya dengan
    urutan karakter yang benar "equality"
'''

'''
    Level 3:
    http://pythonchallenge.com/pc/def/equality.html
'''
