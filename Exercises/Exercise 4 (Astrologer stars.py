def star():
    "printing star pattern"
    row_num=int(input("Enter how many rows do you want:\n"))
    boo_val=input("Enter 1 or 0:\n")
    if(boo_val=="1"):
        for i in range(0,row_num+1):
            print("*"*i,end=" ")
            print()
    elif(boo_val=="0"):
        for i in range(row_num,0,-1):
            print("*"*i,end=" ")
            print()
    else:
        print("Enter 1 or 0 only")
        star()
star()
def continuation():

    continue_or_not=input("Do you want to continue?\n")
    if continue_or_not=="yes":
        star()
    elif continue_or_not=="no":
        print("Good bye")
continuation()

