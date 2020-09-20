from tkinter import *
from tkinter import messagebox as msg
root = Tk()
root.geometry("744x450")

# Funtion for submit button


def Storevl():
    """Stores all the data of the user in a file and also displays a message"""
    msg.showinfo("Response", "Submitted succesfully")
    with open("slider-data.txt", "a") as f:
        f.write(f"User's rating {sld.get()}")


root.title("User Experience using slider")
# slide----
sld = Scale(root, from_=0, to=10, orient=HORIZONTAL)
lb = Label(root, text="How was experience using our service?",
           font="timesnewroman 15 bold", fg="red",
           bg="yellow", padx="400", pady="40").pack()
sld.pack(pady="30", ipadx="100")
lb2 = Label(root, text="Rate us between 1 to 10 :)", bg="grey", font="comicsansms 15 italic",
            fg="green", padx="100", pady="30")
lb2.pack()
sb = Button(root, text="SUBMIT", font="comicsansms 10 bold", fg="white", bg="blue",
            padx="40", pady="15", command=Storevl).pack()

root.configure(bg="grey")
root.mainloop()
