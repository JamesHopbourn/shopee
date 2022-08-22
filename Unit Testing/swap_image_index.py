#!/usr/bin/env python3

import os

path = '/Users/james/Desktop'
image= []
files = os.listdir(path)

for x in range(len(files)):
	if files[x].endswith(('.jpg', '.png', 'jpeg')):
		image.append(files[x])
	if (files[x] in ('123.jpg', '123.jpeg', '123.png')):
		swap = image.index(files[x])
		image[0], image[swap] = image[swap], image[0]