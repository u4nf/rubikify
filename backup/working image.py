import tkinter as tkr
import PIL as p
import PIL.ImageTk as ptk

window = tkr.Tk()

window.title('test')
window.geometry('650x300')

pic = "5.png"
pic1 = p.Image.open(pic)
photo = ptk.PhotoImage(pic1)

label1 = tkr.Label(window, image=photo)
label1.pack()




window.mainloop()



