import threading
from scripts.patterns import *
import pygame

ongoing = []
            
def tutorial():
    
    circle(200, 200, 40, 0.4,0)
    circle(400, 200, 40, 0.4,0)
    pygame.time.delay(1000)
    a = threading.Thread(target = rain, args = (3, 200, 1, 2,))
    ongoing.append(a)
    a.start()
    original_speed = 0.5
    speed = original_speed
    pygame.time.delay(3000)
    for i in range (8):
        circle(100+20*i, 200+5*i, 20, speed,2)
        speed = (i+1)*original_speed
        pygame.time.delay(30*i)
        circle(100+20*i, 200+5*i, 20, speed,5)
        speed = (i+1)*original_speed
        pygame.time.delay(30*i)
def stageone():
    pyramid(200,500,7,1,80,30,1,2)

def stagetwo():
    rain(3, 200, 2, 3)
    


