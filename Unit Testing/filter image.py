#!/usr/bin/env python3

import os
import re
import glob

files = []
directory_name = '/Users/james/code/shopee/82202'
for item in os.listdir(directory_name):
	if (item.endswith(('.png','.jpg','jpeg'))):files.append(item)
image = sorted(files, key=lambda name: int(re.sub('(^.*?\(|\)\..*$)', '', name)))
print(image)