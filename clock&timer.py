from playsound import playsound
import time

seconds = int(input("Enter your time in seconds: "))

for i in range(seconds):
    print(str(seconds-i) + " seconds remain")
    time.sleep(1)
playsound('D:\Programing Files\PyCharm\Projects\Practise\sound.mp3')
quit()