import PIL as p
import PIL.ImageTk as ptk
from PIL import Image, ImageDraw, ImageEnhance, ImageFont
import random

# output width in pixels
width = 87
palette = [255, 255, 255, 255, 255, 0, 255, 165, 0, 255, 0, 0, 0, 0, 255]
#palette = [98, 52, 18, 255, 255, 0, 255, 165, 0, 255, 0, 0, 0, 0, 255]

# initial brightness and contrast
b = 0
c = 0


def initialise():

	# resizes 1.jpg to width, maintaing aspect ratio, creates img_in
	global img_in
	print('open file 1.jpg')
	img_in = p.Image.open('1.jpg')

	print('resizing')
	wpercent = (int(width) / float(img_in.size[0]))							
	hsize = int((float(img_in.size[1]) * float(wpercent)))
	img_in = img_in.resize((int(width), hsize), p.Image.ANTIALIAS)


def set_bri_cont(b, c):
	# sets the brightness and contrast acording to arguments, then converts to grey
	global img_out
	img_out = img_in
	print('init bri {} / con {}'.format(b, c))

	enhancerb = ImageEnhance.Brightness(img_out)
	img_out = enhancerb.enhance(b)
	enhancerc = ImageEnhance.Contrast(img_out)
	img_out = enhancerc.enhance(c)

	print('convert to greyscale')
	img_out = img_out.convert('L')		


def rubikify(img_out):
	# reduces to 5 colours
	print('reducing palette')
	img_out = img_out.convert('P', palette=Image.ADAPTIVE, colors=5)			
	print('apply portrait palette')
	img_out.putpalette(palette)
	return img_out

	
def grid(img):

	def add_text(img, offset, bps):
		print('label function commence')
		xsize, ysize = img.size

		fnt = ImageFont.truetype('font.ttf', 35)							#set the font

		d=ImageDraw.Draw(img)
		alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'		#The column label
		numcount = 1														#The row label

		for x, al in zip(range(0, img.size[0] - (offset + bps), 72), alph):    #set the range starting from offset + plus a bit to make the text fit in the middle of the grid marking
			d.text((x + bps, (offset * 0.5)), al, font=fnt, fill='red')

		for y in range(round(img.size[1] + 0.5 * bps), offset, -72):
			d.text((round(xsize - (offset * 0.5)), round(y - (offset *0.4))), str(numcount), font=fnt, fill=(255,0,0,255))
			numcount += 1
	
		del fnt
		#img.show()
		#img.save('txtimg.png')
		return img

	print('grid function commence')
	global grid_save

	bps = 24   #big pixel size

	img = img.resize(((img.size[0] * bps), (img.size[1] * bps)), p.Image.ANTIALIAS)
	img = img.convert('RGB')
	print('grid resize x - ' + str(img.size[0]) + ' y - ' + str(img.size[1]))

	xinc = int(img.size[0] / 144)  #increment for grid spacing (to maintain the cube grid when img enlarged)
	yinc = int(img.size[1] / 144)

	offset = round(img.size[1] * 0.072)		#create white image to paste under img
	x1= round(img.size[0] + offset)			#get the offset value for white space
	y1= round(img.size[1] + offset)
	new_background = (255,255,255)
		

	txtimg= Image.new('RGB', (x1, y1), new_background)
	txtimg.paste(img, (0, offset))			#paste img to white image

	img = txtimg
	
	xsize = int(img.size[0])
	ysize = int(img.size[1])

	draw = ImageDraw.Draw(img)

	for x in range(0, ((2 * xinc) +2)):					#y line
		draw.line(((x * 72), 0, (x * 72), ysize), fill='black', width=4)

	img = img.rotate(180)				#rotate before lines drawn because I can't figure out how to keep grid on whole cubes
	draw = ImageDraw.Draw(img)

	for y in range(0, ((2 * yinc) +2)):				#x line
		draw.line((0, (y * 72), xsize, (y * 72)), fill='black', width=4)

	img = img.rotate(180)

	grid_save = img

	#img.save('grid.png')
	#img.show()
	img_out = add_text(img, offset, bps)
	del draw 												#enlarges image and overlays grid in 9x9 panels
	return img_out

initialise()

for i in range(20):

	b += 0.1
	c = 0
	
	for a in range(20):

		c += 0.1

		set_bri_cont(b, c)
		img_out = rubikify(img_out)
		img_out = grid(img_out)

		img_out.save('batch/bri{}con{}.png'.format(round(b,1), round(c,1)))