import pygame
import random
import math
pygame.init()#initializes Pygame
pygame.display.set_caption("Mouse events")#sets the window title
screen = pygame.display.set_mode((800, 800))#creates game screen
clock = pygame.time.Clock()

def collision(x1, y1, x2, y2):
    if math.sqrt((y1-y2)**2 + (x1-x2)**2)<20+20:
        print("collision!")
        return True
    else:
        return False

#initial ball1 position
ball1x=random.randrange(100, 700)
ball1y=random.randrange(100, 700)
#initial ball1 velocity
Vx1 = random.randrange(3, 10)
Vy1 = random.randrange(3, 10)


#initial ball2 position
ball2x=random.randrange(100, 700)
ball2y=random.randrange(100, 700)
#initial ball1 velocity
Vx2 = random.randrange(3, 10)
Vy2 = random.randrange(3, 10)


while True:
    
    #event queue and timer
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #close game window
            pygame.quit()
            quit()
    
    #check for collision!
    if collision(ball1x, ball1y, ball2x, ball2y) == True:
        #THIS IS NOT REAL PHYSICS!
        #We'll hopefully modify this later to get it to be more realistic
        Vx1*=-1
        Vy1*=-1
        Vx2*=-1
        Vy2*=-1
        print("boing!")
        
    
    #reflect off walls
    if ball1y+30>800 or ball1y-30<0:
        Vy1*=-1
    if ball1x+30>800 or ball1x-30<0:
        Vx1*=-1
        
    if ball2y+30>800 or ball2y-30<0:
        Vy2*=-1
    if ball2x+30>800 or ball2x-30<0:
        Vx2*=-1
    
    #apply gravity
    #if bally+20<800:
    #    Vy+=.1
    ball1y+=Vy1
    ball1x+=Vx1
    
    ball2y+=Vy2
    ball2x+=Vx2
    
    #apply friction
    #Vx*=.99
    #Vy*=.99
    
    #render section
    screen.fill((0,0,0))
    pygame.draw.circle(screen, (255, 255, 255), (ball1x, ball1y), 20)
    pygame.draw.circle(screen, (255, 255, 255), (ball2x, ball2y), 20)
    pygame.display.flip()
    #end game loop##############################################

pygame.quit()

