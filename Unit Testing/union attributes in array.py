request_data = {
	"description": ['商品描述'],
	"tier_variation": [],
	"video_list": [],
	"model_list": '',
	"condition": 1,
	"category_path": '',
	"seller_sku": "",
	"ds_cat_rcmd_id": "",
	"description_type": "normal",
	"weight": '',
	"brand_id": '',
	"days_to_ship": '',
	"size_chart": "",
	"attributes": [],
	"dimension": {},
	"images": '',
	"mtsku_item_id": 0,
	"name": ''
}

data = {'文件夹名': 82202, '商品分类': '女包背包', '商品名称': '空军一号低帮运动休闲板鞋', '商品描述': "fashion", '性别': None, '品牌': 'NoBrand', '场合': '正式', '材质': '帆布', '子母包': '是', '尺寸': '其他', '包包款式': None, '价格': 248, '库存': 99, '发货时间': 5, '包装重量': 1, 'SKUcolor': 'red,blue,green,orange', 'SKUsize': '35,36,37,38,39,40', '暂停时间': 1, '上架情况': '完成'}

attributes = [
	['子母包', 100221, {"是":1800,"否":1792}],
	['尺寸', 100218, {"微型":1793,"其他":1804}],
	['性别', 100022, {"女":652,"男":662,"情侣":674}],
	['场合', 100155, {"办公":1527,"休闲":1387,"正式":1433,"其他":1397,"户外活动":1515,"运动":1502}],
	['材质', 100134, {"帆布":1129,"皮革":1221,"尼龙":1165,"其他":1257,"PVC":1178,"合成皮":1280,"纺织":1285}],
	['包包款式', 100216, {"波士顿包":1797,"水桶包":1805,"相机包":1816,"链条包":1826,"半月包":1835,"饺子包":1846,"邮差包":1855,"其他":1867,"马鞍包":1878,"小方包":1888}]
]

attr = []
[attr.append(attributes[i][0]) for i in range(len(attributes))]

for item in attributes:
	if(data.get(item[0])):
		request_data['attributes'].append({
			"attribute_id": attributes[attr.index(item[0])][1],
			"attribute_value_id": attributes[attr.index(item[0])][2][data[item[0]]]
		})
print(request_data)