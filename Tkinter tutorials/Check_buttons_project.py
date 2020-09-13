from tkinter import *
root = Tk()


def submit():
    "Stores all the data in a file"
    print("Submitted Successfully")
    with open("Travel-data.txt", "a") as f:
        namev = nameval.get()
        passv = passwval.get()
        checkv = checkval.get()
        paymentv = paymentval.get()
        phonev = phoneval.get()
        if checkv == 0:
            checkv = "Included"
        else:
            checkv = "Not included"

        f.write(f"User : {namev} : [ password : {passv}\nphone number"
                f": {phonev} payment : {paymentv}\nFood service {checkv} ]")
root.configure(bg='grey') 
def help1():
    "Returns Help"
    print(" Help : This form is made by Tanish sarmah ")


root.geometry("540x344")
Label(root, text="Welcome to Tanish's hotels",
      font="comicsansms 20 bold", pady="30", padx="344").grid(row="0", column="2")

# ALL labels:


name = Label(root, text="Name", font="comicsansms 10 bold", padx="168", pady="20", bg="green",
             fg="yellow")
passw = Label(root, text="Password", font="comicsansms 10 bold",
              pady="20", padx="158", fg="yellow", bg="green")
contact = Label(root, text="Phone Number", font="comicsansms 10 bold",
                padx="140", pady="20", fg="yellow", bg="green")
payment = Label(root, text="Payment Mode", font="comicsansms 10 bold",
                padx="140", pady="20", fg="yellow", bg="green")

# packing all labels:
name.grid(row="1", column="0", pady="10")
passw.grid(row="2", column="0", pady="10")
contact.grid(row="3", column="0", pady="10")
payment.grid(row="4", column="0", pady="10")

# BUTTONS
submitframe = Frame(root)
submitbutton = Button(submitframe, text="SUBMIT", font="comicsansms 10 bold",
                      padx=20, pady=10, command=submit, bg="blue", fg="white")
helpframe = Frame(root)
helpb = Button(helpframe, text="Help", font="comicsansms 10 italic",
               command=help1, bg="grey", fg="black", padx="20", pady="10")

# packing buttons

submitframe.grid(row="6", column="1")
submitbutton.grid(row="6", column="1")
helpframe.grid(row="7", column="2")
helpb.grid(row="7", column="2")

# Entries values

nameval = StringVar()
passwval = StringVar()
phoneval = StringVar()
paymentval = StringVar()

#  Entries
nameE = Entry(root, textvariable=nameval, font="comicsansms 15 bold")
passE = Entry(root, textvariable=passwval, font="comicsansms 15 bold")
phoneE = Entry(root, textvariable=phoneval, font="comicsansms 15 bold")
paymentE = Entry(root, textvariable=paymentval, font="comicsansms 15 bold")

#  Packing Entries

nameE.grid(row="1", column="2", ipadx="90", ipady="10")
passE.grid(row="2", column="2", ipadx="90", ipady="10")
phoneE.grid(row="3", column="2", ipadx="90", ipady="10")
paymentE.grid(row="4", column="2", ipadx="90", ipady="10")

# ------Checkbutton---------

checkval = IntVar()

check = Checkbutton(
    root, text="Do you want to prebook food services.", fg='red',bg="yellow",
     pady="20", padx="10",height=1,font="comicsansms 10 bold")
check.grid(row="5", column="2")


root.mainloop()
