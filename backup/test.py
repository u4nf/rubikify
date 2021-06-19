import tkinter as tk
import PIL as p
import PIL.ImageTk as ptk
from tkinter import filedialog
from PIL import Image
import random


window = tk.Tk()
window.title('Rubikify v1.0')
window.geometry('100x100')



org_img_holder = p.Image.open('wide.png')
print('input - W ' + str(org_img_holder.size[0]) + ' /  H ' + str(org_img_holder.size[1]))



width = float(org_img_holder.size[1])
wpercent = (width / float(org_img_holder.size[0]))
hsize = int((float(org_img_holder.size[1]) * float(wpercent)))
		

if width > hsize:
	org_img_holder = org_img_holder.resize((100, int(100 * wpercent )), p.Image.ANTIALIAS)
else:
	org_img_holder = org_img_holder.resize((int(100 / wpercent), 100), p.Image.ANTIALIAS)
print('resize to scale complete - output - W ' + str(org_img_holder.size[0]) + ' /  H ' + str(org_img_holder.size[1]))



print('before photoimage - W ' + str(org_img_holder.size[0]) + ' /  H ' + str(org_img_holder.size[1]))

						
org_img_holder1 = ptk.PhotoImage(org_img_holder)
org_img_holder = tk.Label(window, image=org_img_holder1)
original_image =tk.Label(window, image=org_img_holder1)
original_image.image = org_img_holder1
#print('before place - W ' + str(org_img_holder.size[0]) + ' /  H ' + str(org_img_holder.size[1]))

original_image.place(x=0, y=0)




window.mainloop()

	
	




	
	



