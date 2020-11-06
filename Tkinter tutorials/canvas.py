from tkinter import *
root=Tk()
# root.geometry("700x500")
t_can=Canvas(root,width=1000,height=500)
t_can.pack()
sc = Scrollbar(root)
sc.pack(side="right", fill=Y)
# t_can.create_line(0,0,700,500,fill="red")
# t_can.create_line(700,0,0,500,fill="red")
# # Params of rectangle are coor top left and coor bottom left
# t_can.create_rectangle(0,0,600,250 )#,fill="yellow")
# t_can.pack()
# t_can.create_text(320,250,text="CANVAS",font="comicsansms 20 bold")
# t_can.create_oval(20,0,600,250,fill="green")
sc.config(command=t_can.yview)
t_can.config(yscrollcommand=sc.set)
var = StringVar()
Radiobutton(t_can, text="Hi", font="comicsansms 10 bold", variable=var, value="Hi").pack(pady="20")
food = StringVar()
food.set("null")
    # Label 1
Label(t_can, text="We want some details from you\nAfter completing the questions of this survey hit the submit button",
    font="timesnewroman 10 bold", fg="Red").pack()

food_items = ["Dosa", "Pizza", "Burger", "Momo", "Samosa"]
gdets = ["Xiaomi", "Samsung", "One Plus", "Iphone", "Realme"]
for item in food_items:
    Radiobutton(t_can, text=item, font="timesnewroman 10 bold",
                variable=food, value=item).pack(anchor="w", pady="10")
phone = StringVar()
phone.set("some")
for brand in gdets:
    Radiobutton(t_can, text=brand, font="timesnewroman 10 bold",
                variable=phone, value=brand).pack(anchor="w", pady="10")


root.mainloop()
