import pygame
from pygame.locals import *
blue = (0, 0, 200)
orange = (255,165,0)
yellow = (255,255,0)
grey = (90, 90, 90)
pale = (212, 178, 141)
cyan = (2, 245, 249)
blues = (6, 2, 249)
#bum ass code lmao
screen = pygame.display.set_mode((1500, 1000))
pygame.display.set_caption('Solar System, Rustycloc, 6/12/2023')
earth = pygame.draw.circle(screen, blue, (250,500), 22.7861230329)
mars = pygame.draw.circle(screen,orange,(300,500), 12.1494992847)
venus = pygame.draw.circle(screen, yellow, (175,500), 21.6452074392)
mercury = pygame.draw.circle(screen,grey,(125,500),8.72496423462)
jupiter = pygame.draw.circle(screen, pale, (600,500), 255.693848355)
Uranus = pygame.draw.circle(screen, cyan, (1000, 500), 91.4127324749)
neptune = pygame.draw.circle(screen, blues, (1250,500), 88.5193133047)
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont("arial", 30)
while True:

    mos_x, mos_y = pygame.mouse.get_pos()
    color = screen.get_at((mos_x,mos_y))
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
         exit()

      pygame.display.update()


    
    #earth
    if color == blue:
        pygame.draw.rect(screen,(0,0,0),(0,0,1000,100))
        spacetext = myfont.render('Earth, Avg Temp 15 C, Diameter 12,742 km', 0, (100,100,100))
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
        spacetext = myfont.render('Mars, Avg Temp -63 C, Diameter 6,794 km', 0, (100,100,100))
        screen.blit(spacetext, (0,0))
        pygame.display.update()
    #end of mars
    #venus
    if color == yellow:
        pygame.draw.rect(screen,(0,0,0),(0,0,1000,100))
        spacetext = myfont.render('Venus, Avg Temp 462 C, Diameter 12,104 km', 0, (100,100,100))
        screen.blit(spacetext, (0,0))
        pygame.display.update()
    #end of venus
    #mercury
    if color == grey:
        pygame.draw.rect(screen,(0,0,0),(0,0,1000,100))
        spacetext = myfont.render('Mercury, Avg Temp 427 C, Diameter 4,879 km', 0, (100,100,100))
        screen.blit(spacetext, (0,0))
        pygame.display.update()
    #end of mercury
    #jupiter
    if color == pale:
        pygame.draw.rect(screen,(0,0,0),(0,0,1000,100))
        spacetext = myfont.render('Jupiter, Avg Temp -145 C, Diameter 142,984 km', 0, (100,100,100))
        screen.blit(spacetext, (0,0))
        pygame.display.update()
    #end of jupiter
    #uranus
    if color == cyan:
        pygame.draw.rect(screen,(0,0,0),(0,0,1000,100))
        spacetext = myfont.render('Uranus, Avg Temp -195 C, Diameter 51,118 km', 0, (100,100,100))
        screen.blit(spacetext, (0,0))
        pygame.display.update()
    #end of uranus
    #neptune
    if color == blues:
        pygame.draw.rect(screen,(0,0,0),(0,0,1000,100))
        spacetext = myfont.render('Neptune, Avg Temp -214 C, Diameter 49,500 km', 0, (100,100,100))
        screen.blit(spacetext, (0,0))
        pygame.display.update()
    #end of neptune



   