#!/usr/bin/env python3

import re
import requests

'''
    clue:
        ada gambar lilin kecil diapit oleh 3 lilin besar di kanan dan kirinya
        kalau dilihat dari judulnya 're' menunjukkan kita harus melakukan regex

    tugas:
        cari huruf kecil yang diapit HARUS oleh 3 huruf kapital

    *pastikan konek internet untuk eksekusi file python ini
    *bantuan untuk simulasi regex realtime: https://regexr.com
'''

# ambil text tantangan
url = 'http://www.pythonchallenge.com/pc/def/equality.html'
html = requests.get(url).content
text = re.findall(r'<\!\-\-\n((.|\n)*)\-\-\>', html.decode('utf-8'))[0][0]
text = text.replace('\n', '')

# solusi
result = re.findall(r'[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]', text)
print(''.join(result)) # linkedlist

'''
    penjelasan regex [a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]
    [a-z] adalah semua karakter a-z kecil
    [A-Z] adalah semua karakter A-Z kapital
    [A-Z]{3} adalah semua karakter A-Z kapital beturut-turut selama 3 kali
    kalau di baca semuanya maka: [1kecil][3kapital][1kecil][3kapital][1kecil]
    kenapa ada [1kecil] mengampit? karena HARUS diapit 3 kapital
'''

'''
    Lanjut Level 4:
    http://pythonchallenge.com/pc/def/linkedlist.html
'''
