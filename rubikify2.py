import tkinter as tk
import tkinter.messagebox as box
import PIL as p
import PIL.ImageTk as ptk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageEnhance, ImageFont
import random


swap_list = []
window = tk.Tk()
window.title('Rubikify v2.0')
window.iconbitmap("@" + "cube_logo.xbm")
window.geometry('800x650')


def portrait_mode():
	global custom_mode_active
	custom_mode_active = False
	print('Portrait mode active')


def custom_mode():
	global palette, colour_quantity, custom_mode_active
	custom_mode_active = True
	print('Custom mode active')
	custom_window = tk.Toplevel()
	custom_window.title('Custom mode')
	custom_window.geometry('700x250')

	colours = {'orange':[255, 165, 0,], 'green':[0, 128, 0,], 'blue':[0, 0, 255,], 'red':[255, 0, 0,], 'white':[255, 255, 255,], 'yellow':[255, 255, 0,], 'black':[0, 0, 0,]}



	def set_colours():
		def colour_swap(colour):
			global swap_list, temp_palette, palette, ribbon_frame

			swap_list.append(colours[colour])

			if len(swap_list) == 2:
				print(temp_palette)
				a = temp_palette.index(swap_list[0])
				b = temp_palette.index(swap_list[1])

				temp_palette[a] = swap_list[1]
				temp_palette[b] = swap_list[0]				
				print(temp_palette)

				swap_list = []
				palette = []
				ribbon_frame.destroy()   	#refresh colour ribbon
				ribbon_frame = tk.LabelFrame(custom_window, text='Active palette, click to swap colours', height = 100, width=500)
				ribbon_frame.pack(fill='x', side='top')

				for a,i in enumerate(temp_palette):      #re do the colour ribbon based on the new order

					if temp_palette[a] == colours['white']:
						white_rib = tk.Button(ribbon_frame, bg='white', command= lambda: colour_swap('white'))
						white_rib.pack(expand=True, fill='x', side='left')

					if temp_palette[a] == colours['yellow']:
						yellow_rib = tk.Button(ribbon_frame, bg='yellow', command= lambda: colour_swap('yellow'))
						yellow_rib.pack(expand=True, fill='x', side='left')

					if temp_palette[a] == colours['orange']:
						orange_rib = tk.Button(ribbon_frame, bg='orange', command= lambda: colour_swap('orange'))
						orange_rib.pack(expand=True, fill='x', side='left')

					if temp_palette[a] == colours['green']:
						green_rib = tk.Button(ribbon_frame, bg='green', command= lambda: colour_swap('green'))
						green_rib.pack(expand=True, fill='x', side='left')

					if temp_palette[a] == colours['red']:
						red_rib = tk.Button(ribbon_frame, bg='red', command= lambda: colour_swap('red'))
						red_rib.pack(expand=True, fill='x', side='left')
					
					if temp_palette[a] == colours['blue']:
						blue_rib = tk.Button(ribbon_frame, bg='blue', command= lambda: colour_swap('blue'))
						blue_rib.pack(expand=True, fill='x', side='left')

				convert()


		global palette, ribbon_frame, temp_palette

		try:
			ribbon_frame.destroy()   	#refresh colour ribbon
		except:
			pass

		ribbon_frame = tk.LabelFrame(custom_window, text='Active palette, click to swap colours', height = 100, width=500)
		ribbon_frame.pack(fill='x', side='top')
	
		temp_palette = []
		palette = []
		colour_list = ['white', 'yellow', 'orange', 'green', 'red', 'blue']
		print('Clear palette and colour count')

		if white_enabled.get() == True:
			temp_palette.append(colours['white'])
			white_rib = tk.Button(ribbon_frame, bg='white', command= lambda: colour_swap('white'))
			white_rib.pack(expand=True, fill='x', side='left')

		if yellow_enabled.get() == True:
			temp_palette.append(colours['yellow'])
			yellow_rib = tk.Button(ribbon_frame, bg='yellow', command= lambda: colour_swap('yellow'))
			yellow_rib.pack(expand=True, fill='x', side='left')

		if orange_enabled.get() == True:
			temp_palette.append(colours['orange'])
			orange_rib = tk.Button(ribbon_frame, bg='orange', command= lambda: colour_swap('orange'))
			orange_rib.pack(expand=True, fill='x', side='left')

		if green_enabled.get() == True:
			temp_palette.append(colours['green'])
			green_rib = tk.Button(ribbon_frame, bg='green', command= lambda: colour_swap('green'))
			green_rib.pack(expand=True, fill='x', side='left')

		if red_enabled.get() == True:
			temp_palette.append(colours['red'])
			red_rib = tk.Button(ribbon_frame, bg='red', command= lambda: colour_swap('red'))
			red_rib.pack(expand=True, fill='x', side='left')
		
		if blue_enabled.get() == True:
			temp_palette.append(colours['blue'])
			blue_rib = tk.Button(ribbon_frame, bg='blue', command= lambda: colour_swap('blue'))
			blue_rib.pack(expand=True, fill='x', side='left')
		
		if random_enabled.get() == True:
			random.shuffle(temp_palette)

		print('Custom palette - ' + str(palette))



	def show_options():
		global green_enabled, blue_enabled, red_enabled, orange_enabled, yellow_enabled, white_enabled, random_enabled
		

		colour_checkbox_frame = tk.Frame(custom_window, height=600, width=300)
		colour_checkbox_frame.pack(side='left',fill='y')		

		green_enabled = tk.BooleanVar()
		green_enabled.set(False)
		green_checkbox = tk.Checkbutton(colour_checkbox_frame, text='Green enabled   ', bg='green', var= green_enabled)
		green_checkbox.pack(expand=True,fill='both')

		blue_enabled = tk.BooleanVar()
		blue_enabled.set(False)
		blue_checkbox = tk.Checkbutton(colour_checkbox_frame, text='Blue enabled     ', bg='blue', var= blue_enabled)
		blue_checkbox.pack(expand=True,fill='both')

		red_enabled = tk.BooleanVar()
		red_enabled.set(False)
		red_checkbox = tk.Checkbutton(colour_checkbox_frame, text='Red enabled      ', bg='red', var= red_enabled)
		red_checkbox.pack(expand=True,fill='both')

		orange_enabled = tk.BooleanVar()
		orange_enabled.set(False)
		orange_checkbox = tk.Checkbutton(colour_checkbox_frame, text='Orange enabled ', bg='orange', var= orange_enabled)
		orange_checkbox.pack(expand=True,fill='both')

		yellow_enabled = tk.BooleanVar()
		yellow_enabled.set(False)
		yellow_checkbox = tk.Checkbutton(colour_checkbox_frame, text='Yellow enabled  ', bg='yellow', var= yellow_enabled)
		yellow_checkbox.pack(expand=True,fill='both')

		white_enabled = tk.BooleanVar()
		white_enabled.set(False)
		white_checkbox = tk.Checkbutton(colour_checkbox_frame, text='White enabled   ', bg='white', var= white_enabled)
		white_checkbox.pack(expand=True,fill='both')

		custom_go = p.Image.open("go.png")													#create and place the go button
		custom_go_holder1 = ptk.PhotoImage(custom_go) 
		custom_go_button = tk.Button(custom_window, image=custom_go_holder1, command=convert, borderwidth=8, relief='ridge')
		custom_go_button.image = custom_go_holder1	
		custom_go_button.pack(side='right', fill='y')

		set_colours_button1 = p.Image.open('colour.jpeg')
		set_colours_button1_holder = ptk.PhotoImage(set_colours_button1)
		set_colours_button = tk.Button(custom_window, image=set_colours_button1_holder, compound='center', text='SET PALETTE', command=set_colours)
		set_colours_button.image = set_colours_button1_holder
		set_colours_button.pack(side='bottom', fill='x')

		random_enabled = tk.BooleanVar()
		random_enabled.set(False)
		palette_random = tk.Checkbutton(custom_window, text='Randomise palette', var=random_enabled)
		palette_random.pack(side='bottom')

	show_options()
	custom_window.mainloop()


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
		img.save('txtimg.png')

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

	img.save('grid.png')
	#img.show()
	add_text(img, offset, bps)
	del draw 												#enlarges image and overlays grid in 9x9 panels


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
	global grid_save, img_in, grid_enabled
	#global img_in

	original_image_location = filedialog.askopenfilename()								#gets the input file and labels as active file
	file_label = original_image_location[-22:]
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

	portrait_button = tk.Radiobutton(window, text="Portrait Mode", command=portrait_mode)
	custom_button = tk.Radiobutton(window, text="Custom mode", value=1, command=custom_mode)
	portrait_button.place(x=5, y=210)
	custom_button.place(x=5, y=180)

	grid_enabled = tk.BooleanVar()
	grid_enabled.set(True)
	grid_checkbox = tk.Checkbutton(window, text='Grid enabled', var = grid_enabled)
	grid_checkbox.place(x=500, y=210)




def savefile():
	global img_out
	
	if grid_enabled.get() == True:
		img_out = grid_save
		print('save file assigned as grid')
	else:
		print('save file assignment without grid')
		
	save_image_location = filedialog.asksaveasfilename(defaultextension=".png")			#gets the input file and labels as active file
	img_out.save(str(save_image_location))
	print('saved')


def zoom():													#resizes COPY of output image to simulate zoom
	print('zoom start')
	x, y, xoff, yoff = imresize(img_out, 1000)
	zoomed_img_out = img_out.resize((x, y), p.Image.ANTIALIAS)							
	print('zoomed')
	zoomed_img_out.show()


#the main body of the program
def convert():												

	global img_out1, img_out, grid_enabled, temp_palette

	img_out=img_in 

	if custom_mode_active == True:
		palette = []
		colour_quantity = len(temp_palette)
	else:
		#portrait mode
		palette = [255, 255, 255, 255, 255, 0, 255, 165, 0, 255, 0, 0, 0, 0, 255]
		temp_palette = []
		colour_quantity = 5



	try:
		for a in range(len(temp_palette)):					#mutates list of lists to palette list
			for b in range(0,3):
				palette.append(temp_palette[a][b])
	except:
		pass

	#check for invalid input and declare width, bright and contrast
	try:													
		width = int(width_input.get())
		b = float(bri.get())
		c = float(con.get())
	except ValueError:
		box.showerror('Error', 'You must enter the width, brightness and contrast as a number')

	#shrink image to specified width in pixels, maintaining aspect ratio
	wpercent = (int(width) / float(img_out.size[0]))							
	hsize = int((float(img_out.size[1]) * float(wpercent)))

	img_out = img_out.resize((int(width), hsize), p.Image.ANTIALIAS)
	print('resizing')

	print('set brightness / contrast')											
	enhancerb = ImageEnhance.Brightness(img_out)
	img_out = enhancerb.enhance(b)
	enhancerc = ImageEnhance.Contrast(img_out)
	img_out = enhancerc.enhance(c)

	print('convert to greyscale')
	img_out = img_out.convert('L')												


	#reduce original palette to 'colour_quantity'
	print('colour quantity ' + str(colour_quantity))
	img_out = img_out.convert('P', palette=Image.ADAPTIVE, colors=colour_quantity)			
	print('reducing palette')

	print('final palette......\n' + str(palette) + '\n')
	img_out.putpalette(palette)															

	print('initial image out size - x ' + str(img_out.size[0]) + ' / y ' + str(img_out.size[1]) + '\n')

	if grid_enabled.get() == True:														
		gridme = img_out
		grid(gridme)
	
	x, y, xoff, yoff = imresize(img_out, 400)
	img_out = img_out.resize((x, y))														#resize the modified image for display in ui
	img_out1 = ptk.PhotoImage(img_out)

	output_image.image = img_out1															#the bloody placeholder
	output_image.configure(image=img_out1)													#update image in label
	output_image.place(x=400 + xoff, y=250 + yoff)											#place updated label with offsets taken from resize function

	print('\n\n ---------------------------------------------------------\n\n')

	zoom1 = p.Image.open("zoom.png")														#create and place the zoom button
	zoom_holder1 = ptk.PhotoImage(zoom1) 
	zoom_button = tk.Button(window, image=zoom_holder1, command=zoom, borderwidth=5)
	zoom_button.image = zoom_holder1	
	zoom_button.place(x=688, y=137)

	save_file_button = tk.Button(window, text=' Save image file', command=savefile)
	save_file_button.place(x=625, y=90)

file = 'No file loaded'
active_file_label = tk.Label(window, text=('Active file >>    ' + file))					#active filename text on UI
active_file_label.place(x=450, y=5)

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
open_file_button.place(x=625, y=40)

width_label = tk.Label(window, text='Width in pixels ')
width_label.place(x=15, y=40)

width_input = tk.Entry(window, width=5)
width_input.insert(tk.END, '75')
width_input.place(x=150, y= 40)
width_input.focus()

#brightness and contrast manipulation
brilabel = tk.Label(window, text='Brightness').place(x=15, y=90)
bri = tk.Entry(window, width=5)
bri.insert(tk.END, '1.0')
bri.place(x=150, y=90)
bri.focus()

conlabel = tk.Label(window, text='Contrast').place(x=15, y=140)
con = tk.Entry(window, width=5)
con.insert(tk.END, '1.0')
con.place(x=150, y=140)

def bri_inc():
	bri_temp = (float(bri.get()) + 0.1)
	bri.delete(0, 'end')
	bri.insert(tk.END, bri_temp)
	convert()

def bri_dec():
	bri_temp = (float(bri.get()) - 0.1)
	if bri_temp > 0.1:
		bri.delete(0, 'end')
		bri.insert(tk.END, bri_temp)
	convert()
	
def con_inc():
	con_temp = (float(con.get()) + 0.1)
	con.delete(0, 'end')
	con.insert(tk.END, con_temp)
	convert()

def con_dec():
	con_temp = (float(con.get()) - 0.1)
	if con_temp > 0.1:
		con.delete(0, 'end')
		con.insert(tk.END, con_temp)
	convert()

bri_dec = tk.Button(window, bg = 'red', fg = 'white', text='-', bd = 7, width = 1, command=bri_dec).place(x=230, y=87)
bri_inc = tk.Button(window, bg = 'green', fg = 'white', text='+', bd = 7, width = 1, command=bri_inc).place(x=275, y=87)

con_dec = tk.Button(window, bg = 'blue', fg = 'white', text='-', bd = 7, width = 1, command=con_dec).place(x=230, y=127)
con_inc = tk.Button(window, bg = 'orange', fg = 'white', text='+', bd = 7, width = 1, command=con_inc).place(x=275, y=127)


portrait_mode()

window.mainloop()