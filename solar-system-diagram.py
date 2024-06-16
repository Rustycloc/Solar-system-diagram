import pygame
import sys
import random
i=0

class make_circle():
    def __init__(self) -> None:
        x = str(random.randint(1350, 1400))
        y = str(random.randint(0,1000))
        circle = pygame.draw.circle(screen, kuiper_grey, (int(x),int(y)), 1)










blue = (0, 0, 200)
orange = (255,165,0)
yellow = (255,255,0)
grey = (90, 90, 90)
kuiper_grey = (91, 91, 91)
pale = (212, 178, 141)
cyan = (2, 245, 249)
blues = (6, 2, 249)
blue_grey = (226, 234, 244)
pale_grey = (207, 191, 170)
red_grey = (120, 95, 95)
crimson = (58, 35, 35)
drk_grey = (131, 131, 131)
#bum ass code lmao
screen = pygame.display.set_mode((1500, 1000))
pygame.display.set_caption('Solar System, Rustycloc, 6/13/2024')
earth = pygame.draw.circle(screen, blue, (137.5,500), 22.7861230329)
mars = pygame.draw.circle(screen,orange,(200,500), 12.1494992847)
venus = pygame.draw.circle(screen, yellow, (75,500), 21.6452074392)
mercury = pygame.draw.circle(screen,grey,(25,500),8.72496423462)
jupiter = pygame.draw.circle(screen, pale, (500,500), 255.693848355)
while i < 2500:
    make_circle()
    i += 1
Uranus = pygame.draw.circle(screen, cyan, (900, 500), 91.4127324749)
neptune = pygame.draw.circle(screen, blues, (1150,500), 88.5193133047)
pluto = pygame.draw.circle(screen, blue_grey, (1300, 500), 4.23819742489)
ceres = pygame.draw.circle(screen, pale_grey,(225, 500), 1)
haumea = pygame.draw.circle(screen, red_grey,(1025, 500), 3.11158798283)
makemake = pygame.draw.circle(screen, crimson, (1325, 500), 2.55722460658)
eris = pygame.draw.circle(screen, drk_grey, (1425, 500),4.18097281831)
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont("arial", 30)
while True:

    mos_x, mos_y = pygame.mouse.get_pos()
    color = screen.get_at((mos_x,mos_y))
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
         sys.exit(1)

    pygame.display.update()     
    print(mos_x, mos_y)          

    
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
        spacetext = myfont.render('Venus, Planet. Avg Temp 462 C, Diameter 12,104 km', 0, (100,100,100))
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


    if color == kuiper_grey:
        pygame.draw.rect(screen, (0,0,0),(0,0,1000,100))
        spacetext = myfont.render("Astroid, Kuiper belt", 0, (100, 100, 100))
        screen.blit(spacetext, (0,0))
        pygame.display.update()






   