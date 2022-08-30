#!/usr/bin/env python3
from sys import exit
import json
import requests
from urllib3 import *
disable_warnings()

data_cookie = {}
cookies = json.loads(open('../cookies.txt').read())
for i in range(len(cookies)):
	data = json.loads(json.dumps(cookies[i]))
	data_cookie.update({data['name']: data['value']})

brand = {}
for key in [[101298, 0],[100089, 0]]:
	flag = True
	while(flag):
		brand_list = requests.get(f"https://seller.shopee.cn/api/v3/mtsku/get_mtsku_brand_list?brand_status=1&category_ids={key[0]}&cursor={key[1]}&limit=100",
		cookies=data_cookie,
		verify=False
		)
		data = json.loads(brand_list.text)['data']['list'][0]
		flag = data.get('page_info')['has_next']
		key[1] = data.get('page_info')['cursor']
		for item in data['brand_list']:
			brand.update({item['name'].lower(): item['brand_id']})
print(brand)
		