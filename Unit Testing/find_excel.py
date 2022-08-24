import os

excel = []
files = os.listdir('/Users/james/code/shopee')
for file in files:
	if file.endswith(('.xls')): excel.append(f"{file}")
if(len(excel) == 0):
	print('工作目录下没有 Excel 文件，请检查后重试！')
	print('回车退出程序')
	input()
elif (len(excel) == 1):
	excel = excel[0]
	print(f"将读取【{excel}】内容上架\n请确认是否继续 [y/n]：", end='')
	if (input().lower() != 'y'): os._exit()
else:
	for i in range(len(excel)):
		print(f"{i+1}: {excel[i]}")
	print("\nExcel 文件序号：", end='')
	excel_index = int(input())-1
	excel = excel[excel_index]
print(excel)