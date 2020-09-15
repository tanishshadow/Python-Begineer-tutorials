from datetime import datetime
from tkinter import *
from PIL import Image, ImageTk
import os
root = Tk()
root.title(os.getcwd())
root.configure(bg="yellow")
# Reading content in files
with open("1.txt", "r+") as f:
    content1 = f.read()
with open("2.txt", "r+") as f1:
    content2 = f1.read()
with open("3.txt", "r+") as f2:
    content3 = f2.read()
with open("4.txt", "r+") as f3:
    content4 = f3.read()


# Heading
root.geometry("1000x900")
Label(root, text="Tanish's ", fg="white", bg="black",
      font="timesnewroman 20 bold", padx="180", pady="30").grid(row="0", column="0", sticky="E")
Label(root, text="News", fg="white", bg="black",
      font="timesnewroman 20 bold", padx="400", pady="30").grid(row="0", column='1')

# TODO set the date of hte newspaper using in datetime module
Label(root, text=datetime.now(), fg="red",
      font="comicsansms 10 bold").grid(row="1", column="1")

#         News

news1 = Label(root, bg="grey", fg="white", padx="60", pady="30",
              text=content1).grid(row="2", column="0", pady="10")
news2 = Label(root, bg="grey", fg="white", padx="40", pady="30",
              text=content2).grid(row="3", column="0", pady="10")
news3 = Label(root, bg="grey", fg="white", padx="60", pady="30",
              text=content3).grid(row="4", column="0", pady="10")



# IMAGES

img1 = Image.open("1.jpg")
r_img1 = img1.resize((400, 150), Image.HAMMING)
photo = ImageTk.PhotoImage(r_img1)
img_lb = Label(root, image=photo, padx="20", pady="10").grid(
    row="2", column="1", pady="2")

img2 = Image.open("2.jpg")
r_img2 = img2.resize((400, 150), Image.HAMMING)
photo2 = ImageTk.PhotoImage(r_img2)
img_lb2 = Label(root, image=photo2, padx="20", pady="10").grid(
    row="3", column="1", pady="2")

img3 = Image.open("3.jpg")
r_img3 = img3.resize((400, 200), Image.HAMMING)
photo3 = ImageTk.PhotoImage(r_img3)
img_lb3 = Label(root, image=photo3, padx="20", pady="10").grid(
    row="4", column="1", pady="2")
    
# Event loop

root.mainloop()
