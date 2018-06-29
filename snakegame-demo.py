import pygame
import random

###############################################################
# Initialization
screenWidth = 600
screenHeight = 600
interval = 15     # The size of snake and food
rectWidth = interval
rectHeight = interval
pygame.init()
screen = pygame.display.set_mode((screenWidth,screenHeight))
done = False  # essential bool variable

clock = pygame.time.Clock()
applePos = []
'''
# This is a snake of length 7
snakeBlocks = [[interval*6,0,"right"],
               [interval*5,0,"right"],
               [interval*4,0,"right"],
               [interval*3,0,"right"],
               [interval*2,0,"right"],
               [interval,0,"right"],
               [0,0,"right"]]
'''
snakeBlocks = [[interval,0,"right"],[0,0,"right"]]
pivots = [[]]
speed = 5   # The speed of snake

###############################################################
# Randomly generate the position of the food
foodPos = [random.randint(rectWidth,screenWidth-rectWidth),
           random.randint(rectHeight,screenHeight-rectHeight)]
color = (0,128,255)

###############################################################
# Judgement of whether two squares have common part (whether the snake hits itself)
def isOnSquare(a,b):
    if (abs(a[0]-b[0]) < rectWidth) and (abs(a[1]-b[1]) < rectHeight):
        return True
    else:
        return False


###############################################################
# Main loop of game
while not done:
    # Create the quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((0,0,0))

    ###############################################################
    # Direction change of snake
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and snakeBlocks[0][2] != "down":
        snakeBlocks[0][2] = "up"
        pivots.append(snakeBlocks[0].copy())
    elif pressed[pygame.K_DOWN] and snakeBlocks[0][2] != "up":
        snakeBlocks[0][2] = "down"
        pivots.append(snakeBlocks[0].copy())
    elif pressed[pygame.K_LEFT] and snakeBlocks[0][2] != "right":
        snakeBlocks[0][2] = "left"
        pivots.append(snakeBlocks[0].copy())
    elif pressed[pygame.K_RIGHT] and snakeBlocks[0][2] != "left":
        snakeBlocks[0][2] = "right"
        pivots.append(snakeBlocks[0].copy())

    ###############################################################
    # Generate the food
    pygame.draw.rect(screen,(0,200,100),
                     pygame.Rect(foodPos[0],foodPos[1],rectWidth,rectHeight))

    ###############################################################
    # When the snake eat the food
    if isOnSquare(snakeBlocks[0],foodPos):
        foodPos = [random.randint(rectWidth,screenWidth-rectWidth),
                   random.randint(rectHeight,screenHeight-rectHeight)]
        if snakeBlocks[0][2] == "up":
            snakeBlocks.insert(0,
                               [snakeBlocks[0][0],
                                snakeBlocks[0][1]-rectHeight,"up"])
        elif snakeBlocks[0][2] == "right":
            snakeBlocks.insert(0,
                               [snakeBlocks[0][0]+rectWidth,
                                snakeBlocks[0][1],"right"])
        elif snakeBlocks[0][2] == "down":
            snakeBlocks.insert(0,
                               [snakeBlocks[0][0],
                                snakeBlocks[0][1]+rectHeight,"down"])
        elif snakeBlocks[0][2] == "left":
            snakeBlocks.insert(0,
                               [snakeBlocks[0][0]-rectWidth,
                                snakeBlocks[0][1],"left"])
            
    ###############################################################
    # Move the snake, control directions of body movement
    for block in snakeBlocks:
        if block[2] == "up":
            block[1] -= speed
        elif block[2] == "right":
            block[0] += speed
        elif block[2] == "down":
            block[1] += speed
        elif block[2] == "left":
            block[0] -= speed
        for piv in pivots:
            if(block[:2]==piv[:2]):
                block[2] = piv[2]
                if(snakeBlocks.index(block)==(len(snakeBlocks)-1)):
                    pivots.remove(piv)
        pygame.draw.rect(screen,color,
                         pygame.Rect(block[0],block[1],
                                     rectWidth,rectHeight))
                    
        ###############################################################
        # Hit the wall
        if(block[1]<0):
            done = True
            print("Hit the wall! You lose!")
        elif(block[1]>(screenHeight-rectHeight)):
            done = True
            print("Hit the wall! You lose!")
        elif(block[0]<0):
            done = True
            print("Hit the wall! You lose!")
        elif(block[0]>(screenWidth-rectWidth)):
            done = True
            print("Hit the wall! You lose!")
        ###############################################################
        # The snake eats itselt!
        for otherBlock in snakeBlocks:
            if(isOnSquare(block[:2],otherBlock[:2])
               and
               abs(snakeBlocks.index(block)-snakeBlocks.index(otherBlock))>1):
                done = True
                print("You eat yourself! LOSE!")
        ###############################################################
    pygame.display.flip()  # Show the screen
    clock.tick(144)    # Set frequency of refreshing
    

