import  pygame
import time


def sound():
    pygame.mixer.init()
    pygame.mixer.music.load("Hotel-door-beep-sound-effect.mp3")
    pygame.mixer.music.play()
    time.sleep(1)

x = int(input("Nechi sonidan timer boshlansin:"))

while True:
    print(x)
    x-=1
    time.sleep(1)
    if x == 0:
        print("Vaqt tugadi!!!")
        sound()
        break
    elif x < 0:
        print("error")
        break