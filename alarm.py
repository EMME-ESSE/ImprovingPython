#pip install pygame
from time import localtime
from pygame import mixer

hour = input("Enter the hour")
minute = input("Enter the minute")

while True:
    if localtime().tm_hour == int(hour) and localtime.tm_min == int(minute):
        print("Alarm sound")
        mixer.init()
        mixer.music.load("alarm.mp3")
        mixer.music.play()
        break
