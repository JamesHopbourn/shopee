#!/usr/bin/env python3

import xlrd
table = xlrd.open_workbook('/Users/james/Code/shopee/商品.xls')
sheet = table.sheet_by_name(table.sheet_names()[0])

for i in range(1, sheet.nrows):
	value = sheet[i][9].value
	print(type(value))
	print(value)