#!/usr/bin/env python3

import os
import json
import base64
import requests 
from urllib3 import *

disable_warnings()

def upload(image_path):
	image_encode = open(image_path, 'rb').read().decode("latin-1",errors='ignore')
			
	req = requests.post("https://seller.shopee.cn/api/v3/general/upload_image/?SPC_CDS=d05d282f-3101-4864-b375-66621f6584b4&SPC_CDS_VER=2&cnsc_shop_id=821694597",
		data=f"""------WebKitFormBoundaryJBDkf5fKShesvHzh
Content-Disposition: form-data; name="file"; filename="blob"
Content-Type: image/jpeg

{image_encode}
------WebKitFormBoundaryJBDkf5fKShesvHzh--

""",
		headers={
			"Host": "seller.shopee.cn",
			"accept": "application/json, text/plain, */*",
			"accept-language": "zh-CN,zh;q=0.9",
			"content-type": "multipart/form-data; boundary=----WebKitFormBoundaryJBDkf5fKShesvHzh",
			"origin": "https://seller.shopee.cn",
			"referer": "https://seller.shopee.cn/portal/product/mtsku/new?cnsc_shop_id=821694597",
			"sc-fe-session": "9ea406c5-c0ec-45f9-aef5-c2aaf2d213f1",
			"sc-fe-ver": "56878",
			"sec-ch-ua": "\".Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"103\", \"Chromium\";v=\"103\"",
			"sec-ch-ua-mobile": "?0",
			"sec-ch-ua-platform": "\"macOS\"",
			"sec-fetch-dest": "empty",
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-origin",
			"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
		},
		cookies={
			"CNSC_SSO": "jcsu3IcSZx/7zAGt1uTxuP2ZRsr2p7Sk2zmalEwtcWndAH2ypjOEhZ6JSLhrO91p",
			"SC_DFP": "PeohBwjkIhEoCMCUcF6iUGLClcD7hnES",
			"SPC_CDS": "d05d282f-3101-4864-b375-66621f6584b4",
			"SPC_CNSC_TK": "eede1fca072d11edb1616ecf936a5c2b",
			"SPC_CNSC_UD": "1_1473107",
			"_QPWSDCXHZQA": "c97622d9-c3de-4324-ded7-28fbf9d54818",
			"fulfillment-language": "zh-CN"
		},
		auth=(),
		verify=False
	)
	return json.loads(req.text)['data']['resource_id']


image_address = []
path = "/Users/james/Pictures/测试样品/NO1/"
# list files in img directory
files = os.listdir(path)
for file in files:
	# make sure file is an image
	if file.endswith(('.jpg', '.png', 'jpeg')):
		result = upload(path + file)
		image_address.append(result)
		
print(image_address)