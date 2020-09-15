from pygame import mixer
from time import time
from datetime import datetime

#TODO: Function which plays music

def music(file, stopper):
    "Plays music using pygame module"
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        #  this is needed because otherwise the music will not get enough time to play
        var = input()
        if var == stopper:
            mixer.music.stop()
            break

#  Records all the data in a file

def logs(msg):
    "Records the data in a file"
    f = open("logs", "a")
    f.write(f"{msg} {datetime.now()}")


if __name__ == "__main__":
    # Initialising all varibles for time requirements
    water_t = time()
    eyes_t = time()
    exercise_t = time()
    water_s = 50*60
    eyes_s = 30*60
    exercise_s = 15
    while True:
        # While loop to play music accordingly for every activity

        if time()-water_t > water_s:
            print("Time to drink water enter done to stop the alarm")
            music('water.mp3', "done")
            water_t = time() #Initialising water time again
            logs("Water drank at ")
        elif time()-eyes_t > eyes_s:
            print("Time for eyes excercise enter done to stop the alarm")
            music('eyes.mp3', "done")
            eyes_t = time() #Initialising eyes time again
            logs("Eyes excercise at")
        elif time()-exercise_t > exercise_s:
            print("Time for body excercise enter done to stop the alarm")
            music('excercise.mp3', "done")
            exercise_t = time() #Initialising exercise time again
            logs("Physical excercise at")
