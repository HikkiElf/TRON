import pygame, sys
from pygame.color import THECOLORS
from pygame import font
pygame.init()

def help1():
     pygame.display.set_caption("TRON")
     screen = pygame.display.set_mode([1280, 720])
     background = pygame.image.load("images/TRONmenu2.jpg")
     color = [57, 204, 204]
     color1 = [0, 31, 63]
     top=120; left=90
     font = pygame.font.SysFont('14722', 22, False, False)
     font1 = pygame.font.SysFont('14722', 22, False, True)
     my_file = open('help.txt', 'r')#Открываем файл для чтения
     lines = my_file.readlines()# Записываем строки из файла в список lines
     my_file.close()
     dlina=len(lines)#Это количество строк
     for i in range(0,dlina):
          ln=lines[i]
          dl=len(ln) 
          ln=ln[0:dl]
          text = font.render(ln,1, color)
          text1 = font1.render(ln,1, color1)
          background.blit(text1, [left, top])
          background.blit(text, [left, top])
          top=top+20
     text = font.render("Press Escape to exit",True, color)
     text1 = font1.render("Press Escape to exit",True, color1)
     background.blit(text1, [450, 620])
     background.blit(text, [450, 620])
     screen.blit(background, (0, 0))
     pygame.display.flip()
     running=True
     while running:
          for event in pygame.event.get():
               if event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:
                         running = False
               if event.type == pygame.QUIT:
                    pygame.quit()     