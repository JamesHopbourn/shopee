#!/usr/bin/env python3

from PIL import Image, ImageFont, ImageDraw

for i in range(1, 16):
	image = Image.new('RGB', (250, 250), (255,255,255))
	iwidth, iheight = image.size
	font = ImageFont.truetype('/Library/Fonts/SF-Pro.ttf', 200)
	draw = ImageDraw.Draw(image)
	fwidth, fheight = draw.textsize('60', font) # 获取文字高宽
	fontx = (iwidth - fwidth - font.getoffset('22')[0]) / 2
	fonty = (iheight - fheight - font.getoffset('22')[1]) / 2
	draw.text((fontx, fonty), f"{i}", 'black', font)
	image.save(f'image ({i}).jpg') # 保存图片