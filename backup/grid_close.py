import tkinter as tk
import PIL as p
import PIL.ImageTk as ptk
from tkinter import filedialog
from PIL import Image, ImageDraw
import random



window = tk.Tk()
window.title('Rubikify v1.0')
window.geometry('800x650')

random_enabled = False

def grid(img):

	img = img.resize(((img.size[0] * 24), (img.size[1] * 24)), p.Image.ANTIALIAS)

	print('grid resize x - ' + str(img.size[0]) + ' y - ' + str(img.size[1]))

	draw = ImageDraw.Draw(img)

	xinc = int(img.size[0] / 72)
	yinc = int(img.size[1] / 72)
	xsize = int(img.size[0])
	ysize = int(img.size[1])
	print(str(xinc))
	print(str(yinc))
	print(str(xsize))
	print(str(ysize))
	
	for x in range(0, ((2 * xinc) +2)):
		draw.line(((x * 36), 0, (x * 36), ysize), fill=128)
		
	for y in range(0, ((2 * yinc) + 2)):
		draw.line((0, (y * 36), xsize, (y * 36)), fill=128)
	
	img.save('grid.png')
	del draw

def random0():
	global random_enabled
	random_enabled = False

def random1():
	global random_enabled
	random_enabled = True


def imresize(input_image, max_size):			#returns x, y in pixels to maintain aspect ratio.  neither axis will exceed max size

	width = float(input_image.size[1])
	wpercent = (width / float(input_image.size[0]))
	hsize = int((float(input_image.size[1]) * float(wpercent)))
	
	if width > hsize:
		x = max_size
		y = max_size * wpercent
		xoff = 0								#x,y center gives an OFFSET to centre image that are not square
		yoff = (max_size - y) / 2
	elif width == hsize:
		x = max_size
		y = max_size
		xoff = 0
		yoff = 0
	else:
		x = max_size / wpercent
		y = max_size
		xoff = (max_size - x) / 2
		yoff = 0
	x = int(x)
	y = int(y)
	print('resize to scale function --- output - W ' + str(x) + ' /  H ' + str(y))
	print('X offset ' + str(xoff) + ' / Y offset ' + str(yoff) + '\n')

	return(x, y, xoff, yoff)


def getfile():

	global img_in

	original_image_location = filedialog.askopenfilename()								#gets the input file and labels as active file
	file_label = original_image_location[-35:]
	active_file_label.configure(text=('Active file >> ....' + str(file_label)))

	
	img_in = p.Image.open(str(original_image_location))
 
	x, y, xoff, yoff = imresize(img_in, 400)											#calls imresize function

	img_in = img_in.resize((x, y), p.Image.ANTIALIAS)									#used x, y from function as image size

	img_in1 = ptk.PhotoImage(img_in)													#convert to photoimage
	input_image.configure(image=img_in1)												#update image in label
	input_image.image = img_in1															#bloody placeholder

	input_image.place(x= 0 + xoff, y= 250 + yoff)										#centre the image using offsets from resize function


	go = p.Image.open("go.png")													#create and place the go button
	go_holder1 = ptk.PhotoImage(go) 
	go_button = tk.Button(window, image=go_holder1, command=convert, borderwidth=5)
	go_button.image = go_holder1	
	go_button.place(x=335, y=146)


def zoom():
	x, y, xoff, yoff = imresize(img_out, 700)
	zoomed_img_out = img_out.resize((x, y), p.Image.ANTIALIAS)							#resizes COPY of output image to simulate zoom
	print('zoomed')
	zoomed_img_out.show()


def convert():

	global img_out
	global random_enabled
	global grid_enabled
	global grid_ratio
	
	img_out=img_in 

	width = width_input.get()

	wpercent = (int(width) / float(img_out.size[0]))							
	hsize = int((float(img_out.size[1]) * float(wpercent)))

	img_out = img_out.resize((int(width), hsize), p.Image.ANTIALIAS)
	print('resizing')


	img_out = img_out.convert('L')
	print('convert to greyscale')


	if green_enabled.get() == True:
		colour_quantity = 6
		print('green enabled')
	else:
		colour_quantity = 5

	img_out = img_out.convert('P', palette=Image.ADAPTIVE, colors=colour_quantity)
	print('reducing pallete')

	#orange = [255, 128, 0,]
	#green = [0, 255, 0,]
	#blue = [0, 0, 255,]
	#red = [255, 0, 0,]
	#white = [255, 255, 255,]
	#yellow = [255, 255, 0,]
	#blank = [0, 0, 0,]


	#combo = (  white,           yellow,        orange,         red,            blue)
	combo = [[255, 255, 255,], [255, 255, 0,], [255, 128, 0,], [255, 0, 0,], [0, 0, 255,]]

	if colour_quantity == 6:
		combo.insert(1, [0, 255, 0,])
		print('insert green to palette list')

	if random_enabled == True:
		random.shuffle(combo)
		print('shuffling rubik colours')


	if colour_quantity == 6:
		combo = (combo[0] + combo[1] + combo[2] + combo[3] + combo[4] + combo[5])
		if random_enabled == True:
			print('green included in randomized active palette')
		else:
			print('green is included in active palette')
	else:
		combo = (combo[0] + combo[1] + combo[2] + combo[3] + combo[4])
		if random_enabled == True:
			print('green is not included in randomized active palette')
		else:
			print('green is not included in active palette')



	remainder = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

	final = (combo + remainder)
	print('final palette......\n' + str(combo) + '\n')
	img_out.putpalette(final)

	print('initial image out size - x ' + str(img_out.size[0]) + ' / y ' + str(img_out.size[1]) + '\n')


	print('saved image out size - ')

	#x, y, xoff, yoff = imresize(img_out, (12 * (img_out.size[0])))								#resize the modified image for saved output 12 pixel per pixel
	#img_out = img_out.resize((x, y))														
	#img_out.save('resize.png')


	#grid_ratio = img_out.size[1] / img_out.size[0]

	if grid_enabled.get() == True:
		gridme = img_out
		grid(gridme)


	print('displayed image out size - ')
	x, y, xoff, yoff = imresize(img_out, 400)
	img_out = img_out.resize((x, y))															#resize the modified image for display in ui
	img_out1 = ptk.PhotoImage(img_out)

	output_image.image = img_out1															#the bloody placeholder
	output_image.configure(image=img_out1)													#update image in label
	output_image.place(x=400 + xoff, y=250 + yoff)											#place updated label with offsets

	zoom_button = tk.Button(window, text='Zoom', command=zoom)
	zoom_button.place(x=700, y=135)

	

file = 'No file loaded'
active_file_label = tk.Label(window, text=('Active file >>    ' + file))
active_file_label.place(x=5, y=5)

background = p.Image.open('background.jpg')											#set coloured background to fill dead space whe non square images used
background1 = ptk.PhotoImage(background)
background_label = tk.Label(window, image=background1)
background_label.image = background1
background_label.place(x=0, y=250)

no_file_in_holder = p.Image.open('noinput.png').resize((400,400))							#no input image
no_file_in_holder1 = ptk.PhotoImage(no_file_in_holder)
input_image =tk.Label(window, image=no_file_in_holder1)
input_image.image = no_file_in_holder1
input_image.place(x=0, y=250)

no_file_holder = p.Image.open('nooutput.png').resize((400,400))							#no output image
no_file_holder1 = ptk.PhotoImage(no_file_holder)
output_image =tk.Label(window, image=no_file_holder1)
output_image.image = no_file_holder1
output_image.place(x=401, y=250)

logo_holder = p.Image.open('cube_logo.png').resize((100,110))							#logo image
logo_holder1 = ptk.PhotoImage(logo_holder)
logo_image =tk.Label(window, image=logo_holder1)
logo_image.image = logo_holder1
logo_image.place(x=350, y=5)

open_file_button = tk.Button(window, text='Open image file', command=getfile)
open_file_button.place(x=600, y=20)

width_label = tk.Label(window, text='Width in pixels ')
width_label.place(x=15, y=45)

width_input = tk.Entry(window, width=5)
width_input.insert(tk.END, '60')
width_input.place(x=150, y=45)
width_input.focus()

green_enabled = tk.BooleanVar()
green_enabled.set(False)
green_checkbox = tk.Checkbutton(window, text='Green enabled', variable=green_enabled)
green_checkbox.place(x=200, y=135)

palette_standard = tk.Radiobutton(window, text='Standard palette', command=random0)
palette_random = tk.Radiobutton(window, text='Random palette', value=1, command=random1)
palette_standard.place(x=5, y=135)
palette_random.place(x=5, y=110)

grid_enabled = tk.BooleanVar()
grid_enabled.set(False)
grid_checkbox = tk.Checkbutton(window, text='Grid enabled', var = grid_enabled)
grid_checkbox.place(x=200, y=110)


window.mainloop()