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


###############3

#	for file in files:
#		if file.endswith(('.jpg', '.png', 'jpeg')):
#			image.append(file)
#	if (os.path.exists(os.path.join(directory_name, '123.jpeg'))):
#		index = image.index('123.jpeg')
#		image[0], image[index] = image[index], image[0]
#	elif (os.path.exists(os.path.join(directory_name, '123.png'))):
#		index = image.index('123.png')
#		image[0], image[index] = image[index], image[0]
#	elif (os.path.exists(os.path.join(directory_name, '123.jpg'))):
#		index = image.index('123.jpg')
#		image[0], image[index] = image[index], image[0]