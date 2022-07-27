#!/usr/bin/env python3

import os
import sys
import json
import xlrd
import time
import requests
from urllib3 import *
disable_warnings()

# 获取文件绝对路径
def get_file_path(filename):
	if getattr(sys, 'frozen', False):
		application_path = os.path.dirname(os.path.realpath(sys.executable))
	elif __file__:
		application_path = os.path.dirname(__file__)
	return os.path.join(application_path, filename)

# cookies 文件解析
def parse_cookies():
	data_cookie = {}
	header_cookies = ""
	with open(get_file_path('cookies.txt'), 'r') as content:
		cookies = json.loads(content.read())
	for i in range(len(cookies)):
		data = json.loads(json.dumps(cookies[i]))
		temp = {data['name']: data['value']}
		data_cookie.update(temp)
		header_cookies += f"{data['name']}={data['value']}; "
		header_cookies = header_cookies.replace('"', '\\"')
	return data_cookie, header_cookies

# API 通过 cookies 获取 shopID
def get_shopID():
	account_info = requests.get("https://seller.shopee.cn/api/cnsc/selleraccount/get_session/",
		cookies=data_cookie,
		auth=(),
		verify=False
	)
	status = json.loads(account_info.text)
	if (('errcode' in status) and (status['errcode'] == 1)):
		print('cookies 失效，请重置 cookies.txt 文件')
		sys.exit()
	return status['sub_account_info']['current_shop_id']

# 读取表格内容
def read_excel(excel_filename):
	result = []
	table = xlrd.open_workbook(excel_filename)
	sheet = table.sheet_by_index(0)
	for i in range(1, sheet.nrows):
		result.append(sheet[i])
	return result

# 表格元素定位
def excel_item_index(item_name):
	header = []
	table = xlrd.open_workbook(get_file_path('商品.xls'))
	sheet = table.sheet_by_index(0)
	for key in sheet[0]: header.append(key.value)
	return header.index(item_name)

# 获取图片名字
def get_image_name(directory_name):
	image_linklist = []
	files = os.listdir(directory_name)
	for file in files:
		if file.endswith(('.jpg', '.png', 'jpeg')):
			image_linklist.append(f"{directory_name}/{file}")
	return image_linklist

# 上传商品图片
def get_image_hash(image_path):
	image_encode = open(image_path, 'rb').read().decode('latin-1')
	request = requests.post("https://seller.shopee.cn/api/v3/general/upload_image/",
		params={
			"SPC_CDS": "d05d282f-3101-4864-b375-66621f6584b4",
			"SPC_CDS_VER": "2",
			"cnsc_shop_id": shopID,
		},
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
		cookies=data_cookie,
		auth=(),
		verify=False
	)
	# 返回图片的 resource_id 列表
	return json.loads(request.text)['data']['resource_id']

# 性别选项映射文件; 直接作用于 data
def gender_option_mapper(gender_value):
	gender_option_data = {
		"女": 652,
		"男": 662,
		"情侣": 674
	}
	return gender_option_data[gender_value]
	
# 性别尺码信息 男款 女款 情侣款
def shose_size_mapper(excel_gender):
	man = [
		"BR38=EU40=25CM=US7",
		"BR38.5=EU40.5=25.5cm=US7.5",
		"BR39=EU41=26CM=US8",
		"BR40=EU42=26.5CM=US8.5",
		"BR40.5=EU42.5=27CM=US9",
		"BR41=EU43=27.5CM=US9.5",
		"BR42=EU44=28CM=US10",
		"BR42.5=EU44.5=28.5CM=US10.5",
		"BR43=EU45=29CM=US11",
		"BR44=EUR46=29.5CM=US11.5"
	]

	woman = [
		"BR34=EU36=22.5CM=US5.5",
		"BR34.5=EU36.5=23CM=US6",
		"BR35.5=EU37=23.5CM=US6.5",
		"BR36=EU38=24CM=US7",
		"BR36.5=EU38.5=24.5CM=US7.5",
		"BR37=EU39=25CM=US8"
	]
	
	gender_mapper = {
		"男": man,
		"女": woman,
		"情侣": woman + man
	}
	return gender_mapper[excel_gender]

# 商品类别映射函数
def catagory_mapper(catagory_value):
	category_mapper_data = {
		"篮球鞋": [100637,100726,101298],
		"跑步鞋": [100637,100726,101299],
		"训练鞋": [100637,100726,101300],
		"足球鞋": [100637,100726,101306],
		"登山鞋": [100637,100726,101305],
		"网球鞋": [100637,100726,101301],
		"排球鞋": [100637,100726,101302],
		"室内足球鞋": [100637,100726,101304]
	}
	return category_mapper_data[catagory_value]

# 鞋子品牌映射函数
def brand_id_mapper(brand_name):
	brand_id_data = {
		"air jordan": 1800399,
		"adidas": 1800379,
		"nobrand": 0,
		"nb": 1802060,
		"puma": 2240153
	}
	return brand_id_data[brand_name.lower()]

# 根据鞋码数量重复生成数据
def generate_repeat_data(size_options, sellable_stock, price):
	model_list = []
	for i in range(len(size_options)):
		model_info = {
			"mtsku_model_id": 0,
			"seller_sku": "",
			"stock_setting_list": [{"sellable_stock": sellable_stock}],
			"normal_price": f"{price}",
			"is_default": False,
			"tier_index": []
		}
		model_info['tier_index'].append(i)
		model_list.append(model_info)
	return model_list

def generate_request_data(excel_data, size_options, model_list, image_linklist):
	request_data = {
		"description": excel_data[excel_item_index('商品描述')].value,
		"tier_variation": [
			{
				"images": [],
				"name": "size",
				"options": size_options
			}
		],
		"video_list": [],
		"model_list": model_list,
		"condition": 1,
		"category_path": catagory_mapper(excel_data[excel_item_index('商品分类')].value)
		,
		"seller_sku": "",
		"ds_cat_rcmd_id": "",
		"description_type": "normal",
		"weight": f"{excel_data[excel_item_index('包装重量')].value}",
		"brand_id": brand_id_mapper(excel_data[excel_item_index('品牌')].value),
		"days_to_ship": int(excel_data[excel_item_index('发货时间')].value),
		"size_chart": "",
		"attributes": [
			{
				"attribute_id": 100022,
				"attribute_value_id": gender_option_mapper(excel_data[excel_item_index('性别')].value)
			}
		],
		"dimension": {},
		"images": image_linklist,
		"mtsku_item_id": 0,
		"name": excel_data[excel_item_index('商品名称')].value
	}
	return request_data

def send_request(post_data):
	response = requests.post(
		url="https://seller.shopee.cn/api/v3/mtsku/create_mtsku/",
		params={
			"cnsc_shop_id": shopID,
		},
		headers={
			"Cookie": f"{header_cookies}",
			"Content-Type": "application/json; charset=utf-8",
		},
		data=json.dumps(post_data),
		verify=False
	)
	status = json.loads(response.text)
	if (status['code'] == -2) and ('mtsku.CreateMtskuRequest.Name' in status['message']):
		print("商品名称有误，请修改后重试")
	else:
		print("上架成功 ✅") if(status['code'] == 0) else print("失败")
	print()
	
def countdown_timer(t):
	print(f"随机暂停时间：{t}秒")
	time.sleep(t)
	return
	
# 函数入口定义
if __name__=="__main__":
		data_cookie = parse_cookies()[0]
		header_cookies = parse_cookies()[1]
		shopID = get_shopID()
		excel_sheet = read_excel(get_file_path('商品.xls'))
		# 循环处理所有的产品
		for i in range(len(excel_sheet)):
			excel_data = excel_sheet[i]
			# 如果标记为上传完成的产品就跳过
			if(excel_data[excel_item_index('上架情况')].value == '完成'):
				continue
			# 随机数的暂停时间
			wait_time = int(excel_data[excel_item_index('暂停时间')].value)
			countdown_timer(wait_time)
			# 定义数组，存放图片 ID
			image_linklist = []
			for image in get_image_name(excel_data[excel_item_index('文件夹名')].value):
				image_linklist.append(get_image_hash(image))
			print(f"上传图片数量：{len(image_linklist)}")
			# 获取价格和库存信息
			excel_price = excel_data[excel_item_index('价格')].value
			excel_sellable_stock = int(excel_data[excel_item_index('库存')].value)
			# 从 Excel 读取性别信息，返回适配的尺码信息
			gender_index = excel_item_index('性别')
			gender_value = excel_data[gender_index].value
			size_options = shose_size_mapper(gender_value)
			# 根据尺码信息的数量构造库存价格对应信息
			model_list = generate_repeat_data(size_options, excel_sellable_stock, excel_price)
			# 根据上面的参数构造整体的数据包
			post_data = generate_request_data(excel_data, size_options, model_list, image_linklist)
			send_request(post_data)
		print("\a自动上架完成")