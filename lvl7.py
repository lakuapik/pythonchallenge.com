#!/usr/bin/env python3

import re
import requests
from PIL import Image
from io import BytesIO

'''
    clue:
        ada tulisan `it's in the air. look at the letters.`
        setelah dipahami, air = oxygen
        link baru: http://www.pythonchallenge.com/pc/def/oxygen.html
        ada sebuah gambar dengan garis blur di tengah
        extract informasi dr gambar tersebut

    *pastikan konek internet untuk eksekusi file python ini
'''

'''
    load image langsung dari url
'''
img_url = 'http://www.pythonchallenge.com/pc/def/oxygen.png'
img = Image.open(BytesIO(requests.get(img_url).content))

'''
    garis blur terletak di tengah gambar
    kita ambil warna rgba nya
'''

center = img.height / 2
colors = []

for x in range(img.width):
    colors.append(img.getpixel((x, center)))

'''
    ternyata banyak duplikat warna rgba yang sederet
    setelah dihitung, satu warna seharusnya mencakup 7 pixel
    jadi kita ambil jaraknya 7 lompatan
'''
colors = colors[::7]

'''
    jika di cek ulang, ada beberapa warna rgb yang tidak sama,
    kita hanya ambil warna yang sama
'''
newcolors = []
for r, g, b, a in colors:
    if r == g == b:
        newcolors.append(r)

'''
    karena rgb memakai angka positif 0-255
    kita asumsikan ini adalah ascii karakter
'''
result = ''.join(map(chr, newcolors))
# smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]

'''
    dari hasil result, kita bisa tahu next level
'''
numbers = re.findall(r'\d+', result)
next_lvl = ''.join(map(chr, map(int, numbers)))

print(next_lvl) # integrity

'''
    Lanjut Level 8:
    http://pythonchallenge.com/pc/def/integrity.html
'''
