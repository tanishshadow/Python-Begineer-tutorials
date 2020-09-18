from tkinter import *
root = Tk()
root.geometry("700x600")
root.title("VS CODE")
def Save():
    print("File saved!")
# TODO:Non dropdown menus----
# m1 = Menu(root)
# m1.add_command(label="File", command=func)
# m1.add_command(label="Exit",command=quit)
# root.config(menu=m1)
# TODO: Dropdown menus

main = Menu(root)  #This is the horizontal bar
# File Menu
m3=Menu(main,tearoff="0")
m3.add_command(label="Save", command=Save)
m3.add_command(label="Save as", command=Save)
m3.add_separator()
m3.add_command(label="New File", command=Save)
m3.add_command(label="New folder")
main.add_cascade(label="File",menu=m3)
# Edit Menu
m4edit = Menu(main, tearoff="0")
m4edit.add_command(label="Cut")
m4edit.add_command(label="Copy")
m4edit.add_separator()
m4edit.add_command(label="Undo")
m4edit.add_command(label="Redo")
main.add_cascade(label="Edit",menu=m4edit)

root.config(menu=main)





root.configure(bg="grey")
root.mainloop()
