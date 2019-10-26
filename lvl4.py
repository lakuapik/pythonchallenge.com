#!/usr/bin/env python3

import re
import requests

'''
    clue:
        ada gambar patung yang mengarah ke
        http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345
        dan ketika di kunjungi, ada teks
        `the next nothing is blablabla` *blablabla adalah angka
        ketika dikunjungi, keluar hal yang sama, dan seterusnya
        kalau di lihat source code htmlnya, ada info bahwa
        400 kali percobaan sudah lebih dari cukup

    tugas:
        ikuti nothing sampai ke ujung halaman

    *pastikan konek internet untuk eksekusi file python ini
'''

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
nothing = '12345'

'''
    harus sabar,

    percbobaan 1: range(1, 100)
        di tengah jalan ditemukan teks baru: `Yes. Divide by two and keep going.`
        maka ketika hit html = `Yes. Divide by two and keep going.`
        angka nothing dibagi 2 dan lanjut

    percobaan 2: range(1, 200)
        ditengah jalan ditemukan teks baru
        `There maybe misleading numbers in the text. One example is 82683.
        Look only for the next nothing and the next nothing is 63579`
        jadi kita harus bener2 check regexnya angka nothing berada
        setelah kata `nothing is`

    percobaan 3: range(1, 400)
        di akhir ditemukan teks baru `peak.html`
        dan itulah jawabannya, tapi script error

    percobaan 4: while True
'''

# for i in range(1, 100):
# for i in range(1, 200):
# for i in range(1, 400):
while True:

    html = requests.get(url+str(nothing)).content.decode('utf-8')
    print(html)

    if html.rfind('.html') > 1: break # percobaan 4

    if html == 'Yes. Divide by two and keep going.':
        nothing = int(nothing) / 2
    else :
        # nothing = re.findall(r'\d+', html)[0] # percobaan 1
        nothing = re.findall(r'nothing is (\d+)', html)[0] # percobaan 2

    print('go on: ' + str(nothing))



'''
    Lanjut Level 5:
    http://pythonchallenge.com/pc/def/peak.html
'''
