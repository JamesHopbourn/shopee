#!/usr/bin/env python3

a = 4
b = 4

model_list = []

for i in range((a)):
	model_info = {
		"tier_index": []
	}
	model_info['tier_index'].append(i)
	
	for j in range(a,a+1):
		model_info['tier_index'].append(j)
	
	model_list.append(model_info)

print(model_list)