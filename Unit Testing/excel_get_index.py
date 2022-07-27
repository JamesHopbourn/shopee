#!/usr/bin/env python3

import xlrd

def excel_item_index(item_name):
	header = []
	table = xlrd.open_workbook('商品.xls')
	sheet = table.sheet_by_name(table.sheet_names()[0])
	for key in sheet[0]: header.append(key.value)
	print(header.index('品牌ID'))
	
		
excel_item_index('品牌ID')