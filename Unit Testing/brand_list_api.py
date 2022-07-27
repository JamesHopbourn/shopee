#!/usr/bin/env python3
import requests
import json

brand_list = requests.get("https://seller.shopee.cn/api/v3/mtsku/get_mtsku_brand_list?SPC_CDS=cf75bb61-df31-42f4-94d2-31f33c00315f&SPC_CDS_VER=2&category_ids=101298&brand_status=1&cursor=0&limit=100&cnsc_shop_id=821694597",
	cookies={
		"CNSC_SSO": "1ELepqUwZW2zcZz0NnQhkXyH3PYqOrMvDWxksH9VZ1EwiTROjE/0406+uBGd83js",
		"SC_DFP": "PeohBwjkIhEoCMCUcF6iUGLClcD7hnES",
		"SPC_CDS": "cf75bb61-df31-42f4-94d2-31f33c00315f",
		"SPC_CNSC_TK": "2c4062420cb211edb29096a4f1819780",
		"SPC_CNSC_UD": "1_1473107",
		"_QPWSDCXHZQA": "c97622d9-c3de-4324-ded7-28fbf9d54818",
		"fulfillment-language": "zh-CN"
	},
	auth=(),
	verify=False
)

print(json.loads(brand_list.text))