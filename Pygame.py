import pygame, sys
pygame.init()
clock = pygame.time.Clock()
red = (255, 0, 0)
white = (255, 255, 255)
blue = (0, 255, 255)
vel = 5
X = 20
Y = 20
U = 100
H = 100
WIDTH = 1800
HEIGHT = 1000

win = pygame.display.set_mode((WIDTH, HEIGHT))
Grape = 1

#def block(x, y,width, height):
#    pygame.draw.rect(win, red, pygame.Rect(x,y,width, height
def enemy_one(x,y,color):

    pygame.draw.rect(win,color, pygame.Rect(x,y,30,30))
    
def game_loop_white_square():
    global Grape
    global X
    global Y
    while Grape < 2:
        pygame.time.delay(5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  #this is what allows the window to stay open
                Grape += 4

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and X >= 1:
            X -= vel
        if keys[pygame.K_RIGHT] and X < WIDTH - 30:
            X += vel
        if keys[pygame.K_UP] and Y > 1:
            Y -= vel

        if keys[pygame.K_DOWN] and Y < HEIGHT - 30:

            Y += vel




        win.fill((0,0,0))

    #    block(50,70,40,40)

        enemy_one(100,100,blue)


        pygame.draw.rect(win, white, pygame.Rect(X, Y, 30, 30))


        pygame.display.update()
game_loop_white_square()


pygame.quit()
quit()
