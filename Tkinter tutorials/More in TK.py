from tkinter import *
root = Tk()
root.geometry("700x600")
root.title("Status Bar")
def upload():
    import time

    sts.set("uploading...")
    sts_bar.update()
    time.sleep(3)
    sts.set("Uploaded..!")

# Status bar is not a widget . We need to create it using label.
sts = StringVar()
sts.set("Status")
sts_bar = Label(root, textvariable=sts, relief=SUNKEN,anchor="w")
sts_bar.pack(side=BOTTOM,fill=X)
Button(root, text="upload", fg="blue", command=upload).pack()



root.mainloop()
