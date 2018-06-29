import pygame #import the pygame module

screenWidth = 600 #create a variable that stores the window width
screenHeight = 400 #create a variable that stores the window height
rectWidth = 50 #create a variable that stores the rectangle's width
rectHeight = 40 #create a variable that stores the rectangle's height
pygame.init() #start pygame
#set the game window's height and width
screen = pygame.display.set_mode((screenWidth,screenHeight)) 
done = False #create a variable called "done" that stores the boolean value, False
is_blue = True#create a variable called "is_blue" that stores the boolean value, True
x = 30 #create a variable that stores the rectangle's x coordinate
y = 30 #create a variable that stores the rectangle's y coordinate

clock = pygame.time.Clock() #create a variable that stores the pygame clock
#so that we can control the frame rate of the game.

while not done: #if done is false, keep looping
        for event in pygame.event.get(): 
                if event.type == pygame.QUIT: #if the quit button is hit
                        done = True #make the game quit
                #if the event is the space bar pressed down
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_blue = not is_blue #make the color not blue
        
        pressed = pygame.key.get_pressed() 
        #pressed is a dictionary of True and False corresponding to whether a
        #certain key was pressed
        #ex. if we press the Up arrow, pressed[pygame.K_UP] = True

        if pressed[pygame.K_UP]: #if we pressed the up key
                y -= 3 
                #decrease the y position so that we can move the rectangle up
        if pressed[pygame.K_DOWN]: 
                y += 3
        if pressed[pygame.K_LEFT]: 
                x -= 3
        if pressed[pygame.K_RIGHT]: 
                x += 3

        
        screen.fill((0, 0, 0)) #refresh the screen and get rid of the old frame.
        if is_blue: #if the variable is_blue is true
                color = (0, 128, 255) #change the color to whatever this is
        else: #if the variable is_blue is false, change the color to whatever THAT is 
                color = (255, 100, 0)

        #draw a rectangle on the screen at position x,y with color color
        pygame.draw.rect(screen, color, pygame.Rect(x, y, rectWidth, rectHeight))
        pygame.display.flip() #display the screen
        clock.tick(60) #controls the frame rate of the game (how many times the screen changes per second)
