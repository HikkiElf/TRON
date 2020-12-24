#   TRON GAME
#   Truhanov Vsevolod
#   Python 3.9.0 Pygame

import pygame
import sys
import time
import random
import menu
pygame.init()
pygame.mixer.init()

# Sound
music = pygame.mixer.Sound("music.mp3")
boomSound = pygame.mixer.Sound("boom_sound.wav")
pygame.mixer.music.set_volume(0.1)
# music.play()

# Play Surface
size = width, height = 1280, 720
playSurface = pygame.display.set_mode(size)
pygame.display.set_caption("TRON")
background = pygame.image.load("images/TRON2.png")

# Colors
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
brown = pygame.Color(165, 42, 42)
blue = pygame.Color(0, 255, 255)

# Font
globalFontMini = pygame.font.SysFont('monaco', 150)
globalFont = pygame.font.SysFont('monaco', 300)
globalOutlineFontMini = pygame.font.SysFont('monaco', 153)
globalOutlineFont = pygame.font.SysFont('monaco', 303)

# Text Press space
PressSpaceOutlineSurf = globalOutlineFontMini.render("Press space", True, black)
PressSpaceSurf = globalFontMini.render("Press space", True, white)
PressSpaceOutlineRect = PressSpaceOutlineSurf.get_rect()
PressSpaceRect = PressSpaceSurf.get_rect()
PressSpaceOutlineRect.midtop = (640, 460)
PressSpaceRect.midtop = (640, 460)

# Text blue wins
blueOutlineSurf = globalOutlineFont.render("Blue Wins", True, black)
blueSurf = globalFont.render("Blue Wins", True, blue)
blueOutlineRect = blueOutlineSurf.get_rect()
blueRect = blueSurf.get_rect()
blueOutlineRect.midtop = (640, 260)
blueRect.midtop = (640, 260)

# Text red wins
redOutlineSurf = globalOutlineFont.render("Red Wins", True, black)
redSurf = globalFont.render("Red Wins", True, red)
redOutlineRect = redOutlineSurf.get_rect()
redRect = redSurf.get_rect()
redOutlineRect.midtop = (640, 260)
redRect.midtop = (640, 260)

# Text draw
drawOutlineSurf = globalOutlineFont.render("Draw", True, black)
drawSurf = globalFont.render("Draw", True, white)
drawOutlineRect = drawOutlineSurf.get_rect()
drawRect = drawSurf.get_rect()
drawOutlineRect.midtop = (640, 260)
drawRect.midtop = (640, 260)

# FPS controller
fpsController = pygame.time.Clock()

# Game settings
speed = 10
boostSpeed = 20
redCarPos = [100, 360]
blueCarPos = [1180, 360]
# redCarPosNG = [100, 360]
# blueCarPosNG = [1180, 360]
redCarLine = [[100, 360]]
blueCarLine = [[1180, 360]]
direction = 'RIGHT'
direction1 = 'LEFT'
changeto = ''
changeto1 = ''
redBikeScore = 0
blueBikeScore = 0
animCount = 0
winCount = 0
state = "BEGIN" # RUNNING, END
winner: pygame.Color
loser: pygame.Color
menu = True
running = True

# Red bike images
redBikeLeftImage = pygame.image.load("images/bikeRed.png")
redBikeUpImage = pygame.transform.rotate(redBikeLeftImage, -90)
redBikeDownImage = pygame.transform.rotate(redBikeLeftImage, 90)
redBikeRightImage = pygame.transform.rotate(redBikeLeftImage, 180)

# Blue bike images
blueBikeLeftImage = pygame.image.load("images/bikeBlue.png")
blueBikeUpImage = pygame.transform.rotate(blueBikeLeftImage, -90)
blueBikeDownImage = pygame.transform.rotate(blueBikeLeftImage, 90)
blueBikeRightImage = pygame.transform.rotate(blueBikeLeftImage, 180)

# Draw round count dots
def roundCount(color: pygame.Color):
    global redBikeScore, blueBikeScore

    pygame.draw.circle(playSurface, white, [320, 20], 12, 1)
    pygame.draw.circle(playSurface, white, [342, 20], 12, 1)
    pygame.draw.circle(playSurface, white, [364, 20], 12, 1)
    pygame.draw.circle(playSurface, white, [386, 20], 12, 1)
    pygame.draw.circle(playSurface, white, [408, 20], 12, 1)
    pygame.draw.circle(playSurface, white, [430, 20], 12, 1)
    pygame.draw.circle(playSurface, white, [452, 20], 12, 1)
    pygame.draw.circle(playSurface, white, [474, 20], 12, 1)
    pygame.draw.circle(playSurface, white, [496, 20], 12, 1)
    pygame.draw.circle(playSurface, white, [518, 20], 12, 1)

    pygame.draw.circle(playSurface, white, [964, 20], 12, 1)
    pygame.draw.circle(playSurface, white, [942, 20], 12, 1)
    pygame.draw.circle(playSurface, white, [920, 20], 12, 1)
    pygame.draw.circle(playSurface, white, [898, 20], 12, 1)
    pygame.draw.circle(playSurface, white, [876, 20], 12, 1)
    pygame.draw.circle(playSurface, white, [854, 20], 12, 1)
    pygame.draw.circle(playSurface, white, [832, 20], 12, 1)
    pygame.draw.circle(playSurface, white, [810, 20], 12, 1)
    pygame.draw.circle(playSurface, white, [788, 20], 12, 1)
    pygame.draw.circle(playSurface, white, [766, 20], 12, 1)

    if color == red:
        if redBikeScore >= 1:
            pygame.draw.circle(playSurface, red, [320, 20], 11, 0)
        if redBikeScore >= 2:
            pygame.draw.circle(playSurface, red, [320, 20], 11, 0)
            pygame.draw.circle(playSurface, red, [342, 20], 11, 0)
        if redBikeScore >= 3:
            pygame.draw.circle(playSurface, red, [320, 20], 11, 0)
            pygame.draw.circle(playSurface, red, [342, 20], 11, 0)
            pygame.draw.circle(playSurface, red, [364, 20], 11, 0)
        if redBikeScore >= 4:
            pygame.draw.circle(playSurface, red, [320, 20], 11, 0)
            pygame.draw.circle(playSurface, red, [342, 20], 11, 0)
            pygame.draw.circle(playSurface, red, [364, 20], 11, 0)
            pygame.draw.circle(playSurface, red, [386, 20], 11, 0)
        if redBikeScore >= 5:
            pygame.draw.circle(playSurface, red, [320, 20], 11, 0)
            pygame.draw.circle(playSurface, red, [342, 20], 11, 0)
            pygame.draw.circle(playSurface, red, [364, 20], 11, 0)
            pygame.draw.circle(playSurface, red, [386, 20], 11, 0)
            pygame.draw.circle(playSurface, red, [408, 20], 11, 0)
        if redBikeScore >= 6:
            pygame.draw.circle(playSurface, red, [320, 20], 11, 0)
            pygame.draw.circle(playSurface, red, [342, 20], 11, 0)
            pygame.draw.circle(playSurface, red, [364, 20], 11, 0)
            pygame.draw.circle(playSurface, red, [386, 20], 11, 0)
            pygame.draw.circle(playSurface, red, [408, 20], 11, 0)
            pygame.draw.circle(playSurface, red, [430, 20], 11, 0)
        if redBikeScore >= 7:
            pygame.draw.circle(playSurface, red, [320, 20], 11, 0)
            pygame.draw.circle(playSurface, red, [342, 20], 11, 0)
            pygame.draw.circle(playSurface, red, [364, 20], 11, 0)
            pygame.draw.circle(playSurface, red, [386, 20], 11, 0)
            pygame.draw.circle(playSurface, red, [408, 20], 11, 0)
            pygame.draw.circle(playSurface, red, [430, 20], 11, 0)
            pygame.draw.circle(playSurface, red, [452, 20], 11, 0)
        if redBikeScore >= 8:
            pygame.draw.circle(playSurface, red, [320, 20], 11, 0)
            pygame.draw.circle(playSurface, red, [342, 20], 11, 0)
            pygame.draw.circle(playSurface, red, [364, 20], 11, 0)
            pygame.draw.circle(playSurface, red, [386, 20], 11, 0)
            pygame.draw.circle(playSurface, red, [408, 20], 11, 0)
            pygame.draw.circle(playSurface, red, [430, 20], 11, 0)
            pygame.draw.circle(playSurface, red, [452, 20], 11, 0)
            pygame.draw.circle(playSurface, red, [474, 20], 11, 0)
        if redBikeScore >= 9:
            pygame.draw.circle(playSurface, red, [320, 20], 11, 0)
            pygame.draw.circle(playSurface, red, [342, 20], 11, 0)
            pygame.draw.circle(playSurface, red, [364, 20], 11, 0)
            pygame.draw.circle(playSurface, red, [386, 20], 11, 0)
            pygame.draw.circle(playSurface, red, [408, 20], 11, 0)
            pygame.draw.circle(playSurface, red, [430, 20], 11, 0)
            pygame.draw.circle(playSurface, red, [452, 20], 11, 0)
            pygame.draw.circle(playSurface, red, [474, 20], 11, 0)
            pygame.draw.circle(playSurface, red, [496, 20], 11, 0)
        if redBikeScore >= 10:
            pygame.draw.circle(playSurface, red, [320, 20], 11, 0)
            pygame.draw.circle(playSurface, red, [342, 20], 11, 0)
            pygame.draw.circle(playSurface, red, [364, 20], 11, 0)
            pygame.draw.circle(playSurface, red, [386, 20], 11, 0)
            pygame.draw.circle(playSurface, red, [408, 20], 11, 0)
            pygame.draw.circle(playSurface, red, [430, 20], 11, 0)
            pygame.draw.circle(playSurface, red, [452, 20], 11, 0)
            pygame.draw.circle(playSurface, red, [474, 20], 11, 0)
            pygame.draw.circle(playSurface, red, [496, 20], 11, 0)
            pygame.draw.circle(playSurface, red, [518, 20], 11, 0)


    if color == blue:
        if blueBikeScore >= 1:
            pygame.draw.circle(playSurface, blue, [964, 20], 11, 0)
        if blueBikeScore >= 2:
            pygame.draw.circle(playSurface, blue, [964, 20], 11, 0)
            pygame.draw.circle(playSurface, blue, [942, 20], 11, 0)
        if blueBikeScore >= 3:
            pygame.draw.circle(playSurface, blue, [964, 20], 11, 0)
            pygame.draw.circle(playSurface, blue, [942, 20], 11, 0)
            pygame.draw.circle(playSurface, blue, [920, 20], 11, 0)
        if blueBikeScore >= 4:
            pygame.draw.circle(playSurface, blue, [964, 20], 11, 0)
            pygame.draw.circle(playSurface, blue, [942, 20], 11, 0)
            pygame.draw.circle(playSurface, blue, [920, 20], 11, 0)
            pygame.draw.circle(playSurface, blue, [898, 20], 11, 0)
        if blueBikeScore >= 5:
            pygame.draw.circle(playSurface, blue, [964, 20], 11, 0)
            pygame.draw.circle(playSurface, blue, [942, 20], 11, 0)
            pygame.draw.circle(playSurface, blue, [920, 20], 11, 0)
            pygame.draw.circle(playSurface, blue, [898, 20], 11, 0)
            pygame.draw.circle(playSurface, blue, [876, 20], 11, 0)
        if blueBikeScore >= 6:
            pygame.draw.circle(playSurface, blue, [964, 20], 11, 0)
            pygame.draw.circle(playSurface, blue, [942, 20], 11, 0)
            pygame.draw.circle(playSurface, blue, [920, 20], 11, 0)
            pygame.draw.circle(playSurface, blue, [898, 20], 11, 0)
            pygame.draw.circle(playSurface, blue, [876, 20], 11, 0)
            pygame.draw.circle(playSurface, blue, [854, 20], 11, 0)
        if blueBikeScore >= 7:
            pygame.draw.circle(playSurface, blue, [964, 20], 11, 0)
            pygame.draw.circle(playSurface, blue, [942, 20], 11, 0)
            pygame.draw.circle(playSurface, blue, [920, 20], 11, 0)
            pygame.draw.circle(playSurface, blue, [898, 20], 11, 0)
            pygame.draw.circle(playSurface, blue, [876, 20], 11, 0)
            pygame.draw.circle(playSurface, blue, [854, 20], 11, 0)
            pygame.draw.circle(playSurface, blue, [832, 20], 11, 0)
        if blueBikeScore >= 8:
            pygame.draw.circle(playSurface, blue, [964, 20], 11, 0)
            pygame.draw.circle(playSurface, blue, [942, 20], 11, 0)
            pygame.draw.circle(playSurface, blue, [920, 20], 11, 0)
            pygame.draw.circle(playSurface, blue, [898, 20], 11, 0)
            pygame.draw.circle(playSurface, blue, [876, 20], 11, 0)
            pygame.draw.circle(playSurface, blue, [854, 20], 11, 0)
            pygame.draw.circle(playSurface, blue, [832, 20], 11, 0)
            pygame.draw.circle(playSurface, blue, [810, 20], 11, 0)
        if blueBikeScore >= 9:
            pygame.draw.circle(playSurface, blue, [964, 20], 11, 0)
            pygame.draw.circle(playSurface, blue, [942, 20], 11, 0)
            pygame.draw.circle(playSurface, blue, [920, 20], 11, 0)
            pygame.draw.circle(playSurface, blue, [898, 20], 11, 0)
            pygame.draw.circle(playSurface, blue, [876, 20], 11, 0)
            pygame.draw.circle(playSurface, blue, [854, 20], 11, 0)
            pygame.draw.circle(playSurface, blue, [832, 20], 11, 0)
            pygame.draw.circle(playSurface, blue, [810, 20], 11, 0)
            pygame.draw.circle(playSurface, blue, [788, 20], 11, 0)
        if blueBikeScore >= 10:
            pygame.draw.circle(playSurface, blue, [964, 20], 11, 0)
            pygame.draw.circle(playSurface, blue, [942, 20], 11, 0)
            pygame.draw.circle(playSurface, blue, [920, 20], 11, 0)
            pygame.draw.circle(playSurface, blue, [898, 20], 11, 0)
            pygame.draw.circle(playSurface, blue, [876, 20], 11, 0)
            pygame.draw.circle(playSurface, blue, [854, 20], 11, 0)
            pygame.draw.circle(playSurface, blue, [832, 20], 11, 0)
            pygame.draw.circle(playSurface, blue, [810, 20], 11, 0)
            pygame.draw.circle(playSurface, blue, [788, 20], 11, 0)
            pygame.draw.circle(playSurface, blue, [766, 20], 11, 0)

# Player win
def playerWin(color: pygame.Color):
    global blue, red, blueBikeScore, redBikeScore, running, direction, direction1
    message = str
    if color == blue:
        message = "Blue Wins"
        blueBikeScore += 1
    else:
        message = "Red Wins"
        redBikeScore += 1
    direction = "RIGHT"
    direction1 = "LEFT"
    pygame.display.flip() 
    menu = True
  
# Boom animation
def boom(color: pygame.Color):
    global animCount
    bang = [pygame.image.load("images/Explosion_1.png"), pygame.image.load("images/Explosion_2.png"), 
    pygame.image.load("images/Explosion_3.png"), pygame.image.load("images/Explosion_4.png")]
    bangReverse = pygame.image.load("images/Explosion_2.png") 
    animCount += 1
    if animCount + 1 >= 20:
        animCount = 0
    if color == red:
        if animCount // 5 == 0:
            playSurface.blit(bang[0], (redCarPos[0] - 8, redCarPos[1] - 20))
        if animCount // 5 == 1:
            playSurface.blit(bang[1], (redCarPos[0] - 52, redCarPos[1] - 50))
        if animCount // 5 == 2:
            playSurface.blit(bang[2], (redCarPos[0] - 87, redCarPos[1] - 84))
        if animCount // 5 == 3:
            playSurface.blit(bangReverse, (redCarPos[0] - 52, redCarPos[1] - 50))
    else:
        if animCount // 5 == 0:
            playSurface.blit(bang[0], (blueCarPos[0] - 8, blueCarPos[1] - 20))
        if animCount // 5 == 1:
            playSurface.blit(bang[1], (blueCarPos[0] - 52, blueCarPos[1] - 50))
        if animCount // 5 == 2:
            playSurface.blit(bang[2], (blueCarPos[0] - 87, blueCarPos[1] - 84))
        if animCount // 5 == 3:
            playSurface.blit(bangReverse, (blueCarPos[0] - 52, blueCarPos[1] - 50))

def newRound():
    global redCarPos, blueCarPos
    redCarPos = [100, 360]
    blueCarPos = [1180, 360]
    del redCarLine[:]
    del blueCarLine[:]

def roundWin(color: pygame.Color):
    globalFontWin = pygame.font.SysFont('monaco', 200)
    globalOutlineFontWin = pygame.font.SysFont('monaco', 203)
    if color == red:
        # Text red win round
        redOutlineSurfWin = globalOutlineFontWin.render("Red Win Round : {0}".format(redBikeScore), True, black)
        redSurfWin = globalFontWin.render("Red Win Round : {0}".format(redBikeScore), True, red)
        redOutlineRectWin = redOutlineSurfWin.get_rect()
        redRectWin = redSurfWin.get_rect()
        redOutlineRectWin.midtop = (640, 260)
        redRectWin.midtop = (640, 260)
        playSurface.blit(redOutlineSurfWin, redOutlineRectWin)
        playSurface.blit(redSurfWin, redRectWin)
    else:
        # Text blue win round
        blueOutlineSurfWin = globalOutlineFontWin.render("Blue Win Round : {0}".format(blueBikeScore), True, black)
        blueSurfWin = globalFontWin.render("Blue Win Round : {0}".format(blueBikeScore), True, blue)
        blueOutlineRectWin = blueOutlineSurfWin.get_rect()
        blueRectWin = blueSurfWin.get_rect()
        blueOutlineRectWin.midtop = (640, 260)
        blueRectWin.midtop = (640, 260)
        playSurface.blit(blueOutlineSurfWin, blueOutlineRectWin)
        playSurface.blit(blueSurfWin, blueRectWin)




while running:
    playSurface.blit(background, (0, 0))
    pygame.draw.rect(playSurface, black, pygame.Rect(0, 0, 1280, 52))

    if state == "BEGIN":

        if redBikeScore == 10:
            redBikeScore = 0
            blueBikeScore = 0
        if blueBikeScore == 10:
            redBikeScore = 0
            blueBikeScore = 0

        roundCount(red)
        roundCount(blue)
        
        # handle keydown event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    menu = True
                if event.key == pygame.K_d:
                    changeto = 'RIGHT'
                if event.key == pygame.K_a:
                    changeto = 'LEFT'
                if event.key == pygame.K_w:
                    changeto = 'UP'
                if event.key == pygame.K_s:
                    changeto = 'DOWN'
                if event.key == pygame.K_RIGHT:
                    changeto1 = 'RIGHT'
                if event.key == pygame.K_LEFT:
                    changeto1 = 'LEFT'
                if event.key == pygame.K_UP:
                    changeto1 = 'UP'
                if event.key == pygame.K_DOWN:
                    changeto1 = 'DOWN'
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))

        # draw player bikes
        playSurface.blit(redBikeRightImage, (redCarPos[0]-40, redCarPos[1]-55))
        playSurface.blit(blueBikeLeftImage, (blueCarPos[0]-55, blueCarPos[1]-35))

        if changeto != '' and changeto1 != '':
            state = 'RUNNING'
    
    elif state == 'RUNNING':

        roundCount(red)
        roundCount(blue)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    menu = True
                if event.key == pygame.K_d:
                    changeto = 'RIGHT'
                if event.key == pygame.K_a:
                    changeto = 'LEFT'
                if event.key == pygame.K_w:
                    changeto = 'UP'
                if event.key == pygame.K_s:
                    changeto = 'DOWN'
                if event.key == pygame.K_RIGHT:
                    changeto1 = 'RIGHT'
                if event.key == pygame.K_LEFT:
                    changeto1 = 'LEFT'
                if event.key == pygame.K_UP:
                    changeto1 = 'UP'
                if event.key == pygame.K_DOWN:
                    changeto1 = 'DOWN'
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))

        # Validate direction
        if changeto == 'RIGHT' and direction != 'LEFT':
            direction = changeto
        if changeto == 'LEFT' and direction != 'RIGHT':
            direction = changeto
        if changeto == 'UP' and direction != 'DOWN':
            direction = changeto
        if changeto == 'DOWN' and direction != 'UP':
            direction = changeto
        if changeto1 == 'RIGHT' and direction1 != 'LEFT':
            direction1 = changeto1
        if changeto1 == 'LEFT' and direction1 != 'RIGHT':
            direction1 = changeto1
        if changeto1 == 'UP' and direction1 != 'DOWN':
            direction1 = changeto1
        if changeto1 == 'DOWN' and direction1 != 'UP':
            direction1 = changeto1

        # Update  position
        if direction == 'RIGHT':
            redCarPos[0] += speed
        if direction == 'LEFT':
            redCarPos[0] -= speed
        if direction == 'DOWN':
            redCarPos[1] += speed
        if direction == 'UP':
            redCarPos[1] -= speed
        if direction1 == 'RIGHT':
            blueCarPos[0] += speed
        if direction1 == 'LEFT':
            blueCarPos[0] -= speed
        if direction1 == 'DOWN':
            blueCarPos[1] += speed
        if direction1 == 'UP':
            blueCarPos[1] -= speed

        # Line mechanism
        redCarLine.insert(0, list(redCarPos))
        blueCarLine.insert(0, list(blueCarPos))

        for pos in redCarLine:
            pygame.draw.rect(playSurface, red, pygame.Rect(pos[0], pos[1], speed, speed))
        for pos1 in blueCarLine:
            pygame.draw.rect(playSurface, blue, pygame.Rect(pos1[0], pos1[1], speed, speed))
        
        # Red car correct blit
        if direction == "RIGHT":
            playSurface.blit(redBikeRightImage, (redCarPos[0]-40, redCarPos[1]-55))
        if direction == "UP":
            playSurface.blit(redBikeUpImage, (redCarPos[0]-55, redCarPos[1]-35))
        if direction == "DOWN":
            playSurface.blit(redBikeDownImage, (redCarPos[0]-35, redCarPos[1]-55))
        if direction == "LEFT":
            playSurface.blit(redBikeLeftImage, (redCarPos[0]-55, redCarPos[1]-35))
        
        # Blue car correct blit
        if direction1 == "RIGHT":
            playSurface.blit(blueBikeRightImage, (blueCarPos[0]-40, blueCarPos[1]-55))
        if direction1 == "UP":
            playSurface.blit(blueBikeUpImage, (blueCarPos[0]-55, blueCarPos[1]-35))
        if direction1 == "DOWN":
            playSurface.blit(blueBikeDownImage, (blueCarPos[0]-35, blueCarPos[1]-55))
        if direction1 == "LEFT":
            playSurface.blit(blueBikeLeftImage, (blueCarPos[0]-55, blueCarPos[1]-35))

        # Draw
        if (redCarPos[0] == blueCarPos[0] and redCarPos[1] == blueCarPos[1]):
            boomSound.play()
            winner = red
            loser = red
            state = 'END'

        # Bounds
        if (redCarPos[0] >= width or redCarPos[0] < 0) and (blueCarPos[0] >= width or blueCarPos[0] < 0):
            boomSound.play()
            winner = red
            loser = red
            state = 'END'
        if (redCarPos[1] >= height or redCarPos[1] <= 40) and (blueCarPos[1] >= height or blueCarPos[1] <= 40):
            boomSound.play()
            winner = red
            loser = red
            state = 'END'
        if redCarPos[0] >= width or redCarPos[0] < 0 and state != "END":
            boomSound.play()
            state = 'END'
            winner = blue
            loser = red
            playerWin(winner)
        if redCarPos[1] >= height or redCarPos[1] <= 40 and state != "END":
            boomSound.play()
            state = 'END'
            winner = blue
            loser = red
            playerWin(winner)
        if blueCarPos[0] >= width or blueCarPos[0] < 0 and state != "END":
            boomSound.play()
            state = 'END'
            winner = red
            loser = blue
            playerWin(winner)
        if blueCarPos[1] >= height or blueCarPos[1] <= 40 and state != "END":
            boomSound.play()
            state = 'END'
            winner = red
            loser = blue
            playerWin(winner)
        
        # Self hit and enemy line hit
        for block in redCarLine[1:]:
            if blueCarPos == block and redCarPos == block:
                boomSound.play()
                winner = red
                loser = red
                state = 'END'
            elif redCarPos == block and state != "END":
                boomSound.play()
                state = 'END'
                winner = blue
                loser = red
                playerWin(winner)
            elif blueCarPos == block and state != "END":
                boomSound.play()
                state = 'END'
                winner = red
                loser = blue
                playerWin(winner)
        for block1 in blueCarLine[1:]:
            if blueCarPos == block1 and redCarPos == block1:
                boomSound.play()
                winner = red
                loser = red
                state = 'END'
            elif blueCarPos == block1 and state != "END":
                boomSound.play()
                state = 'END'
                winner = red
                loser = blue
                playerWin(winner)
            elif redCarPos == block1 and state != "END":
                boomSound.play()
                state = 'END'
                winner = blue
                loser = red
                playerWin(winner)

    elif state == 'END':

        # playSurface.blit(PressSpaceOutlineSurf, PressSpaceOutlineRect)
        # playSurface.blit(PressSpaceSurf, PressSpaceRect)

        for pos in redCarLine:
            pygame.draw.rect(playSurface, red, pygame.Rect(pos[0], pos[1], speed, speed))
        for pos1 in blueCarLine:
            pygame.draw.rect(playSurface, blue, pygame.Rect(pos1[0], pos1[1], speed, speed))

        # Red car correct blit
        if direction == "RIGHT":
            playSurface.blit(redBikeRightImage, (redCarPos[0]-40, redCarPos[1]-55))
        if direction == "UP":
            playSurface.blit(redBikeUpImage, (redCarPos[0]-55, redCarPos[1]-35))
        if direction == "DOWN":
            playSurface.blit(redBikeDownImage, (redCarPos[0]-35, redCarPos[1]-55))
        if direction == "LEFT":
            playSurface.blit(redBikeLeftImage, (redCarPos[0]-55, redCarPos[1]-35))
        
        # Blue car correct blit
        if direction1 == "RIGHT":
            playSurface.blit(blueBikeRightImage, (blueCarPos[0]-40, blueCarPos[1]-55))
        if direction1 == "UP":
            playSurface.blit(blueBikeUpImage, (blueCarPos[0]-55, blueCarPos[1]-35))
        if direction1 == "DOWN":
            playSurface.blit(blueBikeDownImage, (blueCarPos[0]-35, blueCarPos[1]-55))
        if direction1 == "LEFT":
            playSurface.blit(blueBikeLeftImage, (blueCarPos[0]-55, blueCarPos[1]-35))
        
        if loser == winner:
            boom(blue)
            boom(red)

            roundCount(red)
            roundCount(blue)

            playSurface.blit(drawOutlineSurf, drawOutlineRect)
            playSurface.blit(drawSurf, drawRect)

            playSurface.blit(PressSpaceOutlineSurf, PressSpaceOutlineRect)
            playSurface.blit(PressSpaceSurf, PressSpaceRect)
        elif winner == blue:
            boom(loser)

            roundCount(red)
            roundCount(blue)

            if blueBikeScore == 10:
                playSurface.blit(blueOutlineSurf, blueOutlineRect)
                playSurface.blit(blueSurf, blueRect)
            if blueBikeScore < 10:
                roundWin(blue)
            
            playSurface.blit(PressSpaceOutlineSurf, PressSpaceOutlineRect)
            playSurface.blit(PressSpaceSurf, PressSpaceRect)
        else:
            boom(loser)

            roundCount(red)
            roundCount(blue)

            if redBikeScore == 10:
                playSurface.blit(redOutlineSurf, redOutlineRect)
                playSurface.blit(redSurf, redRect)
            if redBikeScore < 10:
                roundWin(red)

            playSurface.blit(PressSpaceOutlineSurf, PressSpaceOutlineRect)
            playSurface.blit(PressSpaceSurf, PressSpaceRect)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    state = 'BEGIN'
                    changeto = ''
                    changeto1 = ''
                    newRound()

    # showScore()
    pygame.display.flip()
    fpsController.tick(60)