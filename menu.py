import pygame, sys, random
import pickle

pygame.init()

# Screen setings
pygame.display.set_caption("TRON")
screen = pygame.display.set_mode([1000, 600])
background = pygame.Surface(screen.get_size())

# Buttons setings
top = 480; left = [60, 290, 520, 740]; width = 200; height = 80
menu_text=["Play", "Help", "About", "Quit"]
buttonColor = pygame.Color(0, 31, 63)
buttonColorActive = pygame.Color(0, 50, 102)
textColor = pygame.Color(57, 204, 204)
font = pygame.font.SysFont("14722", 40)
line_width = 0
running=True

while running:
    background.fill([0, 0, 0])

    for i in range(0, 4):
        pygame.draw.rect(background, buttonColor, [left[i], top, width, height], line_width)

        #Play button text blit
        text = font.render(menu_text[0], 1, textColor)
        background.blit(text, [left[0] + 42, top + 15])

        #Help button text blit
        text = font.render(menu_text[1], 1, textColor)
        background.blit(text, [left[1] + 45, top + 15])

        #About button text blit
        text = font.render(menu_text[2], 1, textColor)
        background.blit(text, [left[2] + 25, top + 15])

        #Exit button text blit
        text = font.render(menu_text[3], 1, textColor)
        background.blit(text, [left[3] + 50, top + 15])

    text = font.render("Menu", 1, buttonColor)
    background.blit(text, [150, 10])
    screen.blit(background, (0, 0))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            (xMousePos, yMousePos) = pygame.mouse.get_pos()#координаты курсора мыши
            for i in range (0, 4):
                if xMousePos > left[i] and xMousePos < left[i] + width and yMousePos > top and yMousePos < top + height:
                    break
            if i == 3:
                running = False #выход
                pygame.quit() 
            if i == 0:
                import TRON #игра
                running = False
            if i == 2:
                import records
                records.show_rec()
            if i == 1:
                import my_help
                my_help.myhelp() #помощь

pygame.quit()         

