#!/usr/bin/env python3

'''
    15 Apr 2017 JKT DHE
    davidadi216@gmail.com
    solusi untuk Level 0 pythonchallenge.com
    http://www.pythonchallenge.com/pc/def/0.html
'''

'''
    clue: diberikan gambar monitor dengan anka 2 pangkat 38
    tugas: hasilnya berapa?
'''

result = pow(2, 38)
result = 2 ** 38

'''
    Kenapa angka 38?
    Karena angka 38 kalau di bahasa java / c sudah menunjukkan longInteger,
    sedangkan di python tidak ada longInteger, bingInteger, dsb.
    Di python hanya ada satu type Integer: <class int>

    pembuktian:
    print(type(result))
'''
print(result)
#print(type(result))

'''
    Level 1:
    http://pythonchallenge.com/pc/def/274877906944.html
    Akan teralihkan ke:
    http://www.pythonchallenge.com/pc/def/map.html
'''
