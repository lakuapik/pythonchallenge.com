#!/usr/bin/env python3

import pickle
import requests

'''
    clue:
        ada gambar bukit dan tulisan `pronounce it`
        ketika di lihat source code htmlnya
        ada link http://www.pythonchallenge.com/pc/def/banner.p
        dan tulisan `peak hell sounds familiar ?`

    tugas:
        deserialize konten yang ada di banner.p

    *pastikan konek internet untuk eksekusi file python ini
'''

url = 'http://www.pythonchallenge.com/pc/def/banner.p'
content = requests.get(url).content

'''
    data yang ada di dalam banner.p adalah
    hasil serialized object python menggunakan pickle,
    jd kita pake pickle lagi utk unserialzed datanya.
    hasil unserialized adalah list yg isinya tupple (karakter, angka)
    dirangkai maka akan jadi banner
'''

unserialized = pickle.loads(content)

for obj in unserialized:
    line = ''
    for obj2 in obj:
        char, times = obj2
        line += char * times
    print(line)

'''
    Lanjut Level 6:
    http://pythonchallenge.com/pc/def/channel.html
'''
