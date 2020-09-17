"""Author : Tanish sarmah
Date:17/09/2020"""
from tkinter import *
root = Tk()
root.geometry("400x300")
# Labels

Label(root, text="Window Resizer",
      font="comicsansms 20 bold").grid(row="0", column="1")

height = Label(root, text="Enter The width",
               font="comicsansms 10 bold").grid(row="2", column="0", pady=20,
                                                padx=20)
width = Label(root, text="Enter The heigth",
              font="comicsansms 10 bold").grid(row="3", column="0", pady=20,
                                               padx=20)
root.title("Window Resizer")
# Values for entries

heightvl = StringVar()
widthvl = StringVar()
# Entries
wen = Entry(root, textvariable=widthvl)
hen = Entry(root, textvariable=heightvl)
wen.grid(row="2", column="1")
hen.grid(row="3", column="1")


def resize():
    "Resizes the GUI window"
    w = wen.get()
    h = hen.get()
    root.geometry(f"{w}x{h}")


# Button
Button(root, text="Apply", command=resize).grid(row="4", column="1", pady="30")


root.mainloop()
