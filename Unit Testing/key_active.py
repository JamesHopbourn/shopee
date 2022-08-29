#!/usr/bin/env python3

import uuid
import hashlib
import base64
import re
import pyotp
from datetime import datetime

def split_key(key):
	list=[]
	for i in range(0,len(key),4):
		list.append(key[i:i+4])
	return '-'.join(list)

def get_mac_address():
	number = uuid.getnode()
	number = hashlib.md5(b'{number}').hexdigest().upper()
	return re.sub('={1,}', '', base64.b32encode(bytearray(str(number), 'ascii')).decode('utf-8'))[:16]

key = get_mac_address()
print(split_key(get_mac_address()))
print()
#password = input('请输入密码：')
#print(pyotp.TOTP(key).now() == password)
