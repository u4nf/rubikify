import tkinter as tk
import tkinter.messagebox as box
import PIL as p
import PIL.ImageTk as ptk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageEnhance, ImageFont
import random


img = p.Image.open('grid.png')#.convert('RGBA')
palette = [255, 255, 255, 255, 255, 0, 255, 165, 0, 255, 0, 0, 0, 0, 255]

xsize, ysize = img.size

if ysize > xsize:					#set the offset to be the larger of of the x or y axis
	offset = round(ysize * 0.04)
else:
	offset = round(xsize * 0.04)


x1= round(xsize + offset)			#get the offset for new white space image
y1= round(ysize + offset)
		

txtimg= Image.new('P', (x1, y1), (255,255,255,255))   #4th entry on rgb is opacity

fnt = ImageFont.truetype('font.ttf', 40)							#set the font

d=ImageDraw.Draw(txtimg)
alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'		#The column label
numcount = 1														#The row label


for x, al in zip(range(offset + 13, round(img.size[0]), 72), alph):    #set the range starting from offset + plus a bit to make the text fit in the middle of the grid marking
	d.text((x, round(img.size[1] - (offset * 0.01))), al, font=fnt, fill='red')
	

for y in range(0, round(img.size[1]), 72):
	d.text((round(offset * 0.1), y), str(numcount), font=fnt, fill=(255,0,0,255))
	numcount += 1


#txtimg.putpalette(palette)							  #apply new palette
txtimg.paste(img, (offset, 0))		  					#paste original image on new blank canvas


txtimg.show()

#txtimg.save('txtimg.png')
