#!/usr/bin/env python3
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
for i in [100016, 100637]:
	brand_list = requests.get(f"https://seller.shopee.cn/api/v3/mtsku/get_mtsku_brand_list?category_ids={i}&brand_status=2&cursor=0&limit=100",
	cookies=data_cookie,
	verify=False
  )
	data = json.loads(brand_list.text)['data']['list'][0]['brand_list']
	for item in data:
		brand.update({item['name'].lower(): item['brand_id']})

print(brand)
