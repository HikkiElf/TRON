import pygame, sys, random
import pickle

pygame.init()

# Screen setings
pygame.display.set_caption("TRON")
screen = pygame.display.set_mode([1000, 600])
background = pygame.Surface(screen.get_size())

# Buttons setings
top=[60, 210, 360, 510]; left = 400; width = 200; height = 80
menu_text=["Play", "Help", "Options", "Exit"]
buttonColor = pygame.Color(0, 31, 63)
buttonColorActive = pygame.Color(0, 50, 102)
textColor = pygame.Color(57, 204, 204)
font = pygame.font.SysFont("14722", 40)
line_width = 0
running=True

while running:
    background.fill([255,200,0])

    for i in range(0, 4):#рисуем пункты меню
        pygame.draw.rect(background, buttonColor, [left, top[i], width, height], line_width)
        text = font.render(menu_text[i], 1, textColor)
        background.blit(text, [left+50, top[i]+30])

    text = font.render("Menu", 1, buttonColor)
    background.blit(text, [150, 10])
    screen.blit(background, (0, 0))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            (xMousePos, yMousePos) = pygame.mouse.get_pos()#координаты курсора мыши
            for i in range (0, 4):
                if xMousePos > left and xMousePos < left + width and yMousePos > top[i] and yMousePos < top[i] + height:
                    break
            if i == 3:
                running = False #выход
            if i == 0:
                import TRON #игра
            if i == 2:
                import records
                records.show_rec()
            if i == 1:
                import my_help
                my_help.myhelp() #помощь

pygame.quit()         

