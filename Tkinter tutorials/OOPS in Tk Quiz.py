"""Using oops to make GUI (quiz)
Date : 27/09/2020
"""
from tkinter import *
from tkinter import messagebox as msg


class MyGui(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("700x600")
        self.title("GUI OOPS")

    def chngcolor(self):
        from random import choice
        bgs = ["Blue", "Red", "Maroon", "Black", "Grey"]
        ch = choice(bgs)
        val = msg.askyesno(
            "COLOUR", "This will change the colour of the window ..\nDo you want to continue anyway?")
        if val == True:
            self.configure(bg=ch)
        else:
            pass

    def resetColor(self):
        val2 = msg.askyesno(
            "Reset", "This will reset the color of the window back to white\nDo you want to continue?")
        if val2 == True:
            self.configure(bg="white")
        else:
            pass

    def button1(self):
        b1 = Button(text="CLICK", bg="gold", command=self.chngcolor, padx="20")
        b1.pack(anchor="w", side="top", padx="14")

    def butt2(self):
        Button(text="Reset", bg="silver", command=self.resetColor).pack(side=BOTTOM,
                                                                        anchor="e", padx="15")

    def label1(self):
        self.sts = StringVar()
        self.sts.set("Status :OK")
        self.stsbar = Label(self, textvar=self.sts, font="timesnewroman 10 bold",
                            fg="green", anchor="w", relief=SUNKEN, borderwidth=5)
        self.stsbar.pack(side=BOTTOM, fill=X)

    def radiobt(self):
        # Scrollbar----
        self.scbr = Scrollbar(self)
        self.scbr.pack(fill=Y, side=RIGHT)
        self.food = StringVar()
        self.food.set("null")
        # Label 1 
        Label(self, text="We want some details from you\nAfter completing the questions of this survey hit the submit button",
              font="timesnewroman 10 bold", fg="Red").pack()
        Label(self, text="Choose a food item from the foloowing options",font="timesnewroman 10 bold",fg="black").pack(pady=20)
        food_items = ["Dosa", "Pizza", "Burger", "Momo", "Samosa"]
        gdets = ["Xiaomi", "Samsung", "One Plus", "Iphone", "Realme"]
        for item in food_items:
            Radiobutton(self, text=item, font="timesnewroman 10 bold",
                        variable=self.food, value=item).pack(anchor="w", pady="10")
        self.phone = StringVar()
        self.phone.set("Null")
        Label(self, text="Choose a phone  from the foloowing options",
              font="timesnewroman 10 bold", fg="black").pack(pady=20)
        for brand in gdets:
            Radiobutton(self, text=brand, font="timesnewroman 10 bold",
                        variable=self.phone, value=brand).pack(anchor="w", pady="10")
        # Configuring scrollbar=----
        # self.scbr.config(command=self.text.yview)
    def submit(self):
        msg.showinfo("RESPONSE", "Your Response has been recorded!")
        with open("oops-quiz-data.txt","a") as f:
            f.write(f"Mobile Brand : {self.phone.get()}\nFood :{self.food.get()}")
    def subbut(self):
        Button(self.stsbar,text="SUBMIT", bg="blue" ,command=self.submit).pack()

if __name__ == "__main__":

    root = MyGui()
    root.button1()
    root.label1()
    root.butt2()
    root.radiobt()
    root.subbut()
    root.mainloop()
