#!/usr/bin/env python3

import xlwt 
import xlrd
import xlrd
from xlutils.copy import copy

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
	table = xlrd.open_workbook(('商品.xls'))
	sheet = table.sheet_by_index(0)
	for key in sheet[0]: header.append(key.value)
	return header.index(item_name)

def product_launched(launch_status):
	table = xlrd.open_workbook('商品.xls')
	workbook = copy(table)
	sh1 = workbook.get_sheet(0)
	# 产品序号实际是从0开始
	for i in range(len(launch_status)):
		sh1.write(launch_status[i]+1, excel_item_index('上架情况'), '已上架')
	workbook.save('商品.xls')

product_launched([0,1,2,3])