#!/usr/bin/env python3
import json
import requests
from urllib3 import *
disable_warnings()

data_cookie = {}
cookies = json.loads(open('./cookies.txt').read())
for i in range(len(cookies)):
	data = json.loads(json.dumps(cookies[i]))
	data_cookie.update({data['name']: data['value']})

brand_list = requests.get("https://seller.shopee.cn/api/v3/mtsku/get_mtsku_brand_list?category_ids=101298&brand_status=1&cursor=0&limit=100",
	cookies=data_cookie,
	auth=(),
	verify=False
)

print(json.loads(brand_list.text))
