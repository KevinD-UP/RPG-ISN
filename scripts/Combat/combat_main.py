import pygame as pg #plus court à écrire
import math
import threading
from scripts.stats import *
from scripts.stages import *
from ressources import *
from scripts.textures import *
from scripts.patterns import *

def combat(stage):
    
    pg.init()
    # caractéristiques de la fenêtre       
    width = 600
    height = 800
    windowx = 485
    windowy = 300
    white = (255, 255, 255)
    screen = pg.display.set_mode((width, height))
    pg.display.set_caption("flèches directionnelles pour bouger, Esc pour quitter")
    screen_rect = pg.Rect((0,0), (width, height))  
    background = pg.image.load("ressources/background.jpg")
    #dessine la fenêtre où le logo est confiné
    window_rect = pg.Rect((((width/2)-(windowx/2)),(height-windowy)-100), (windowx, windowy))
    lines = pg.draw.lines(background, white, True, [((width/2)-(windowx/2), height-100), ((((width/2)-(windowx/2)),(height-windowy)-100)), ((((width/2)+(windowx/2)),(height-windowy)-100)), ((width/2)+(windowx/2), height-100)], 5)
    
    #chemin vers l'image
    sprite = pg.image.load("ressources/pythonlogo.png")
    hitbox = pg.image.load("ressources/hitbox.jpg")
    # prend les données du rectangle de l'image
    sprite_rect = sprite.get_rect()
    hitbox_rect = hitbox.get_rect()
    # place le logo au milieu de l'écran
    
    sprite_rect.centerx = (width//2)
    sprite_rect.centery = (height//2)
    screen.blit(background, (0,0))
    screen.blit(sprite, sprite_rect)   
    hitbox_rect.centerx = sprite_rect.centerx 
    hitbox_rect.centery = sprite_rect.centery 
    screen.blit(hitbox, hitbox_rect)
    clock = pg.time.Clock()

    if stage == 0:
        level = tutorial
    elif stage == 1:
        level = stageone
    elif stage == 2:
        level = stagetwo

    fight = threading.Thread(target = level)
    threads = [fight]
    fight.start()
    
    pg.display.update()
       
    
    
    # boucle infine de la fenêtre
    while 1:
        # 60 images par seconde, changer les fps changera la vitesse (v=d/t)
        clock.tick(60)        
        pg.event.pump()
        # vérifie qu'une touche est active ou non
        keyinput = pg.key.get_pressed()
        # quitte avec escape
        for event in pg.event.get():
            if keyinput[pg.K_ESCAPE]:
                raise SystemExit
                
        # quitte sur le bouton "x"
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                raise SystemExit
        
                
        if keyinput[pg.K_RSHIFT]:
            ms = 10 - MoveSpeed
        else :
            ms = MoveSpeed
            
               
              
        # vérifie d'abord si deux directions opposées sont entrées
                
        if keyinput[pg.K_a] and keyinput [pg.K_d]:
            sprite_rect.centerx = sprite_rect.centerx

        elif keyinput[pg.K_w] and keyinput [pg.K_s]:
            sprite_rect.centery = sprite_rect.centery
                    
        #vérifie si deux directions (donnant une diagonale) sont entrées
                
        elif keyinput[pg.K_a] and keyinput[pg.K_w]:
            sprite_rect.centerx -= ms*math.sqrt(2)/2
            sprite_rect.centery -= ms*math.sqrt(2)/2

        elif keyinput[pg.K_a] and keyinput[pg.K_s]:
            sprite_rect.centerx -= ms*math.sqrt(2)/2
            sprite_rect.centery += ms*math.sqrt(2)/2

        elif keyinput[pg.K_d] and keyinput[pg.K_s]:
            sprite_rect.centerx += ms*math.sqrt(2)/2
            sprite_rect.centery += ms*math.sqrt(2)/2

        elif keyinput[pg.K_d] and keyinput[pg.K_w]:
            sprite_rect.centerx += ms*math.sqrt(2)/2
            sprite_rect.centery -= ms*math.sqrt(2)/2
                    
        #vérifie enfin si une seule direction est donnée

        elif keyinput[pg.K_w]:
            sprite_rect.centery -= ms

        elif keyinput[pg.K_a]:
            sprite_rect.centerx -= ms

        elif keyinput[pg.K_s]:
            sprite_rect.centery += ms

        elif keyinput[pg.K_d]:
            sprite_rect.centerx += ms

        hitbox_rect.centerx = sprite_rect.centerx 
        hitbox_rect.centery = sprite_rect.centery

        
        
            
            
        #clamp_ip empêche le sprite de sortir de l'écran
        
        sprite_rect.clamp_ip(window_rect)
        screen.blit(background, (0,0))
        screen.blit(sprite, sprite_rect)
        screen.blit(hitbox, hitbox_rect)        
        bullet_sprite.update()
        bullet_sprite.draw(screen)
        pg.display.update()
        
        # met à jour la fenêtre


        
combat(0)                   
      
        
