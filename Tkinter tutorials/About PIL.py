from tkinter import *
from PIL import Image, ImageTk
from os import getcwd
root = Tk()
root.title(getcwd())
root.geometry("955x944")
img = Image.open("photo.jpg")
# i_crop=img.crop((0,0,955,944))
# photo=ImageTk.PhotoImage(i_crop)
# photo = ImageTk.PhotoImage(img)


r_img=img.resize((img.width//10,img.height//10),Image.LANCZOS)
photo=ImageTk.PhotoImage(r_img)
Label(root,image=photo).pack()

Button(root,text="RESIZE").pack()
root.mainloop()
