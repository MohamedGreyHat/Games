import pygame, sys
from pygame.locals import *
from Objects import Snake, Food
import random, time, copy



#assert hasattr(Objects, 'Food')

    

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARKGREEN = (0, 155, 0)
BACKGROUDNCOLOR = GREEN
SNAKECOLOR = (0, 0, 255)

WIDTH = 1020
HIGHT = 600

x0, y0 = 40, 40
hsize = 20 # head size
board = []
board_size = (WIDTH , HIGHT - y0)
# xf := width of the game_play board
# yf := height of the game_play board
xf, yf = board_size[0], board_size[1] 
assert xf % hsize == 0
assert yf % hsize == 0

x = random.randrange(x0, xf - hsize, hsize)
y = random.randrange(y0, yf - hsize, hsize)
z = [pygame.Rect(x, y, hsize, hsize),pygame.Rect(x-hsize, y, hsize, hsize)] 
snake = Snake(GREEN, z)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HIGHT))
screen.fill(WHITE)
pygame.display.set_caption("Snake Amzing")
#pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, HIGHT)) 
pygame.draw.line(screen, BLACK, (0, yf),(xf, yf), 2)
for i in range(0, board_size[0], hsize):
    for j in range(0, board_size[1], hsize):
        pygame.draw.rect(screen, GREEN, (i,j , hsize, hsize))

direction = {'previous': "", 'actuel':""}
SCORE = 0

def draw_init_snake():
    for e in snake.body :
        pygame.draw.rect(screen, SNAKECOLOR, (e.left, e.top, hsize, hsize))
        #pygame.draw.rect(screen, DARKGREEN, (e.left, e.top, hsize, hsize), )

def draw_food():
    global food 
    x = random.randrange(x0, xf - hsize, hsize)
    y = random.randrange(y0, yf - hsize, hsize)
    food = Food([x, y])
    pygame.draw.rect(screen, RED, (food.x, food.y, hsize, hsize))
    



def draw_snake():
    for i in range(len(tmp_snake.body)) :
        pygame.draw.rect(screen, BACKGROUDNCOLOR, (tmp_snake.body[i][0], tmp_snake.body[i][1], hsize, hsize)) # draw white rectangle in old position
        pygame.draw.rect(screen, SNAKECOLOR, (snake.body[i][0], snake.body[i][1], hsize, hsize))
        pygame.draw.rect(screen, SNAKECOLOR, (snake.body[i][0], snake.body[i][1], hsize, hsize))

def check_win():
    global SCORE
    if snake.body[0].collidepoint(food.x, food.y) :
        pygame.draw.rect(screen, BACKGROUDNCOLOR, (food.x, food.y, hsize, hsize)) # delete the food
        snake.body.append(pygame.Rect(snake.body[-1][0]-hsize, y, hsize, hsize)) # add rectangle at the end
        print "> ", len(snake.body)
        SCORE += 1
        blit_score()
        draw_food()

def check_collision():
    if snake.body[1].left < 0 or snake.body[1].top < 0 or snake.body[1].left > xf or snake.body[1].top > yf  :
        print "Loosed"
    else :
        for i in range(len(snake.body)) : 
            for j in range(1, len(snake.body)):
                if i != j and snake.body[i].collidepoint(snake.body[j].left, snake.body[j].top):
                    print "collide it self"
                


def move_snake():
    global tmp_snake
    tmp_snake = copy.deepcopy(snake)

    if direction == "up" :
        snake.body[0].top -= hsize # changer la tete en 1er lieux
        for i in range(len(snake.body)-1, 0,-1):
            snake.body[i] = tmp_snake.body[i-1]
    elif direction == "down" :
        snake.body[0].top += hsize
        for i in range(len(snake.body)-1, 0,-1):
            snake.body[i] = tmp_snake.body[i-1]
    elif direction == "left" :
        snake.body[0].left -= hsize
        for i in range(len(snake.body)-1, 0,-1):
            snake.body[i] = tmp_snake.body[i-1]
    if direction == "right" :
        snake.body[0].left += hsize
        for i in range(len(snake.body)-1, 0,-1):
            snake.body[i] = tmp_snake.body[i-1]

    draw_snake()
    check_win()
    check_collision()

def blit_score():
    global score_font
    score_font  = pygame.font.Font('freesansbold.ttf', 15)
    score_surf = score_font.render('SCORE : '+str(SCORE), True, BLACK)
    score_rect = score_surf.get_rect()
    score_rect.midtop = (50, yf+10)
    pygame.draw.rect(screen, WHITE, score_rect)
    screen.blit(score_surf, score_rect)
    
def blit_quit():
    global quit_rect
    quit_surf = score_font.render('QUIT', True, BLACK)
    quit_rect = quit_surf.get_rect()
    quit_rect.midtop = (xf-40, yf+10)
    pygame.draw.rect(screen, WHITE, quit_rect)
    screen.blit(quit_surf, quit_rect)

def blit_restart() :
    global rest_rect
    rest_surf = score_font.render('RESTART', True, BLACK)
    rest_rect = rest_surf.get_rect()
    rest_rect.midtop = (xf-40, yf+10)
    pygame.draw.rect(screen, WHITE, rest_rect)
    screen.blit(rest_surf, rest_rect)

def blit_pause(_pause_play_msg = "|>PAUSE ") :
    global pause_rect, pause_play_msg
    pause_play_msg = _pause_play_msg
    pause_surf = score_font.render(pause_play_msg, True, BLACK)
    pause_rect = pause_surf.get_rect()
    pause_rect.midtop = (quit_rect.left-40, yf+10)
    screen.blit(pause_surf, pause_rect)
    


draw_init_snake()
draw_food()
       
blit_score()
blit_quit()
blit_pause()

FPS = 10
clock = pygame.time.Clock() 
while True :
    move_snake()
    for event in pygame.event.get():
        if event.type == QUIT :
            pygame.quit()
            sys.exit()
        elif event.type == KEYUP:
            if event.key == K_UP :
                direction = "up"   
            elif event.key == K_DOWN :
                direction = "down"
                
            elif event.key == K_LEFT :
                direction = "left"
                
            elif event.key == K_RIGHT :
                direction = "right"
        elif event.type == MOUSEBUTTONUP:
            x, y = event.pos
            if quit_rect.collidepoint(x, y):
                sys.exit()
            elif pause_rect.collidepoint(x, y):
                pygame.draw.rect(screen, WHITE, pause_rect)
                blit_pause("")
                if pause_play_msg == "":
                    blit_pause("PLAY")
                elif pause_play_msg == "PLAY" :
                    print "in"
                    blit_pause("")
                    blit_pause("PAUSE")
                    
                

                              
    pygame.display.update()
    clock.tick(FPS)

