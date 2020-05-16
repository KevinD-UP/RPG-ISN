import pygame
import os
import math



bullet_sprite = pygame.sprite.Group()

types = [
    pygame.image.load(os.path.join("ressources/BulletBlueCircle.png")),
    pygame.image.load(os.path.join("ressources/BulletRedCircle.png")),
    pygame.image.load(os.path.join("ressources/BulletGreenCircle.png")),
    pygame.image.load(os.path.join("ressources/BulletDarkredTriangle.png")),
    pygame.image.load(os.path.join("ressources/BulletIceTriangle.png")),
    pygame.image.load(os.path.join("ressources/BulletFireTriangle.png")),
    
]


class Bullet (pygame.sprite.Sprite):

    
    def __init__ (self, angle, centerx, centery, speed, style):
            
        pygame.sprite.Sprite.__init__(self)
        
        self.image = types[style]
        self.rect = self.image.get_rect()
        self.rect.center = (centerx, centery)
        self.posx = self.rect.centerx
        self.posy = self.rect.centery
        self.angle = angle
        self.speedx = speed*math.cos(math.radians(self.angle))
        self.speedy = speed*math.sin(math.radians(self.angle))
        
        
    def update(self):
        
        self.posx += self.speedx
        self.posy += self.speedy
        self.rect.center = (self.posx, self.posy)
        
        if(self.rect.right > 600 or self.rect.left < 1 or self.rect.bottom > 800 or self.rect.top < 1 ):
            self.kill() 
        

   

    

    


