import pygame, sys, random
import pickle
import intro

pygame.init()
intro.intro()

def menu():
    # Screen setings
    pygame.display.set_caption("TRON")
    screen = pygame.display.set_mode([1280, 720])
    background = pygame.Surface(screen.get_size())
    tronLogo = pygame.image.load("images/TRON logo.png")
    TRONmenu = pygame.image.load("images/TRONmenu1.jpg")

    # Buttons setings
    xButtonPos = [60, 368, 680, 980]; width = [240, 240, 240, 240]; height = [120, 120, 120, 120]; yButtonPos = [580, 580, 580, 580]
    menu_text=["Play", "Help", "About", "Quit"]
    buttonColor = [pygame.Color(0, 31, 63), pygame.Color(0, 31, 63), pygame.Color(0, 31, 63), pygame.Color(0, 31, 63)]
    menuColor = pygame.Color(0, 50, 102)
    buttonColorActive = pygame.Color(0, 50, 102)
    textColor = pygame.Color(57, 204, 204)
    font = pygame.font.SysFont("14722", 50)
    selectSound = pygame.mixer.Sound("select.wav")
    buttonSound = pygame.mixer.Sound("button.wav")
    line_width = 0
    run=True
    count = 4

    white = pygame.Color(255, 255, 255)

    def buttonFocusedAnimation(count):
        if count == 0:
            buttonColor[0] = buttonColorActive
            xButtonPos[0] = 58
            yButtonPos[0] = 578
            width[0] = 244
            height[0] = 124
        if count == 1:
            buttonColor[1] = buttonColorActive
            xButtonPos[1] = 366
            yButtonPos[1] = 578
            width[1] = 244
            height[1] = 124
        if count == 2:
            buttonColor[2] = buttonColorActive
            xButtonPos[2] = 678
            yButtonPos[2] = 578
            width[2] = 244
            height[2] = 124
        if count == 3:
            buttonColor[3] = buttonColorActive
            xButtonPos[3] = 978
            yButtonPos[3] = 578
            width[3] = 244
            height[3] = 124

    def buttonUnfocusedAnimation(count):
        if not count == 0:
            buttonColor[0] = pygame.Color(0, 31, 63)
            xButtonPos[0] = 60
            yButtonPos[0] = 580
            width[0] = 240
            height[0] = 120
        if not count == 1:
            buttonColor[1] = pygame.Color(0, 31, 63)
            xButtonPos[1] = 368
            yButtonPos[1] = 580
            width[1] = 240
            height[1] = 120
        if not count == 2:
            buttonColor[2] = pygame.Color(0, 31, 63)
            xButtonPos[2] = 680
            yButtonPos[2] = 580
            width[2] = 240
            height[2] = 120
        if not count == 3:
            buttonColor[3] = pygame.Color(0, 31, 63)
            xButtonPos[3] = 980
            yButtonPos[3] = 580
            width[3] = 240
            height[3] = 120

            
    while run:
        background.fill([0, 0, 0])

        background.blit(TRONmenu, (-343, 0))

        background.blit(tronLogo, (140, 130))

        count = 4

        for i in range(0, 4):
            pygame.draw.rect(background, buttonColor[i], [xButtonPos[i], yButtonPos[i], width[i], height[i]], line_width)

            #Play button text blit
            text = font.render(menu_text[0], 1, textColor)
            background.blit(text, [xButtonPos[0] + 47, yButtonPos[0] + 25])

            #Help button text blit
            text = font.render(menu_text[1], 1, textColor)
            background.blit(text, [xButtonPos[1] + 50, yButtonPos[1] + 25])

            #About button text blit
            text = font.render(menu_text[2], 1, textColor)
            background.blit(text, [xButtonPos[2] + 25, yButtonPos[2] + 25])

            #Exit button text blit
            text = font.render(menu_text[3], 1, textColor)
            background.blit(text, [xButtonPos[3] + 55, yButtonPos[3] + 25])

        # text = font.render("Menu", 1, menuColor)
        # background.blit(text, [150, 10])
        screen.blit(background, (0, 0))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
            if event.type == pygame.MOUSEBUTTONDOWN:
                (xMousePos, yMousePos) = pygame.mouse.get_pos()#координаты курсора мыши
                if xMousePos > xButtonPos[0] and xMousePos < xButtonPos[0] + width[0] and yMousePos > yButtonPos[0] and yMousePos < yButtonPos[0] + height[0]:
                    import TRON #игра
                    # run = False
                    # pygame.quit()
                if xMousePos > xButtonPos[1] and xMousePos < xButtonPos[1] + width[1] and yMousePos > yButtonPos[1] and yMousePos < yButtonPos[1] + height[1]:
                    import help #помощь
                    help.help1()
                if xMousePos > xButtonPos[2] and xMousePos < xButtonPos[2] + width[2] and yMousePos > yButtonPos[2] and yMousePos < yButtonPos[2] + height[2]:
                    import about
                    about.about()
                if xMousePos > xButtonPos[3] and xMousePos < xButtonPos[3] + width[3] and yMousePos > yButtonPos[3] and yMousePos < yButtonPos[3] + height[3]:
                    run = False #выход
                    pygame.quit()

            if event.type == pygame.MOUSEMOTION:
                (xMousePos, yMousePos) = pygame.mouse.get_pos()
                if xMousePos > xButtonPos[0] and xMousePos < xButtonPos[0] + width[0] and yMousePos > yButtonPos[0] and yMousePos < yButtonPos[0] + height[0]:
                    count = 0
                if xMousePos > xButtonPos[1] and xMousePos < xButtonPos[1] + width[1] and yMousePos > yButtonPos[1] and yMousePos < yButtonPos[1] + height[1]:
                    count = 1
                if xMousePos > xButtonPos[2] and xMousePos < xButtonPos[2] + width[2] and yMousePos > yButtonPos[2] and yMousePos < yButtonPos[2] + height[2]:
                    count = 2
                if xMousePos > xButtonPos[3] and xMousePos < xButtonPos[3] + width[3] and yMousePos > yButtonPos[3] and yMousePos < yButtonPos[3] + height[3]:
                    count = 3
                buttonFocusedAnimation(count)
                buttonUnfocusedAnimation(count)


    pygame.quit()         