import tkinter as tk
 
app = tk.Tk() 
app.geometry('150x100')


def boop():
	chkValue = not chkValue
	print(chkValue)

chkValue = tk.IntVar() 
chkValue.set(True)
 
chkExample = tk.Checkbutton(app, text='Check Box', command=boop) 
chkExample.grid(column=0, row=0)





app.mainloop()








