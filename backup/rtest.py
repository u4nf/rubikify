import tkinter as tk
import tkinter.messagebox as box
import PIL as p
import PIL.ImageTk as ptk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageEnhance
import random



window = tk.Tk()
window.title('Rubikify v1.1')
window.iconbitmap("@" + "cube_logo.xbm")
window.geometry('800x650')



random_enabled = False


def grid(img):
	global grid_save

	img = img.resize(((img.size[0] * 24), (img.size[1] * 24)), p.Image.ANTIALIAS)

	print('grid resize x - ' + str(img.size[0]) + ' y - ' + str(img.size[1]))

	draw = ImageDraw.Draw(img)

	xinc = int(img.size[0] / 144)
	yinc = int(img.size[1] / 144)
	xsize = int(img.size[0])
	ysize = int(img.size[1])
	print(str(xinc))
	print(str(yinc))
	print(str(xsize))
	print(str(ysize))
	
	for x in range(0, ((2 * xinc) +2)):
		draw.line(((x * 72), 0, (x * 72), ysize), fill=128)
		
	for y in range(0, ((2 * yinc) + 2)):
		draw.line((0, (y * 72), xsize, (y * 72)), fill=128)

	cubes = str(((2 * xinc)+1) * ((2 * yinc) + 1))
	#print(cubes + ' Rubik cubes required at this resolution')          EXPERIMENTAL
	#img.show()
	grid_save = img

	img.save('grid.png')
	return cubes
	del draw 																			#enlarges image and overlays grid in 9x9 panels

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
	global grid_save
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
	go_button.place(x=330, y=146)


def savefile():
	global img_out
	
	if grid_enabled.get() == True:
		img_out = grid_save
		print('save file assigned as grid')
	else:
		print('save file assignment without grid')
		
	save_image_location = filedialog.asksaveasfilename(defaultextension=".png")						#gets the input file and labels as active file
	img_out.save(str(save_image_location))
	print('saved')


def zoom():													#resizes COPY of output image to simulate zoom
	print('zoom start')
	x, y, xoff, yoff = imresize(img_out, 700)
	zoomed_img_out = img_out.resize((x, y), p.Image.ANTIALIAS)							
	print('zoomed')
	zoomed_img_out.show()


def convert():												#the main body of the program

	global img_out1
	global img_out
	global random_enabled
	global grid_enabled
	global img_refine

	img_out=img_in 

	try:																	#check for invalid input and declare width, bright and contrast
		width = int(width_input.get())
		b = float(bri.get())
		c = float(con.get())
	except ValueError:
		box.showerror('Error', 'You must enter the width, brightness and contrast as a number')


	wpercent = (int(width) / float(img_out.size[0]))							#shrink image to specified width in pixels, maintaining aspect ratio
	hsize = int((float(img_out.size[1]) * float(wpercent)))

	img_out = img_out.resize((int(width), hsize), p.Image.ANTIALIAS)
	print('resizing')

	print('bright function started  - Brightness >> ' + str(b) + '  Contrast >> ' + str(c))											#apply brightness and contrast adjustments
	enhancer = ImageEnhance.Brightness(img_out)
	img_out = enhancer.enhance(b)
	enhancer = ImageEnhance.Contrast(img_out)
	img_out = enhancer.enhance(c)

	img_out = img_out.convert('L')												#convert to grey
	print('convert to greyscale')

	
	if green_enabled.get() == True:
		colour_quantity = 6
		print('green enabled')
	else:
		colour_quantity = 5

	img_out = img_out.convert('P', palette=Image.ADAPTIVE, colors=colour_quantity)					#reduce palette to 5 or 6 colours
	print('reducing pallete')

	#orange = [255, 128, 0,]
	#green = [0, 255, 0,]
	#blue = [0, 0, 255,]
	#red = [255, 0, 0,]
	#white = [255, 255, 255,]
	#yellow = [255, 255, 0,]
	#blank = [0, 0, 0,]


	#combo = (  white,           yellow,        orange,         red,            blue)
	#combo = [[255, 255, 255,], [255, 255, 0,], [252, 102, 0,], [255, 0, 0,], [0, 0, 255,]]

	#modified palette better separation of shades
	combo = [[255, 255, 255,], [239, 253, 95,], [255, 116, 23,], [255, 40, 0,], [0, 70, 173,]]			#set colours in palette


	#rubic palette
	#combo = [[255, 255, 255,], [255, 213, 0,], [255, 88, 0,], [255, 8, 0,], [0, 70, 173,]]

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
	img_out.putpalette(final)															#apply new palette

	print('initial image out size - x ' + str(img_out.size[0]) + ' / y ' + str(img_out.size[1]) + '\n')

	if grid_enabled.get() == True:															#grid function
		gridme = img_out
		grid(gridme)
	
	print('saved image out size - ')


	print('displayed image out size - ')
	x, y, xoff, yoff = imresize(img_out, 400)
	img_out = img_out.resize((x, y))														#resize the modified image for display in ui
	img_out1 = ptk.PhotoImage(img_out)

	output_image.image = img_out1															#the bloody placeholder
	output_image.configure(image=img_out1)													#update image in label
	output_image.place(x=400 + xoff, y=250 + yoff)											#place updated label with offsets taken from resize function

	zoom1 = p.Image.open("zoom.png")														#create and place the zoom button
	zoom_holder1 = ptk.PhotoImage(zoom1) 
	zoom_button = tk.Button(window, image=zoom_holder1, command=zoom, borderwidth=5)
	zoom_button.image = zoom_holder1	
	zoom_button.place(x=688, y=137)

	save_file_button = tk.Button(window, text='Save image file', command=savefile)
	save_file_button.place(x=650, y=55)

file = 'No file loaded'
active_file_label = tk.Label(window, text=('Active file >>    ' + file))					#active filename text on UI
active_file_label.place(x=5, y=5)

background = p.Image.open('background.jpg')													#set coloured background to fill dead space whe non square images used
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
open_file_button.place(x=650, y=20)

width_label = tk.Label(window, text='Width in pixels ')
width_label.place(x=15, y=45)

width_input = tk.Entry(window, width=5)
width_input.insert(tk.END, '75')
width_input.place(x=150, y=45)
width_input.focus()

brilabel = tk.Label(window, text='Brightness').place(x=15, y=75)
bri = tk.Entry(window, width=5)
bri.insert(tk.END, '1.0')
bri.place(x=150, y=75)
bri.focus()

conlabel = tk.Label(window, text='Contrast').place(x=15, y=105)
con = tk.Entry(window, width=5)
con.insert(tk.END, '1.0')
con.place(x=150, y=105)

green_enabled = tk.BooleanVar()
green_enabled.set(False)
green_checkbox = tk.Checkbutton(window, text='Green enabled', variable=green_enabled)
green_checkbox.place(x=200, y=185)

palette_standard = tk.Radiobutton(window, text='Standard palette', command=random0)
palette_random = tk.Radiobutton(window, text='Random palette', value=1, command=random1)
palette_standard.place(x=5, y=185)
palette_random.place(x=5, y=160)

grid_enabled = tk.BooleanVar()
grid_enabled.set(False)
grid_checkbox = tk.Checkbutton(window, text='Grid enabled', var = grid_enabled)
grid_checkbox.place(x=200, y=160)


window.mainloop()