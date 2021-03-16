import pygame
import sys
pygame.init()
pygame.display.set_caption("TRON")
def intro():
    music2 = pygame.mixer.Sound("data/audio/Start.wav")
    music2.set_volume(0.5)
    music2.play()
    screen = pygame.display.set_mode([1280, 720])
    intro_pic = pygame.image.load('data/images/splash screen copy.png')
    screen.blit(intro_pic, (0, 0))
    pygame.display.flip()
    running=True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                (xMousePos, yMousePos) = pygame.mouse.get_pos()
                if xMousePos > 0 and xMousePos < 1000 and yMousePos > 0 and yMousePos < 600:
                    running = False
