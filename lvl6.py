#!/usr/bin/env python3

import re
from zipfile import ZipFile

'''
    clue:
        ada gambar jaket yang risletingnya terbuka
        ada judul halaman: `now there are pairs`
        ketika di lihat source kode htmlnya
        ada tulisan: `<!-- <-- zip -->`

    *pastikan konek internet untuk eksekusi file python ini
'''

'''
    setelah di cek2, ada link baru yang mengarah ke
    http://pythonchallenge.com/pc/def/channel.zip
    clue di readme.txt:
        hint1: start from 90052
        hint2: answer is inside the zip

    buka zip file dan looping utk cari jawabannya
'''

archive = ZipFile('lvl6.zip', 'r')
txtFile = '90052.txt'

while True:
    text = archive.read(txtFile).decode('utf-8')
    try:
        txtFile = re.findall(r'nothing is (\d+)', text)[0] + '.txt'
    except:
        print(text) # Collect the comments.
        break

'''
    dapat clue baru yaitu `collect the comments`
    kita coba lagi dan kumpulkan commentnya
'''

archive = ZipFile('lvl6.zip', 'r')
txtFile = '90052.txt'
comments = ''

while True:
    text = archive.read(txtFile).decode('utf-8')
    comments += archive.getinfo(txtFile).comment.decode('utf-8')
    try:
        txtFile = re.findall(r'nothing is (\d+)', text)[0] + '.txt'
    except:
        break

print(comments)

'''
    Lanjut Level 7:
    http://pythonchallenge.com/pc/def/hockey.html
'''
