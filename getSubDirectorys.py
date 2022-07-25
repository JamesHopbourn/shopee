#!/usr/bin/env python3

import os
rootdir = '/Users/james/Pictures/测试样品'
for file in os.listdir(rootdir):
	d = os.path.join(rootdir, file)
	if os.path.isdir(d):
		print(d)