import os
import sys
import json
import xlrd
import time
import requests
from xlutils.copy import copy
from urllib3 import *
disable_warnings()

# 获取文件绝对路径
def get_file_path(filename):
	if getattr(sys, 'frozen', False):
		application_path = os.path.dirname(os.path.realpath(sys.executable))
	elif __file__:
		application_path = os.path.dirname(__file__)
	return os.path.join(application_path, filename)

# 读取表格内容
def read_excel(excel_filename):
	result = []
	table = xlrd.open_workbook(excel_filename)
	sheet = table.sheet_by_index(0)
	for i in range(1, sheet.nrows):
		result.append(sheet[i])
	return result

def validate_directory_exists(dirname_list):
	return

def excel_duplicates_check():
	dir_names = []
	data = read_excel('商品.xls')
	for item in data: dir_names.append(item[0].value)
	if len(dir_names) != len(set(dir_names)):
		print('Excel 中文件夹重名，请检查后重试')

excel_duplicates_check()