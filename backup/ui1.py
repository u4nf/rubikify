import tkinter as tk
import PIL as p
import PIL.ImageTk as ptk
from tkinter import filedialog



window = tk.Tk()
window.title('Rubikify v1.0')
window.geometry('400x500')



def getfile():

	original_image_location = filedialog.askopenfilename()
	file_label = original_image_location[-35:]
	active_file_label.configure(text=('Active file >> ....' + str(file_label)))


	no_file_in_image.destroy()

	org_img_holder = p.Image.open(str(original_image_location)).resize((200,200))
	org_img_holder1 = ptk.PhotoImage(org_img_holder)

	original_file_image = tk.Label(window, image=org_img_holder1)
	original_file_image.image = org_img_holder1										#the bloody placeholder
	original_file_image.place(x=0, y=300)

	
	rubikify_button = tk.Button(window, text='Rubikify', font=('Impact', 20))
	rubikify_button.place(x=240, y=80)
	

file = 'No file loaded'
active_file_label = tk.Label(window, text=('Active file >>    ' + file))
active_file_label.place(x=5, y=5)


no_file_in_holder = p.Image.open('noinput.png').resize((200,200))							#no input image
no_file_in_holder1 = ptk.PhotoImage(no_file_in_holder)
no_file_in_holder = tk.Label(window, image=no_file_in_holder1)
no_file_in_image =tk.Label(window, image=no_file_in_holder1)
no_file_in_image.image = no_file_in_holder1
no_file_in_image.place(x=0, y=300)

no_file_holder = p.Image.open('nooutput.png').resize((200,200))							#no output image
no_file_holder1 = ptk.PhotoImage(no_file_holder)
no_file_holder = tk.Label(window, image=no_file_holder1)
no_file_image =tk.Label(window, image=no_file_holder1)
no_file_image.image = no_file_holder1
no_file_image.place(x=201, y=300)


open_file_button = tk.Button(window, text='Open image file', command=getfile)
open_file_button.place(x=240, y=40)

width_label = tk.Label(window, text='Width in pixels ')
width_label.place(x=15, y=45)

width_input = tk.Entry(window, width=5)
width_input.insert(tk.END, '60')
width_input.place(x=135, y=45)
width = width_input.get()
width_input.focus()

green_enabled = tk.BooleanVar()
green_enabled.set(False)
green_checkbox = tk.Checkbutton(window, text='Green enabled', var = green_enabled)
green_checkbox.place(x=5, y=175)

grid_enabled = tk.BooleanVar()
grid_enabled.set(False)
grid_checkbox = tk.Checkbutton(window, text='Grid enabled', var = grid_enabled, state=tk.DISABLED)
grid_checkbox.place(x=5, y=200)

random0 = tk.BooleanVar()
random1 = tk.BooleanVar()
palette_standard = tk.Radiobutton(window, text='Standard palette', command=random0)
palette_random = tk.Radiobutton(window, text='Random palette', value=1, command=random1)
palette_standard.place(x=5, y=135)
palette_random.place(x=5, y=110)

def random0():
	random_enabled = False

def random1():
	random_enabled = True




















window.mainloop()