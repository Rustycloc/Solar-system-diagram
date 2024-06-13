import sys
import pygame

blue = (0, 0, 200)
orange = (255,165,0)
yellow = (255,255,0)
grey = (90, 90, 90)
pale = (212, 178, 141)
cyan = (2, 245, 249)
blues = (6, 2, 249)
blue_grey = (226, 234, 244)
pale_grey = (207, 191, 170)
red_grey = (120, 95, 95)
crimson = (58, 35, 35)
drk_grey = (131, 131, 131)

screen = pygame.display.set_mode((1500, 1000))
pygame.display.set_caption('Solar System, Rustycloc, 6/13/2024')
earth = pygame.draw.circle(screen, blue, (237.5,500), 22.7861230329)
mars = pygame.draw.circle(screen,orange,(300,500), 12.1494992847)
venus = pygame.draw.circle(screen, yellow, (175,500), 21.6452074392)
mercury = pygame.draw.circle(screen,grey,(125,500),8.72496423462)
jupiter = pygame.draw.circle(screen, pale, (600,500), 255.693848355)
uranus = pygame.draw.circle(screen, cyan, (1000, 500), 91.4127324749)
neptune = pygame.draw.circle(screen, blues, (1250,500), 88.5193133047)
pluto = pygame.draw.circle(screen, blue_grey, (1375, 500), 4.23819742489)
ceres = pygame.draw.circle(screen, pale_grey,(325, 500), 1)
haumea = pygame.draw.circle(screen, red_grey,(1125, 500), 3.11158798283)
makemake = pygame.draw.circle(screen, crimson, (1400, 500), 2.55722460658)
eris = pygame.draw.circle(screen, drk_grey, (1450, 500),4.18097281831)

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont("arial", 30)

error_text = "\033[0;31mYOUR CODE SUCKS!!!!!!!!!!!!!!!!!! YOU GOT AN ERROR!!!!!!!!!!!!! BOOOOOOOOOO!!!! oh btw its \033[0m"

while True:
    try:
        mos_x, mos_y = pygame.mouse.get_pos()
        color = screen.get_at((mos_x,mos_y))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() 
                sys.exit(1)

            pygame.display.update()
    except Exception as exception:
        print(error_text + str(exception))
        pass

    try: # probably not the best way to do this
        #earth
        if color == blue:
            pygame.draw.rect(screen,(0,0,0),(0,0,1000,100))
            spacetext = myfont.render('Earth, Planet, Avg Temp 15 C, Diameter 12,742 km', 0, (100,100,100))
            screen.blit(spacetext, (0,0))
            pygame.display.update()
        #end of earth

        #space
        if color == (0,0,0):
            pygame.draw.rect(screen,(0,0,0),(0,0,1000,100))
            spacetext = myfont.render('Space', 0, (100,100,100))
            screen.blit(spacetext, (0,0))
            pygame.display.update()
        #end of space
        #mars
        if color == orange:
            pygame.draw.rect(screen,(0,0,0),(0,0,1000,100))
            spacetext = myfont.render('Mars, Planet, Avg Temp -63 C, Diameter 6,794 km', 0, (100,100,100))
            screen.blit(spacetext, (0,0))
            pygame.display.update()
        #end of mars
        #venus
        if color == yellow:
            pygame.draw.rect(screen,(0,0,0),(0,0,1000,100))
            spacetext = myfont.render('Venus, Planet, Avg Temp 462 C, Diameter 12,104 km', 0, (100,100,100))
            screen.blit(spacetext, (0,0))
            pygame.display.update()
        #end of venus
        #mercury
        if color == grey:
            pygame.draw.rect(screen,(0,0,0),(0,0,1000,100))
            spacetext = myfont.render('Mercury, Planet, Avg Temp 427 C, Diameter 4,879 km', 0, (100,100,100))
            screen.blit(spacetext, (0,0))
            pygame.display.update()
        #end of mercury
        #jupiter
        if color == pale:
            pygame.draw.rect(screen,(0,0,0),(0,0,1000,100))
            spacetext = myfont.render('Jupiter, Planet, Avg Temp -145 C, Diameter 142,984 km', 0, (100,100,100))
            screen.blit(spacetext, (0,0))
            pygame.display.update()
        #end of jupiter
        #uranus
        if color == cyan:
            pygame.draw.rect(screen,(0,0,0),(0,0,1000,100))
            spacetext = myfont.render('Uranus, Planet, Avg Temp -195 C, Diameter 51,118 km', 0, (100,100,100))
            screen.blit(spacetext, (0,0))
            pygame.display.update()
        #end of uranus
        #neptune
        if color == blues:
            pygame.draw.rect(screen,(0,0,0),(0,0,1000,100))
            spacetext = myfont.render('Neptune, Planet, Avg Temp -214 C, Diameter 49,500 km', 0, (100,100,100))
            screen.blit(spacetext, (0,0))
            pygame.display.update()
        #end of neptune
        #pluto
        if color == blue_grey:
            pygame.draw.rect(screen,(0,0,0),(0,0,1000,100))
            spacetext = myfont.render('Pluto, Dwarf Planet, Avg Temp -240 C, Diameter 2,370 km', 0, (100,100,100))
            screen.blit(spacetext, (0,0))
            pygame.display.update()
        #end of pluto    
        #cerus
        if color == pale_grey:
            pygame.draw.rect(screen,(0,0,0),(0,0,1000,100))
            spacetext = myfont.render('Cerus, Dwarf Planet, Avg Temp -70 C, Diameter 476 km', 0, (100,100,100))
            screen.blit(spacetext, (0,0))
            pygame.display.update()
        #end of cerus    
        #haumea
        if color == red_grey:
            pygame.draw.rect(screen,(0,0,0),(0,0,1000,100))
            spacetext = myfont.render('Haumea, Dwarf Planet, Avg Temp -241 C, Diameter 1,740 km', 0, (100,100,100))
            screen.blit(spacetext, (0,0))
            pygame.display.update()
        #end of haumea    
        #makemake
        if color == crimson:
            pygame.draw.rect(screen,(0,0,0),(0,0,1000,100))
            spacetext = myfont.render('Makemake, Dwarf Planet, Avg Temp -230 C, Diameter 1,430 km', 0, (100,100,100))
            screen.blit(spacetext, (0,0))
            pygame.display.update()
        #end of makemake    
        #eris
        if color == drk_grey:
            pygame.draw.rect(screen,(0,0,0),(0,0,1000,100))
            spacetext = myfont.render('Eris, Dwarf Planet, Avg Temp -243 C, Diameter 2,338 km', 0, (100,100,100))
            screen.blit(spacetext, (0,0))
            pygame.display.update()
        #end of eris
    except Exception as exception:
        print(error_text + str(exception))
        pass
