import pygame

pygame.init()


class Tiles:

    Size = 32
    Size2 = 320

    Blocked = []
    Blocked_Types = ["16","17","18","30"]

    def Blocked_At(pos):
        if list(pos) in Tiles.Blocked:
            return True
        else:
            return False
    

    def Load_Texture(file, Size):
        bitmap = pygame.image.load(file)
        bitmap = pygame.transform.scale(bitmap, (Size, Size))
        surface = pygame.Surface ((Size, Size), pygame.HWSURFACE|pygame.SRCALPHA)
        surface.blit (bitmap, (0, 0))
        return surface

    #GRASS
    Grass = Load_Texture("graphics\\grass.PNG", Size)
    Grass2 = Load_Texture("graphics\\grass2.PNG", Size)
    Grass3 = Load_Texture("graphics\\grass3.PNG", Size)
    Grass4 = Load_Texture("graphics\\grass4.PNG", Size)

    #STONE
    Stone = Load_Texture("graphics\\stone.PNG", Size)
    Stone2 = Load_Texture("graphics\\stone2.PNG", Size)
    Stone3 = Load_Texture("graphics\\stone3.PNG", Size)

    #WATER
    Water = Load_Texture("graphics\\water.PNG", Size)
    Water2 = Load_Texture("graphics\\water2.PNG", Size)
    Water3 = Load_Texture("graphics\\water3.PNG", Size)
    Water4 = Load_Texture("graphics\\water4.PNG", Size)

    #SAND
    Sand = Load_Texture("graphics\\sand.PNG", Size)

    #Tree
    Tree = Load_Texture("graphics\\tree.PNG", Size2)
    Tree2 = Load_Texture("graphics\\tree2.PNG", Size2)
    Tree3 = Load_Texture("graphics\\tree3.PNG", Size2)

    #HOUSE
    House = Load_Texture("graphics\\house.PNG", Size2)
    House2 = Load_Texture("graphics\\house2.PNG", Size2)
    House3 = Load_Texture("graphics\\house3.PNG", Size2)
    House4 = Load_Texture("graphics\\house4.PNG", Size2)
    House5 = Load_Texture("graphics\\house5.PNG", Size2)
    House6 = Load_Texture("graphics\\house6.PNG", Size2)
    House7 = Load_Texture("graphics\\house7.PNG", Size2)
    House8 = Load_Texture("graphics\\house8.PNG", Size2)
    House9 = Load_Texture("graphics\\house9.PNG", Size2)

    #Flower
    Flower = Load_Texture("graphics\\flower.PNG", Size)

    #Dungeon
    Floor = Load_Texture("graphics\\floor.PNG", Size)
    Floor2 = Load_Texture("graphics\\floor2.PNG", Size)
    Light = Load_Texture("graphics\\light.PNG", Size)
    Black = Load_Texture("graphics\\black.PNG", Size)
    Wall =  Load_Texture("graphics\\wall.PNG", Size)
       

    Texture_Tags = {"1" : Grass, "2" : Grass2, "3" : Grass3, "4" : Grass4,

                    "5" : Stone, "6" : Stone2, "7": Stone3,

                    "8" : Water, "9" : Water2, "10" : Water3, "11": Water4,
                    
                    "12" : Sand, "13": Tree, "14": Tree2, "15": Tree3,

                    "16": House, "17": House2, "18": House3, "19": House4, "20": House5, "21": House6, "22": House7, "23": House8, "24": House9, "25": Flower,

                    "26": Floor, "27": Floor2, "28": Light, "29": Black, "30": Wall
                    }

   

                  
    
