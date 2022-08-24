#!/usr/bin/env python3

import os
rootdir = '/Users/james/Pictures/测试样品'
for file in os.listdir(rootdir):
	path = os.path.join(rootdir, file)
	if os.path.isdir(path):
		files = os.listdir(path)
		for file in files:
			if file.endswith(('.jpg', '.png', 'jpeg')):
				print(path + file)
			
		print(111)