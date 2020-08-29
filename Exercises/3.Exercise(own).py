print("Welcome to guess the no. game.....")
guess_no=1
while guess_no<=5:
    user=int(int(input("Enter a number to guess:\n")))

    if user>62:
        print("The no is greater ..try again..")
    elif user<62:
        print("The no is lesser..try again...")
        print(f"You took {guess_no} of guesses to win... ")
    else:
        print("Yeah you won!")
        break
    print(f"{5-guess_no} of guesses left ..")
    guess_no+=1
if guess_no>5:
    print("GAME OVER!")
  
