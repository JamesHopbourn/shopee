#!/usr/bin/env python3

import xlwt
import xlrd
import xlsxwriter
from xlutils.copy import copy



# 表格元素定位
def excel_item_index(item_name):
	header = []
	table = xlrd.open_workbook('商品.xls')
	sheet = table.sheet_by_name(table.sheet_names()[0])
	for key in sheet[0]: header.append(key.value)
	return header.index(item_name)

def modify_excel_status():
	table = xlrd.open_workbook('商品.xls')
	first_sheet = table.sheet_by_index(0)
	first_sheet.write(0,11,'完成')
	first_sheet.save() 

modify_excel_status()

