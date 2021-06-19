import tkinter as tk
import PIL as p
import PIL.ImageTk as ptk
from tkinter import filedialog
from PIL import Image
import random



window = tk.Tk()
window.title('Rubikify v1.0')
window.geometry('800x650')

org_img_holder ='none'
random_enabled = False



def getfile():

	global org_img_holder

	original_image_location = filedialog.askopenfilename()
	file_label = original_image_location[-35:]
	active_file_label.configure(text=('Active file >> ....' + str(file_label)))


	no_file_in_image.destroy()

	org_img_holder = p.Image.open(str(original_image_location))

	resize_to_scale(org_img_holder, 400)

	#width = float(org_img_holder.size[1])
	#wpercent = (width / float(org_img_holder.size[0]))
	#hsize = int((float(org_img_holder.size[1]) * float(wpercent)))
	

	#if width > hsize:
	#	org_img_holder = org_img_holder.resize((400, int(400 / wpercent )), p.Image.ANTIALIAS)
	#else:
	#	org_img_holder = org_img_holder.resize((int(400 / wpercent), 400), p.Image.ANTIALIAS)



	print('resizing')






	#resize((400,400))
	org_img_holder1 = ptk.PhotoImage(org_img_holder.resize(400,300))
	original_file_image = tk.Label(window, image=org_img_holder1)
	original_file_image.image = org_img_holder1
									#the bloody placeholder

	print('potoimage scale before place complete - output - W ' + str(org_img_holder.size[0]) + ' /  H ' + str(org_img_holder.size[1]))


	original_file_image.place(x=-1, y=250)

	go = p.Image.open("go.png")
	go_holder1 = ptk.PhotoImage(go)
	go_button = tk.Button(window, image=go_holder1, command=convert, borderwidth=5)
	go_button.image = go_holder1	
	
	go_button.place(x=330, y=146)




def resize_to_scale(input_image, max_out_dim):
	max_out_dim = 400

	width = float(input_image.size[1])
	wpercent = (width / float(input_image.size[0]))
	hsize = int((float(input_image.size[1]) * float(wpercent)))
	

	if width > hsize:
		input_image = input_image.resize((max_out_dim, int(max_out_dim / wpercent )), p.Image.ANTIALIAS)
	else:
		input_image = input_image.resize((int(max_out_dim / wpercent), max_out_dim), p.Image.ANTIALIAS)
	print('resize to scale complete - output - W ' + str(input_image.size[0]) + ' /  H ' + str(input_image.size[1]))

	

def zoom():
	zoomed_img = img.resize((int(650), 650), p.Image.ANTIALIAS)
	print('zoomed')
	zoomed_img.show()


def convert():

	global img
	global random_enabled
	global grid_enabled

	img=org_img_holder 

	#random_enabled = True

	width = width_input.get()

	wpercent = (int(width) / float(img.size[0]))
	hsize = int((float(img.size[1]) * float(wpercent)))

	img = img.resize((int(width), hsize), p.Image.ANTIALIAS)
	print('resizing')

	img = img.convert('L')
	print('convert to greyscale')

	print(grid_enabled.get())
	#random_enabled = False

	if green_enabled.get() == True:
		colour_quantity = 6
		print('green enabled')
	else:
		colour_quantity = 5

	img = img.convert('P', palette=Image.ADAPTIVE, colors=colour_quantity)
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
	print('final palette......\n' + str(combo))

	img.putpalette(final)

	no_file_image.destroy()

	img = img.resize((400,400))
	img1 = ptk.PhotoImage(img)

	new_image = tk.Label(window, image=img1)
	new_image.image = img1										#the bloody placeholder
	new_image.place(x=399, y=250)


	zoom_button = tk.Button(window, text='Zoom', command=zoom)
	zoom_button.place(x=700, y=135)

	img.save('resize.png')
	print('Saved to {} pixels wide.'.format(str(width)))



file = 'No file loaded'
active_file_label = tk.Label(window, text=('Active file >>    ' + file))
active_file_label.place(x=5, y=5)


no_file_in_holder = p.Image.open('noinput.png').resize((400,400))							#no input image
no_file_in_holder1 = ptk.PhotoImage(no_file_in_holder)
no_file_in_holder = tk.Label(window, image=no_file_in_holder1)
no_file_in_image =tk.Label(window, image=no_file_in_holder1)
no_file_in_image.image = no_file_in_holder1
no_file_in_image.place(x=-1, y=250)

no_file_holder = p.Image.open('nooutput.png').resize((400,400))							#no output image
no_file_holder1 = ptk.PhotoImage(no_file_holder)
no_file_holder = tk.Label(window, image=no_file_holder1)
no_file_image =tk.Label(window, image=no_file_holder1)
no_file_image.image = no_file_holder1
no_file_image.place(x=399, y=250)


logo_holder = p.Image.open('cube_logo.png').resize((100,110))							#logo image
logo_holder1 = ptk.PhotoImage(logo_holder)
logo_holder = tk.Label(window, image=logo_holder1)
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
#width = width_input.get()
width_input.focus()


def random0():
	global random_enabled
	random_enabled = False

def random1():
	global random_enabled
	random_enabled = True

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
grid_checkbox = tk.Checkbutton(window, text='Grid enabled', var = grid_enabled, state=tk.DISABLED)
grid_checkbox.place(x=200, y=110)






window.mainloop()