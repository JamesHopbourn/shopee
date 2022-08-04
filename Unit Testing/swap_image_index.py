#!/usr/bin/env python3

import os

path = '/Users/james/Pictures/谷歌下载/okk'
image_linklist= []
files = os.listdir(path)
for file in files:
	if file.endswith(('.jpg', '.png', 'jpeg')):
		image_linklist.append(f"{file}")
print(image_linklist)

if (os.path.exists(os.path.join(path, '123.jpg'))):
	index = image_linklist.index('123.jpg')
elif (os.path.exists(os.path.join(path, '123.png'))):
	index = image_linklist.index('123.png')
elif (os.path.exists(os.path.join(path, '123.jpeg'))):
	index = image_linklist.index('123.jpeg')
image_linklist[0], image_linklist[index] = image_linklist[index], image_linklist[0]

print(image_linklist)