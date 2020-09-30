name = input("Enter your name:")
try:
    folder_inp = input(
        "Enter the the path of your folder with'r' eg-r""c://"":\n")
    file_inp = input(
        "Enter the name of the file which you want to exclude from the operation:\n")
    format_inp = input(
        "Enter the file format eg-jpg to number it as 1,2.....:\n")

    def soldier(folder, file, format1):
        "Oh soldier pretiffy my folder."
        import os
        #changing the path of the current working directory to the path of the input folder.
        os.chdir(folder)
        #Converting the folder in a list that contains file.
        lst_file = os.listdir(folder)
        for item in lst_file:
            if item != file_inp:
            #capitalizes the name of each item.
                os.rename(item, item.capitalize())
        for key, value in enumerate(lst_file):
            key = str(key)
            if value.endswith(format1):
                os.rename(value, key)
                #Renaming the file by numbering
            print(item, f"{key}.{format1}")
    soldier(folder_inp, file_inp, format_inp)
except IOError as er:
    print(er)
except EOFError as f:
    print(f)
except Exception as ex:
    print(ex)
finally:
    if __name__ == "__main__":
        print(f"Thanks for using the program {name} :)")
