#!/usr/bin/env python3

'''
    15 Apr 2017 JKT DHE
    davidadi216@gmail.com
    Solusi untuk Level 1 pythonchallenge.com
    http://www.pythonchallenge.com/pc/def/map.html
'''

'''
    clue:
        K -> M, O -> Q, E -> G

    tugas:
        mengubah setiap huruf di kalimat tersebut maju 2 huruf.
        ini bisa dilakukan dengan mudah menggunakan str.maketrans() di python3
        lalu di str.translate()
'''

data = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

textDari = "abcdefghijklmnopqrstuvwxyz"
textKe = "cdefghijklmnopqrstuvwxyzab"

#membuat dictionary yang me-map A -> C sampai Z -> B
mapped = str.maketrans(textDari, textKe)

#men-translate string
result = data.translate(mapped)

print(result)


'''
    "i hope you didnt translate it by hand. thats what computers are for.
    doing it in by hand is inefficient and that's why this text is so long.
    using string.maketrans() is recommended. now apply on the url."

    - itu adalah kalimat setelah di translate, namun itu bukan jawaban.
    Ini memberikan clue berikutnya-> "now apply on the url": map.html
    translate kata "map" dengan "mapped" yang sudah kita buat

'''

print("map".translate(mapped))
# hasilnya adalah "ocr"

'''
    Level 2:
    http://pythonchallenge.com/pc/def/ocr.html
'''
