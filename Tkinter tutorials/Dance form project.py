from tkinter import *


def help():
    print("This Form  is for the students who want to join dance school.\n"
          "You are required to enter asked details for joining the dance school\n"
          "Regards-'Tanish sarmah'")


def data():
    filee = open("user-data-dance.txt", "at")
    name = u_val.get()
    password = p_val.get()
    filee.write(f"Name : {name} Password: {password}\n")


root = Tk()
root.geometry("720x555")
root.title("Dance Form ")
l0 = Label(root, text="DANCE", bg="red", fg="white",
           pady=40, padx=200, font="comicsansms 20 bold")
l0.grid(row="0", column="0")
l1 = Label(root, text="FORM", bg="red", fg="white",
           font="comicsansms 20 bold", pady="40", padx="720")
l1.grid(row=0, column=1)

user = Label(root, text="NAME", padx=190, pady=40, fg="red", borderwidth="5",
             bg="yellow", relief=SUNKEN)
passw = Label(root, text="PASSWORD",
              padx=175, pady=40, fg="red", bg="yellow", borderwidth="5",
              relief=SUNKEN)
user.grid(row="1", column="0", pady=40)
passw.grid(row="2", column="0", pady=40)
s_f = Frame(root, borderwidth="7", relief=GROOVE)
s_f.grid()
s_b = Button(s_f, text="SUBMIT", bg="green",
             fg="white", padx=60, pady=10, command=data)
s_b.grid(column=1)
u_val = StringVar()
p_val = StringVar()
u_ent = Entry(root, textvariable=u_val)
p_ent = Entry(root, textvariable=p_val)
u_ent.grid(row=1, column=1, ipadx=120, ipady=25)
p_ent.grid(row=2, column=1, ipadx=120, ipady=25)
f1 = Frame(root, borderwidth="4")
f1.grid(row=4, column=1)
b1 = Button(f1, text="Help", fg="blue", bg="grey", padx=40, pady=6,
            font="comicsansms 10 bold", command=help)
b1.grid(row=3, column=1)


root.mainloop()
