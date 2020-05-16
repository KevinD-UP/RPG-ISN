from scripts.textures import*
import math
import random



def circle (centerx, centery, density, speed,style):
    angle = 0 
    for i in range(density):
        bullet_sprite.add(Bullet(angle, centerx, centery, speed,style))
        angle +=  360/density
       
def pyramid (centerx, centery, size, orientation, opening, density, speed, style):
    n = 0
    original_centerx = centerx
    original_centery = centery
    for i in range(size):
        n += 1
        centery += density  
        centerx = original_centerx - (i*opening / 2) 
        for j in range (n):
            centerx += (i+1)*opening/n
            bullet_sprite.add(Bullet(angle, centerx, centery, speed, style))
            
def rain (style, size, thickness, speed):
    angle = 90
    for i in range (size):
        cadence = int(100/thickness)
        pygame.time.wait(cadence)
        centerx = random.randint(0, 600)
        centery = random.randint(0, 200)
        bullet_sprite.add(Bullet(angle, centerx, centery, speed, style))
    
    
