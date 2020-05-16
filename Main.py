import pygame, sys, time, math
from scripts.color import *
from scripts.textures import *
from scripts.globals import *
from scripts.map_engine import *
from scripts.npc import *
from scripts.player import *
from scripts.gui import *
from scripts.stats import *



pygame.init() 

cSec = 0
cFrame = 0
FPS = 0





terrain = Map_Engine.load_map("maps\\world.map")





fps_font = pygame.font.Font("C:\\Windows\\Fonts\\Verdana.ttf", 20)

sky = pygame.image.load("graphics\\sky.png")
Sky = pygame.Surface(sky.get_size(), pygame.HWSURFACE)
Sky.blit(sky, (0, 0))
del sky

logo_img_temp = pygame.image.load("graphics\\logo.png")
logo_img_temp = pygame.transform.scale(logo_img_temp, (239, 176))
logo_img = pygame.Surface(logo_img_temp.get_size(), pygame.HWSURFACE)
logo_img.blit(logo_img_temp, (0, 0))
del logo_img_temp

def show_fps():
    fps_overlay = fps_font.render (str(FPS), True, Color.Goldenrod)
    window.blit(fps_overlay, (0,0))
    
def create_window():
    global window, window_width, window_height, window_title
    window_width, window_height = 800, 600
    window_title = "RPG python"
    pygame.display.set_caption(window_title)
    window = pygame.display.set_mode((window_width, window_height), pygame.HWSURFACE|pygame.DOUBLEBUF)
    
def count_fps():
    global cSec, cFrame, FPS, deltatime

    if cSec == time.strftime("%S"):
        cFrame += 1
    else:
        FPS = cFrame
        cFrame = 0
        cSec = time.strftime("%S")
        if FPS > 0:
            deltatime = 1 / FPS
            
def combat(stage):

    # caractéristiques de la fenêtre           
    areax = 600
    areay = 400
    white = (255, 255, 255)
    pygame.display.set_caption("flèches directionnelles pour bouger, Esc pour quitter")
    #dessine la fenêtre où le logo est confiné
    area_rect = pygame.Rect((((window_width/2)-(areax/2)),(window_height-areay)-100), (areax, areay))
    lines = pygame.draw.lines(window, white, True,
    [((window_width/2)-(areax/2), window_height-100),
    ((((window_width/2)-(areax/2)),(window_height-areay)-100)),
    ((((window_width/2)+(areax/2)),(window_height-areay)-100)),
    ((window_width/2)+(areax/2), window_height-100)],
    5)
    
    #chemin vers l'image
    sprite = pygame.image.load("scripts/ressources/pythonlogo.png")
    hitbox = pygame.image.load("scripts/ressources/hitbox.jpg")
    # prend les données du rectangle de l'image
    sprite_rect = sprite.get_rect()
    hitbox_rect = hitbox.get_rect()
    # place le logo au milieu de l'écran
    sprite_rect.centerx = (window_width//2)
    sprite_rect.centery = (window_height//2)
    
    window.blit(sprite, sprite_rect)   
    hitbox_rect.centerx = sprite_rect.centerx 
    hitbox_rect.centery = sprite_rect.centery 
    window.blit(hitbox, hitbox_rect)
    pygame.display.flip()
    clock = pygame.time.Clock()
    
    # boucle infine de la fenêtre
    while 1:
        # 60 images par seconde
        clock.tick(60)      
        pygame.event.pump()
        # vérifie qu'une touche est active ou non
        keyinput = pygame.key.get_pressed()
        
                
        if keyinput[pygame.K_RSHIFT]:
            ms = 15 - MoveSpeed
        else :
            ms = MoveSpeed
            
               
              
        # vérifie d'abord si deux directions opposées sont entrées
                
        if keyinput[pygame.K_a] and keyinput [pygame.K_d]:
            sprite_rect.centerx = sprite_rect.centerx

        elif keyinput[pygame.K_w] and keyinput [pygame.K_s]:
            sprite_rect.centery = sprite_rect.centery
                    
        #vérifie si deux directions (donnant une diagonale) sont entrées
                
        elif keyinput[pygame.K_a] and keyinput[pygame.K_w]:
            sprite_rect.centerx -= ms*math.sqrt(2)/2
            sprite_rect.centery -= ms*math.sqrt(2)/2

        elif keyinput[pygame.K_a] and keyinput[pygame.K_s]:
            sprite_rect.centerx -= ms*math.sqrt(2)/2
            sprite_rect.centery += ms*math.sqrt(2)/2

        elif keyinput[pygame.K_d] and keyinput[pygame.K_s]:
            sprite_rect.centerx += ms*math.sqrt(2)/2
            sprite_rect.centery += ms*math.sqrt(2)/2

        elif keyinput[pygame.K_d] and keyinput[pygame.K_w]:
            sprite_rect.centerx += ms*math.sqrt(2)/2
            sprite_rect.centery -= ms*math.sqrt(2)/2
                    
        #vérifie enfin si une seule direction est donnée

        elif keyinput[pygame.K_w]:
            sprite_rect.centery -= ms

        elif keyinput[pygame.K_a]:
            sprite_rect.centerx -= ms

        elif keyinput[pygame.K_s]:
            sprite_rect.centery += ms

        elif keyinput[pygame.K_d]:
            sprite_rect.centerx += ms

        hitbox_rect.centerx = sprite_rect.centerx 
        hitbox_rect.centery = sprite_rect.centery
        

            
        #clamp_ip empêche le sprite de sortir de l'écran
        sprite_rect.clamp_ip(area_rect)       
        window.blit(sprite, sprite_rect)
        window.blit(hitbox, hitbox_rect)
        pygame.display.flip() 
                   

create_window()

player = Player("Kévin")
player_w, player_h = player.width, player.height
player_x = (window_width / 2 - player_w / 2 - Globals.camera_x) / Tiles.Size
player_y = (window_height / 2 - player_h / 2 - Globals.camera_y) / Tiles.Size

#INITIALIZE MUSIC
pygame.mixer.music.load("music\\Title_Screen.wav")
pygame.mixer.music.play(-1)

#INITIALIZE SOUNDS





#INITIALIZE GUI

def Play():
    Globals.scene = "game"
    pygame.mixer.music.load("music\\town.wav")
    pygame.mixer.music.play(-1)
   
def Exit():
    global isRunning
    isRunning = False

btnPlay = Menu.Button(text = "Play", rect = (0, 80, 300, 60),
                    tag = ("menu", None))
btnPlay.Left = window_width / 2 - btnPlay.Width / 2
btnPlay.Top = window_height / 2 - btnPlay.Height / 2

btnPlay.Command = Play

btnExit = Menu.Button(text = "Exit", rect = (0, 0, 300, 60),
                      tag = ("menu", None))

btnExit.Left = btnPlay.Left
btnExit.Top = btnPlay.Top + btnExit.Height + 3
btnExit.Command = Exit

menuTitle = Menu.Text(text = "Python's Tales", color = Color.Cyan,
                      font = Font.Large)
menuTitle.Left, menuTitle.Top = window_width / 2 - menuTitle.Width / 2, 0

logo = Menu.Image(bitmap = logo_img)
logo.Left = window_width / 2 - logo.Width / 2
logo.Top = menuTitle.Top + menuTitle.Height + 3

ms = 300
isRunning = True

while isRunning:

    
    for event in pygame.event.get():
                    
        if event.type == pygame.QUIT:
            isRunning = False
    

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and keys[pygame.K_s]:
            Globals.camera_move = 0
        elif keys[pygame.K_a] and keys[pygame.K_d]:
            Globals.camera_move = 0
        elif event.type == pygame.KEYUP:
            Globals.camera_move = 0
        elif keys[pygame.K_w] and keys[pygame.K_a]:
            Globals.camera_move = 2
            player.facing = "north"
        elif keys[pygame.K_s] and keys[pygame.K_a]:
            Globals.camera_move = 4
            player.facing = "east"
        elif keys[pygame.K_s] and keys[pygame.K_d]:
            Globals.camera_move = 6
            player.facing = "south"
        elif keys[pygame.K_w] and keys[pygame.K_d]:
            Globals.camera_move = 8
            player.facing = "west"
        elif keys[pygame.K_w]:
            Globals.camera_move = 1
            player.facing = "north"
        elif keys[pygame.K_s]:
            Globals.camera_move = 5
            player.facing = "south"
        elif keys[pygame.K_a]:
            Globals.camera_move = 3
            player.facing = "east"
        elif keys[pygame.K_d]:
            Globals.camera_move = 7
            player.facing = "west"
        elif keys[pygame.K_p]:
            combat(1)
        
        elif  event.type == pygame.KEYUP:
   
         if event.key == pygame.K_w or event.key == pygame.K_s or event.key == pygame.K_a or event.key == pygame.K_d:
                Globals.camera_move = 0

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: #LEFT CLICK

        

                #HANDLE BUTTON CLICK EVENTS
                for btn in Menu.Button.All:
                    if btn.Tag[0] == Globals.scene and btn.Rolling:
                        if btn.Command != None:
                            btn.Command()#DO BUTTON EVENT
                        btn.Rolling = False
                        break #EXIT LOOP

            
    # RENDER SCENE
    if Globals.scene == "game":
                
        # LOGIC
            
        
        if Globals.camera_move == 1:
            Globals.camera_y += ms * deltatime

        if Globals.camera_move == 5:
           
            Globals.camera_y -= ms * deltatime
        if Globals.camera_move == 3:
            
            Globals.camera_x += ms * deltatime
        if Globals.camera_move == 7:
           
            Globals.camera_x -= ms * deltatime
        if Globals.camera_move == 2:
            
            Globals.camera_y += (ms*(math.sqrt(2))/2) * deltatime
            Globals.camera_x += (ms*(math.sqrt(2))/2) * deltatime
        if Globals.camera_move == 4:
           
            Globals.camera_y -= (ms*(math.sqrt(2))/2) * deltatime
            Globals.camera_x += (ms*(math.sqrt(2))/2) * deltatime
        if Globals.camera_move == 6:
            
            Globals.camera_y -= (ms*(math.sqrt(2))/2) * deltatime
            Globals.camera_x -= (ms*(math.sqrt(2))/2) * deltatime
        if Globals.camera_move == 8:
            
            Globals.camera_y += (ms*(math.sqrt(2))/2) * deltatime
            Globals.camera_x -= (ms*(math.sqrt(2))/2) * deltatime

        
        player_x = (window_width / 2 - player_w / 2 - Globals.camera_x) / Tiles.Size
        player_y = (window_height / 2 - player_h / 2 - Globals.camera_y) / Tiles.Size

      
        

        
        
       
        # RENDER GRAPHICS
        window.blit(Sky, (0, 0))

        window.blit(terrain, (Globals.camera_x, Globals.camera_y))
      
        window.blit(window, (0,0))      
        player.render(window, (window_width / 2 - player_w / 2, window_height / 2 - player_h / 2))


    #PROCESS MENU
    elif Globals.scene == "menu":
        window.fill(Color.Fog)
        logo.Render(window)
        menuTitle.Render(window)

        for btn in Menu.Button.All:
            if btn.Tag[0] == "menu":
                btn.Render(window)
                
        
    show_fps()

    count_fps()
    pygame.display.flip()



pygame.quit()
sys.quit()
