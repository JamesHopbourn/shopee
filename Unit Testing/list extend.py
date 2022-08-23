model_info = {
	"mtsku_model_id": 0,
	"seller_sku": "",
	"stock_setting_list": [],
	"normal_price": "12",
	"is_default": False,
	"tier_index": []
}
model_list = []
for i in range(4):
	for j in range(1):
		model_info = {
			"mtsku_model_id": 0,
			"seller_sku": "",
			"stock_setting_list": [{"sellable_stock": 1}],
			"normal_price": f"10",
			"is_default": False,
			"tier_index": []
		}
		model_info['tier_index'].extend([j,i])
		model_list.append(model_info)
print(model_list)