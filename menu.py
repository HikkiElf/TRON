import pygame, sys, random
import pickle
from pygame.color import THECOLORS
from pygame import font
pygame.init()
pygame.display.set_caption("TRON")
screen = pygame.display.set_mode([400, 600])
background = pygame.Surface(screen.get_size())
top=[60,210,360,510]; left=100; width=200; height=80
menu_text=["Play", "Help","records","Exit"]
color = THECOLORS["blue"]
font = pygame.font.Font(None, 40)
line_width = 0
running=True
while running:
    background.fill([255,200,0])
    for i in range(0,4):#рисуем пункты меню
        pygame.draw.rect(background, color, [left, top[i], width, height], line_width)
        text = font.render(menu_text[i],1, THECOLORS ["white"])
        background.blit(text, [left+50, top[i]+30] )
    text = font.render("Menu",1, THECOLORS ["blue"])
    background.blit(text, [150,10] )
    screen.blit(background, (0, 0))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            (x,y)=pygame.mouse.get_pos()#координаты курсора мыши
            for i in range (0,4):
                if x>left and x<left+width and y>top[i] and y<top[i]+height:
                    break
            if i==3:
                running = False #выход            
            if i==0:
                import game
                game.mygame() #игра
            if i==2:
                import records
                records.show_rec()
            if i==1:
                import my_help
                my_help.myhelp() #помощь          
pygame.quit()         

