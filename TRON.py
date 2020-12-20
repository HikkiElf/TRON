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
globalFont = pygame.font.SysFont('monaco', 300)
globalOutlineFont = pygame.font.SysFont('monaco', 303)

# Text Press space
PressSpaceOutlineSurf = globalOutlineFont.render("Press space", True, black)
PressSpaceSurf = globalFont.render("Press space", True, white)
PressSpaceOutlineRect = PressSpaceOutlineSurf.get_rect()
PressSpaceRect = PressSpaceSurf.get_rect()
PressSpaceOutlineRect.midtop = (640, 260)
PressSpaceRect.midtop = (640, 260)

# Text red wins
blueOutlineSurf = globalOutlineFont.render("Blue Wins", True, black)
blueSurf = globalFont.render("Blue Wins", True, blue)
blueOutlineRect = blueOutlineSurf.get_rect()
blueRect = blueSurf.get_rect()
blueOutlineRect.midtop = (640, 260)
blueRect.midtop = (640, 260)

# Text blue wins
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

# Red bike image
redBikeLeftImage = pygame.image.load("images/bikeRed.png")
redBikeUpImage = pygame.transform.rotate(redBikeLeftImage, -90)
redBikeDownImage = pygame.transform.rotate(redBikeLeftImage, 90)
redBikeRightImage = pygame.transform.rotate(redBikeLeftImage, 180)

# Blue bike image
blueBikeLeftImage = pygame.image.load("images/bikeBlue.png")
blueBikeUpImage = pygame.transform.rotate(blueBikeLeftImage, -90)
blueBikeDownImage = pygame.transform.rotate(blueBikeLeftImage, 90)
blueBikeRightImage = pygame.transform.rotate(blueBikeLeftImage, 180)

def roundCount(color: pygame.Color):
    global redBikeScore, blueBikeScore

    pygame.draw.circle(playSurface, white, [320, 20], 10, 1)
    pygame.draw.circle(playSurface, white, [342, 20], 10, 1)
    pygame.draw.circle(playSurface, white, [364, 20], 10, 1)

    pygame.draw.circle(playSurface, white, [920, 20], 10, 1)
    pygame.draw.circle(playSurface, white, [942, 20], 10, 1)
    pygame.draw.circle(playSurface, white, [964, 20], 10, 1)

    if color == red:
        if redBikeScore >= 1:
            pygame.draw.circle(playSurface, red, [320, 20], 9, 0)
        if redBikeScore >= 2:
            pygame.draw.circle(playSurface, red, [320, 20], 9, 0)
            pygame.draw.circle(playSurface, red, [342, 20], 9, 0)
        if redBikeScore >= 3:
            pygame.draw.circle(playSurface, red, [320, 20], 9, 0)
            pygame.draw.circle(playSurface, red, [342, 20], 9, 0)
            pygame.draw.circle(playSurface, red, [364, 20], 9, 0)

    if color == blue:
        if blueBikeScore >= 1:
            pygame.draw.circle(playSurface, blue, [964, 20], 9, 0)
        if blueBikeScore >= 2:
            pygame.draw.circle(playSurface, blue, [964, 20], 9, 0)
            pygame.draw.circle(playSurface, blue, [942, 20], 9, 0)
        if blueBikeScore >= 3:
            pygame.draw.circle(playSurface, blue, [964, 20], 9, 0)
            pygame.draw.circle(playSurface, blue, [942, 20], 9, 0)
            pygame.draw.circle(playSurface, blue, [920, 20], 9, 0)


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
    if animCount + 1 >= 20:
        animCount = 0
    if color == red:
        playSurface.blit(bang[animCount // 5], (redCarPos[0]-100, redCarPos[1]-100))
        animCount += 1
    else:
        playSurface.blit(bang[animCount // 5], (blueCarPos[0]-100, blueCarPos[1]-100))
        animCount += 1

# Show Score Red and Blue Bike
def showScore():
    SFont = pygame.font.SysFont('monaco', 32)
    SBsurf = SFont.render("BLUE PLAYER SCORE  :  {0}".format(blueBikeScore), True, white)
    SRsurf = SFont.render("RED PLAYER SCORE  :  {0}".format(redBikeScore), True, white)
    SBrect = SBsurf.get_rect()
    SRrect = SRsurf.get_rect()
    SBrect.midtop = (1120, 10)
    SRrect.midtop = (145, 10)
    playSurface.blit(SBsurf, SBrect)
    playSurface.blit(SRsurf, SRrect)

def tie():
    myFont = pygame.font.SysFont('monaco', 300)
    Tsurf = myFont.render("DRAW", True, white)
    Trect = Tsurf.get_rect()
    Trect.midtop = (640, 260)
    playSurface.blit(Tsurf, Trect)
    pygame.display.flip() 

def newGame():
    global redCarPos, blueCarPos
    redCarPos = [100, 360]
    blueCarPos = [1180, 360]
    del redCarLine[:]
    del blueCarLine[:]

while running:
    playSurface.blit(background, (0, 0))
    pygame.draw.circle(playSurface, white, [320, 20], 10, 1)
    pygame.draw.circle(playSurface, white, [342, 20], 10, 1)
    pygame.draw.circle(playSurface, white, [364, 20], 10, 1)

    if state == "BEGIN":

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

        # Bounds
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
            if blueCarPos == block and redCarPos == block1:
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

        # Draw
        if (redCarPos[0] == blueCarPos[0] and redCarPos[1] == blueCarPos[1]) or ((redCarPos[1] >= height or redCarPos[1] <= 40) and (blueCarPos[1] >= height or blueCarPos[1] <= 40)) or  ((redCarPos[0] >= width or redCarPos[0] < 0) and (blueCarPos[0] >= width or blueCarPos[0] < 0)) or ((redCarPos == block) and (blueCarPos == block)) or ((blueCarPos == block1) and (redCarPos == block1)):
            boomSound.play()
            winner = red
            loser = red
            state = 'END'

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
        elif winner == blue:
            boom(loser)

            roundCount(red)
            roundCount(blue)

            playSurface.blit(blueOutlineSurf, blueOutlineRect)
            playSurface.blit(blueSurf, blueRect)
        else:
            boom(loser)

            roundCount(red)
            roundCount(blue)

            playSurface.blit(redOutlineSurf, redOutlineRect)
            playSurface.blit(redSurf, redRect)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    state = 'BEGIN'
                    changeto = ''
                    changeto1 = ''
                    newGame()

    showScore()
    pygame.display.flip()
    fpsController.tick(60)
