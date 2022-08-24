#!/usr/bin/env python3

import xlrd

def excel_item_title(item_index):
	header = []
	table = xlrd.open_workbook('../商品.xls')
	sheet = table.sheet_by_name(table.sheet_names()[0])
	for key in sheet[0]: header.append(key.value)
	print(header[item_index])
	print(len(sheet))

excel_item_title(9)