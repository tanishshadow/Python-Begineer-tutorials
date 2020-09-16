"""Author : Tanish Sarmah
date : 9/16/2020
Problem: Guess the number game (practice problem)
"""
# Initialising player
player = 1
# initialising trials
trials = 1
while player < 3:

    def guess_the_number():
        """Players  have to guess the number from the range they provided .If their 
        number matches with the number generated randomly. Player with the lesser guesses wins
        the game.Number of guesses is limited to 10 only.Good Luck!"""

        print("Welcome to no.guessing game . You have 10 trials . Good luck")
        global player
        print(f"Player{player}'s turn : ")

        a = int(input("Enter the starting of the range:\n"))
        b = int(input("Enter the ending of the range:\n"))
        from random import randint
        # Generates a random number between the given range
        random_number = randint(a, b)
        global trials
        while trials <= 10:

            n = int(input("Guess a number:\n"))  # User's number

            if n > random_number:
                print("Wrong ! Please enter a lesser number:")

            elif n < random_number:
                print("Wrong! Please enter a greater number:")
            else:
                print("Yeah ! you won ")
                print(F"player{player} won the game in {trials} no. of trials")
                break
            print(f"{10-trials} no. of trials  left")
            trials += 1
            if trials>10:
                print(f"GAME OVER! the number was {random_number}")
            # creating player 1's and player 2's points in the global scope
            if player == 1:
                global player_point1
                player_point1 = trials

            else:
                global player_point2
                player_point2 = trials

    guess_the_number()
    player += 1
if player_point1 > player_point2:
    print("Player 1 won!")
elif player_point2 > player_point1:
    print("Player 2 won!")
else:
    print("TIE!!")
