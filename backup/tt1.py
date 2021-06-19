import tkinter as tk
import PIL as p
import PIL.ImageTk as ptk
from tkinter import filedialog
from PIL import Image
import random


window = tk.Tk()
window.title('Rubikify v1.0')
window.geometry('400x400')







def imresize(input_image, max_size):

	width = float(input_image.size[1])
	wpercent = (width / float(input_image.size[0]))
	hsize = int((float(input_image.size[1]) * float(wpercent)))
		

	if width > hsize:
		x = max_size
		y = max_size * wpercent

	else:
		x = max_size / wpercent
		y = max_size
	x = int(x)
	y = int(y)
	return(x, y)



org_img_holder = p.Image.open('tall.png')
print('input - W ' + str(org_img_holder.size[0]) + ' /  H ' + str(org_img_holder.size[1]))


x, y = imresize(org_img_holder, 400)
print('imresize x = ' + str(x) + ' // y = ' + str(y))
org_img_holder = org_img_holder.resize((x, y), p.Image.ANTIALIAS)					


org_img_holder1 = ptk.PhotoImage(org_img_holder)
org_img_holder = tk.Label(window, image=org_img_holder1)
original_image =tk.Label(window, image=org_img_holder1)
original_image.image = org_img_holder1

original_image.place(x=0, y=0)




window.mainloop()

	
	



