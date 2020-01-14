#!/usr/bin/env python3

import re
import bz2
import requests

'''
    buka source code
    link baru http://www.pythonchallenge.com/pc/return/good.html dgn basic auth
    dikunjungi dan ada clue: inflate

    ada comment
    <!--
    un: 'BZh91AY&SYA....'
    pw: 'BZh91AY&SY....'
    -->

    *pastikan konek internet untuk eksekusi file python ini
'''

'''
    deinflate user and password
    dilihat dari BZh91AY adalah hasil compress bz2
'''

# stuck convert string to bytes without escaping
# html = requests.get('http://www.pythonchallenge.com/pc/def/integrity.html').text
# un = re.findall(r'un\:\s\'(.*)\'', html)[0]
# pw = re.findall(r'pw\:\s\'(.*)\'', html)[0]

un = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

usr = bz2.decompress(un).decode()
pwd = bz2.decompress(pw).decode()

print('user: {}, password: {}'.format(usr, pwd))

'''
    Lanjut Level 9:
    http://www.pythonchallenge.com/pc/return/good.html
    user: huge, password: file
'''
