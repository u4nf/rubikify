import tkinter as tk
import tkinter.messagebox as box
import PIL as p
import PIL.ImageTk as ptk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageEnhance
import random



window = tk.Tk()
window.title('Rubikify v1.0')
#window.iconbitmap('cubelogo.ico')
window.geometry('800x650')

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


def refine():

	def funcbase():
		pass
	def funcd1():
		pass
	def funcd2():
		pass
	def funcu1():
		pass
	def funcu2():
		pass

	init_brightness = 1

	global img_out

	print('refine function started')
	refinewindow = tk.Toplevel()
	refinewindow.title('Rubikify refine')
	refinewindow.geometry('1000x500')
	


	x, y, xoff, yoff = imresize(img_out, 200)
	img_base = img_out.resize((x, y))														
	#img_base = ptk.PhotoImage(img_base)

	


	bri = -0.2
	enhancer = ImageEnhance.Brightness(img_base)
	img_d1 = enhancer.enhance(init_brightness + bri)

	img_d1 = ptk.PhotoImage(img_d1)
	img_base = ptk.PhotoImage(img_base)

	base_button = tk.Button(refinewindow, image=img_base, command=funcbase, borderwidth=1)
	base_button.place(x=310, y=10)


	d1 = tk.Button(refinewindow, image=img_d1, command=funcd1, borderwidth=1)
	d1.place(x=160, y=10)
	
	#d2 =   tk.Label(refine, text='d1'),place(x=10, y=10)
	#d1 =   tk.Label(refine, text='d2').place(x=160, y=10)
	#u1 =   tk.Label(refine, text='u1').place(x=460, y=10)
	#u2 =   tk.Label(refine, text='u2').place(x=610, y=10)
	
	refinewindow.mainloop()

zoom1 = p.Image.open("zoom.png")														#create and place the zoom button
zoom_holder1 = ptk.PhotoImage(zoom1) 
zoom_button = tk.Button(window, image=zoom_holder1, command=refine, borderwidth=5)
zoom_button.image = zoom_holder1	
zoom_button.place(x=688, y=137)


img_out = p.Image.open('no.jpg')



window.mainloop()