#!/usr/bin/env python3

import requests

url = 'http://ipinfo.io'
for i in range(30):
	try:
		r = requests.get(url)
		print(r.text)
	except (Exception):
		print('网络错误')
		continue