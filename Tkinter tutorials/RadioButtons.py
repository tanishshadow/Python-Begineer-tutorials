from tkinter import *
from os import getcwd
from tkinter import messagebox as msg
root = Tk()
root.geometry("600x500")
# var = IntVar()
# var.set(1)
var = StringVar()
var.set("some")

root.title("RadioButtons" + getcwd())
Label(root, text="Select any food items from the following options",
      fg="red", font="timesnewroman 13 bold").pack()
# Radiobuttons------
# rb1 = Radiobutton(root, text="Dosa", variable=var, value=1).pack(anchor="w",
#                                                                  pady=10)
# rb2 = Radiobutton(root, text="Pizza", variable=var,
#                   value=2).pack(anchor="w", pady=10)
# rb3 = Radiobutton(root, text="Burger", variable=var,
#                   value=3).pack(anchor="w", pady=10)
# rb4 = Radiobutton(root, text="Momo", variable=var,n
#                   value=4).pack(anchor="w", pady=10)
# rb5 = Radiobutton(root, text="Samosa", variable=var,
#                   value=5).pack(anchor="w", pady=10)
# All these can be done by using for loop as follows


def order():
    msg.showinfo("Order", F"We have recieved your order for {var.get()}")


food_items = ["Dosa", "Pizza", "Burger", "Momo", "Samosa"]
# var_vl = var.get()

for food in food_items:
    Radiobutton(root, text=food, variable=var,
                value=food).pack(anchor="w", pady="10")


def newWindwow():
    rt = Tk()
    rt.geometry("300x200")
    rt.mainloop()


# ItemList = ['Pizza', 'Boriyani', 'Fried Rice']
# for i, item in enumerate(ItemList):
#     Radiobutton(root, text=item, padx=14, variable=var, value=i+1).pack(anchor='w')
Button(root, text="Order now", padx="20", pady="20", command=order).pack()
Button(root, text="Click me!", command=print("Hello world")).pack()
Button(root, text='New Window', command=newWindwow).pack()
root.mainloop()
