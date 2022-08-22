#!/usr/bin/env python3

import os
import re
files = os.listdir('/Users/james/Code/shopee/81901')
files = sorted(files, key=lambda name: int(re.sub('(^.*?\(|\)\..*$)', '', name)))
for file in files:
	print(file)