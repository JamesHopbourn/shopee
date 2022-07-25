#!/usr/bin/env python3

import json
import configparser

config = configparser.ConfigParser()
config.read('/Users/james/Code/shopee/config.txt', encoding='utf-8')
# 常用变量定义
price = config.get('data', 'price')
sellable_stock = config.getint('data', 'sellable_stock')



size_result = []
for i in range(0, 15):
	size_info = {
				"mtsku_model_id": 0,
				"seller_sku": "",
				"stock_setting_list": [{"sellable_stock": sellable_stock}],
				"normal_price": price,
				"is_default": False,
				"tier_index": [1]
		}
	size_info['tier_index'][0]= i
	size_result.append(size_info)
print(size_result)