# snake water gun game
print("Welcome to the snake water gun game")
print("There will be a total of 10 rounds")
print("Good luck!")


import random
ex_list=["Water","Snake","Gun"]
play_game=1
computer_point=0
user_point=0
while(play_game<=10):
    computer=random.choice(ex_list)


    
    print("Round:",play_game)
    play_game=play_game+1
    user_input=str(input("Enter 'Snake' / 'Water'/ 'Gun':\n"))
    if(user_input.upper()=="SNAKE"and computer=="Water"):
        user_point=user_point+1
        print("You won!")
        print("Computer input:",computer)

    elif(user_input.upper()=="GUN"and computer=="Snake"):
        user_point=user_point+1

        print("You won!")
        print("Computer input:",computer)


    elif(user_input.upper()=="GUN"and computer=="Water"):
        computer_point=computer_point+1
        print("You lose!")
        print("Computer input:",computer)

    elif(user_input.upper()=="SNAKE"and computer=="Gun"):
        computer_point=computer_point+1

        print("You lose!")
        print("Computer input:",computer)

    elif(user_input.upper()=="WATER"and computer=="Gun"):
        user_point=user_point+1

        print("You won!")
        print("Computer input:",computer)

    elif(user_input.upper()=="GUN"and computer=="Snake"):
        user_point=user_point+1
       
        print("You won!")
        print("Computer input:",computer)
    
    elif(user_input.upper()=="WATER"and computer=="Snake"):
        computer_point=computer_point+1

        print("Computer input:",computer)

        print("You lose!")

    elif(user_input.upper()==computer.upper()):
        print("Computer input:",computer)
        print("Draw!")
       
    else:
        print("Invalid input...try again")
        play_game=play_game-1
        continue
    print("Player point:",user_point,"Computer point:",computer_point)

if(computer_point>user_point):
    print("player lose!")
elif(computer_point<user_point):
    print("player won!")
else:
    print("Tie!")
