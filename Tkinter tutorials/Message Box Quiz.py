from tkinter import *
from tkinter import messagebox as msg
root = Tk()
root.geometry("700x600")
root.title("Harry is awesome")


def funcbot():
    """Function for simple captcha verification by asking yes or no"""
    msg.askyesno("Captcha", "Are you human")


def funcpr():
    msg.showwarning("Security",
                    "Warning! The link may be harmful. ")


# TODO: Captcha verification-----
main = Menu(root, tearoff="0")
m2 = Menu(main, tearoff="0")
m2.add_command(label="Captcha", command=funcbot)
main.add_cascade(label="Verify", menu=m2)
# config is like packing a button
root.config(menu=main)
# TODO: Prank
m3 = Menu(main, tearoff="0")
m3.add_command(label="Harmful Content", command=funcpr)
main.add_cascade(label="Content", menu=m3)
root.config(menu=main)

root.configure(bg="sky blue")
root.configure(bg="black")
m2 = Menu(main, tearoff="0")


root.mainloop()
