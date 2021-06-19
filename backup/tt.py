import tkinter as tkr
import PIL as p
import PIL.ImageTk as ptk


window = tkr.Tk()
window.title('Rubikify v1.0')
window.geometry('400x500')

file = 'No file loaded'
active_file_label = tkr.Label(window, text=('Active file >>    ' + file))
active_file_label.grid(column=0, row=0)


def getfile():
	file = tkr.filedialog.askopenfilename()
	file_label = file[-35:]
	active_file_label.configure(text=('Active file >> ....' + str(file_label)))
	
	original_image = p.Image.open(str(file)).resize((200,200))
	ph = ptk.PhotoImage(original_image)

	original_image_label = tkr.Label(window, image=ph)
	original_image_label.grid(column=0, row=7)

	#panel1.pack(side = LEFT)

open_file_button = tkr.Button(window, text='Open image file', command=getfile)
open_file_button.grid(column=0, row=1)


#btn = Button(window, text='Rubikify', command= rubikify_clicked, font=('Impact', 20))
rubikify_button = tkr.Button(window, text='Rubikify', font=('Impact', 20))
rubikify_button.grid(column=0, row=6)

width_label = tkr.Label(window, text='Width in pixels ')
width_label.grid(column=0, row=2)

width_input = tkr.Entry(window, width=5)
width_input.grid(column=1, row=2)
width = width_input.get()
width_input.focus()

green_enabled = tkr.BooleanVar()
green_enabled.set(False)
green_checkbox = tkr.Checkbutton(window, text='Green enabled', var = green_enabled)
green_checkbox.grid(column=0, row=3)

grid_enabled = tkr.BooleanVar()
grid_enabled.set(False)
grid_checkbox = tkr.Checkbutton(window, text='Grid enabled', var = grid_enabled)
grid_checkbox.grid(column=0, row=4)

random0 = tkr.BooleanVar()
random1 = tkr.BooleanVar()
palette_standard = tkr.Radiobutton(window, text='Standard palette', value=1, command=random0)
palette_random = tkr.Radiobutton(window, text='Random palette (x10)', value=2, command=random1)
palette_standard.grid(column=0, row=5)
palette_random.grid(column=1, row=5)

def random0():
	random_enabled = False

def random1():
	random_enabled = True























#def rubikify_clicked():
	

window.mainloop()
