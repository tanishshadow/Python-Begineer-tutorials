# python excercise 5 
# health management system

def healthcaresystem():
    print(" Health management system for Harry,Rohan and Hammid")
    import datetime
    def gettime():
        return datetime.datetime.now()
    def name():
        """Function for genrating files for differnt names"""
        enter_name=input("Enter Harry, Rohan or Hammid:\n")
    # asking name
        if(enter_name.upper()=="HARRY"):
            lock_or_retrieve=input("Do you want to retreive or lock? Enter 'Retrieve' or 'lock':\n")
        # LOCK input
            if(lock_or_retrieve.upper()=="LOCK"):
                ex_or_food=input("Enter diet plan or excercise: type'Food' or 'Exercise':\n")
        # Exercise input
                if(ex_or_food.lower()=="exercise"):
                    ex=input("Enter the excercise that you want to add:\n")
                    t=open("harry-ex.txt","w")
                    t.write(ex)
                    t.write("\n")
                    t.write(str([str(gettime())]))
                    print("Succesfully added to the file.")
                    t.close()
            # food input
                elif(ex_or_food.lower()=="food"):
                    fd=input("Enter the food that you want to add:\n")
                    t2=open("harry-fd.txt","w")
                    t2.write(fd)
                    t2.write("\n")
                    t2.write(str([str(gettime())]))
                    print("Succesfully added to the file.")

                    t2.close()
            # error then again start , else for food or excercise locking
                else:
                    print("Sorry an error occured ! please try again..")
                    
        # retreiveing files
            elif(lock_or_retrieve.lower()=="retrieve"):
                rv_ex_food=input("What data do you want retrieve? 'Food' or 'Excercise':\n")
            # food input:
                if(rv_ex_food.upper()=="FOOD"):
                    retreive_file=open("harry-fd.txt")
                    print(retreive_file.readlines())
            #   exercise input:
                elif(rv_ex_food.upper()=="EXERCISE"):
                    retreive_file2=open("harry-ex.txt")
                    print(retreive_file2.readlines())
                # input for other than food or exercise:
                else:
                    print("Invalid input please try again... ")
        # input other than lock or retrieve:
            else:
                print("invalid input please try again...")
    
    # asking name
        elif(enter_name.upper()=="ROHAN"):
            lock_or_retrieve=input("Do you want to retreive or lock? Enter 'Retrieve' or 'lock':\n")
        # LOCK input
            if(lock_or_retrieve.upper()=="LOCK"):
                ex_or_food=input("Enter diet plan or excercise: type'Food' or 'Exercise':\n")
        # Exercise input
                if(ex_or_food.lower()=="exercise"):
                    ex=input("Enter the excercise that you want to add:\n")
                    t=open("rohan-ex.txt","w")
                    t.write(ex)
                    t.write("\n")
                    t.write(str([str(gettime())]))
                    print("Succesfully added to the file.")

                    t.close()
            # food input
                elif(ex_or_food.lower()=="food"):
                    fd=input("Enter the food that you want to add:\n")
                    t2=open("rohan-fd.txt","w")
                    t2.write(fd)
                    t2.write("\n")
                    t2.write(str([str(gettime())]))
                    print("Succesfully added to the file.")

                    t2.close()
            # error then again start , else for food or excercise locking
                else:
                    print("Sorry an error occured ! please try again..")
            # retreiveing files
            elif(lock_or_retrieve.lower()=="retrieve"):
                rv_ex_food=input("What data do you want retrieve? 'Food' or 'Excercise':\n")
                # food input:
                if(rv_ex_food.upper()=="FOOD"):
                    retreive_file=open("rohan-fd.txt")
                    print(retreive_file.readlines())
            #       exercise input:
                elif(rv_ex_food.upper()=="EXERCISE"):
                        retreive_file2=open("rohan-ex.txt")
                        print(retreive_file2.readlines())
                 # input for other than food or exercise:
                else:
                    print("Invalid input please try again... ")
        #    input other than lock or retrieve:
            else:
                print("invalid input please try again...")
    
    # asking name
        elif(enter_name.upper()=="HAMMAD"):
            lock_or_retrieve=input("Do you want to retreive or lock? Enter 'Retrieve' or 'lock':\n")
        #   LOCK input
            if(lock_or_retrieve.upper()=="LOCK"):
                ex_or_food=input("Enter diet plan or excercise: type'Food' or 'Exercise':\n")
        #    Exercise input
                if(ex_or_food.lower()=="exercise"):
                    ex=input("Enter the excercise that you want to add:\n")
                    t=open("hammad-ex.txt","w")
                    t.write(ex)
                    t.write("\n")
                    t.write(str([str(gettime())]))
                    print("Succesfully added to the file.")

                    t.close()
            #    food input
                elif(ex_or_food.lower()=="food"):
                    fd=input("Enter the food that you want to add:\n")
                    t2=open("hammad-fd.txt","w")
                    t2.write(fd)
                    t2.write("\n")
                    t2.write(str([str(gettime())]))
                    t2.close()
            #   error then again start , else for food or excercise locking
                else:
                    print("Sorry an error occured ! please try again..")
        #   retreiveing files
            elif(lock_or_retrieve.lower()=="retrieve"):
                rv_ex_food=input("What data do you want retrieve? 'Food' or 'Excercise':\n")
                    # food input:
                if(rv_ex_food.upper()=="FOOD"):
                    retreive_file=open("hammad-fd.txt")
                    print(retreive_file.readlines())
            #    exercise input:
                elif(rv_ex_food.upper()=="EXERCISE"):
                        retreive_file2=open("hammad-ex.txt")
                        print(retreive_file2.readlines())
                    # input for other than food or exercise:
                else:
                    print("Please don't use any other keyword other than 'Food ' or 'Exercise' ")
        #   input other than lock or retrieve
            else:
                print("invalid input please try again...")
        else:
            print("Invalid name please try again")
        
    name()
    
    
# function for continuation of the program
    def again():
        'continue the program'
        continue_or_not=input("Do you want to continue? Enter Yes or No:\n")
        if(continue_or_not.upper()=="YES"):
            healthcaresystem()
        elif(continue_or_not.upper()=="NO"):
            print("Thanks for using tanish's health management system")
        else:
            print("Please enter Yes or No only....try again")
            again()
    
    again()

healthcaresystem()
