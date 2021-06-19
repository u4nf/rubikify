from tkinter import *
from tkinter import filedialog

window = Tk()
window.title('Rubikify v1.0')
window.geometry('400x500')

file = 'No file loaded'
active_file_label = Label(window, text=('Active file >>    ' + file))
active_file_label.grid(column=0, row=0)


def getfile():
	file = filedialog.askopenfilename()
	file_label = file[-35:]
	active_file_label.configure(text=('Active file >> ....' + file_label))


open_file_button = Button(window, text='Open image file', command=getfile)
open_file_button.grid(column=0, row=1)


#btn = Button(window, text='Rubikify', command= rubikify_clicked, font=('Impact', 20))
rubikify_button = Button(window, text='Rubikify', font=('Impact', 20))
rubikify_button.grid(column=0, row=6)

width_label = Label(window, text='Width in pixels ')
width_label.grid(column=0, row=2)

width_input = Entry(window, width=5)
width_input.grid(column=1, row = 2)
width = width_input.get()
width_input.focus()

green_enabled = BooleanVar()
green_enabled.set(False)
green_checkbox = Checkbutton(window, text='Green enabled', var = green_enabled)
green_checkbox.grid(column=0, row=3)

grid_enabled = BooleanVar()
grid_enabled.set(False)
grid_checkbox = Checkbutton(window, text='Grid enabled', var = grid_enabled)
grid_checkbox.grid(column=0, row=4)

random0 = BooleanVar()
random1 = BooleanVar()
palette_standard = Radiobutton(window, text='Standard palette', value=1, command=random0)
palette_random = Radiobutton(window, text='Random palette (x10)', value=2, command=random1)
palette_standard.grid(column=0, row=5)
palette_random.grid(column=1, row=5)

def random0():
	random_enabled = False

def random1():
	random_enabled = True























#def rubikify_clicked():
	

window.mainloop()
