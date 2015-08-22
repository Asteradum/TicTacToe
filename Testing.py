__author__ = 'almartinorive'

# Import a library of functions called 'pygame'
import pygame
import math
# Initialize the game engine
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
#WHITE = (0xFF, 0xFF, 0xFF)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Size and name
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Professor Craven's Cool Game")

# Loop until the user clicks the close button.
done = False
click = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
# Used for painting the cells
WIDTH = size[0]/3
HEIGHT = size[1]/3
CELLS_DIMENSIONS = [ [[0,0,WIDTH,HEIGHT],           [size[0]/3,0,WIDTH,HEIGHT],         [size[0]*2/3,0,WIDTH,HEIGHT]],
                     [[0,size[1]/3,WIDTH,HEIGHT],   [size[0]/3,size[1]/3,WIDTH,HEIGHT], [size[0]*2/3,size[1]/3,WIDTH,HEIGHT]],
                     [[0,size[1]*2/3,WIDTH,HEIGHT], [size[0]/3,size[1]*2/3,WIDTH,HEIGHT], [size[0]*2/3,size[1]*2/3,WIDTH,HEIGHT]], ]
COMBINATIONS = [[[0,0],[0,1],[0,2]],
                [[1,0],[1,1],[1,2]],
                [[2,0],[2,1],[2,2]],
                [[0,0],[1,0],[2,0]],
                [[0,1],[1,1],[2,1]],
                [[0,2],[1,2],[2,2]],
                [[0,0],[1,1],[2,2]],
                [[0,2],[1,1],[2,0]]]

cells = [[0,0,0],
         [0,0,0],
         [0,0,0]]

pos = (0,0)

draw = False
player1 = True

# -------- Main Program Loop -----------
while not done and draw == False:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click = True
            pos = pygame.mouse.get_pos()
    # --- Game logic should go here
    # Assigning cells
    if click:
        for i in range(3):
            for j in range(3):
                if pygame.Rect(CELLS_DIMENSIONS[i][j]).collidepoint(pos) and cells[i][j] == 0:
                    if player1:
                        cells[i][j] = 'X'
                        player1 = not player1
                    else:
                        cells[i][j] = 'O'
                        player1 = not player1
                    break
        click = False

    # Checking for winner
    for i in range(len(COMBINATIONS)):
        if ((cells[COMBINATIONS[i][0][0]][COMBINATIONS[i][0][1]] == 'X'
            and cells[COMBINATIONS[i][1][0]][COMBINATIONS[i][1][1]] == 'X'
            and cells[COMBINATIONS[i][2][0]][COMBINATIONS[i][2][1]] == 'X')
            or (cells[COMBINATIONS[i][0][0]][COMBINATIONS[i][0][1]] == 'O'
            and cells[COMBINATIONS[i][1][0]][COMBINATIONS[i][1][1]] == 'O'
            and cells[COMBINATIONS[i][2][0]][COMBINATIONS[i][2][1]] == 'O')):
            done = True

    # Checking for draw
    draw = True
    for i in range(3):
        for j in range(3):
            if cells[i][j] == 0:
                draw = False
    if not draw:
        print('Draw')

    # --- Drawing code should go here
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
    for i in range(3):
        for j in range(3):
            if cells[i][j] == 'X':
                pygame.draw.line(screen,
                                 GREEN,
                                 (CELLS_DIMENSIONS[i][j][0] + 25,CELLS_DIMENSIONS[i][j][1] + 25), #Start Point
                                 (CELLS_DIMENSIONS[i][j][0] + CELLS_DIMENSIONS[i][j][2] - 25,CELLS_DIMENSIONS[i][j][1] + CELLS_DIMENSIONS[i][j][3] - 25), #End Point
                                 3)
                pygame.draw.line(screen,
                                 GREEN,
                                 (CELLS_DIMENSIONS[i][j][0] + CELLS_DIMENSIONS[i][j][2] - 25, CELLS_DIMENSIONS[i][j][1] + 25),
                                 (CELLS_DIMENSIONS[i][j][0] + 25,CELLS_DIMENSIONS[i][j][1] + CELLS_DIMENSIONS[i][j][3] - 25 ),
                                 3)
            elif cells[i][j] == 'O':
                pygame.draw.ellipse(screen, RED,CELLS_DIMENSIONS[i][j], 3)
    # Paint cells
    pygame.draw.rect(screen, BLACK, CELLS_DIMENSIONS[0][0], 2)
    pygame.draw.rect(screen, BLACK, CELLS_DIMENSIONS[0][1], 2)
    pygame.draw.rect(screen, BLACK, CELLS_DIMENSIONS[0][2], 2)
    pygame.draw.rect(screen, BLACK, CELLS_DIMENSIONS[1][0], 2)
    pygame.draw.rect(screen, BLACK, CELLS_DIMENSIONS[1][1], 2)
    pygame.draw.rect(screen, BLACK, CELLS_DIMENSIONS[1][2], 2)
    pygame.draw.rect(screen, BLACK, CELLS_DIMENSIONS[2][0], 2)
    pygame.draw.rect(screen, BLACK, CELLS_DIMENSIONS[2][1], 2)
    pygame.draw.rect(screen, BLACK, CELLS_DIMENSIONS[2][2], 2)

    # If winner paint
    if done and not draw:
        player1 = not player1
        font = pygame.font.SysFont('Calibri', 25, True, False)
        if player1:
            text = font.render("Player 1 Wins",True,BLACK)
        else:
            text = font.render("Player 2 Wins",True,BLACK)
        screen.blit(text, [250, 250])
    if draw:
         font = pygame.font.SysFont('Calibri', 25, True, False)
         text = font.render("Draw",True,BLACK)
         screen.blit(text, [250, 250])
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    click = False
    # --- Limit to 60 frames per second
    clock.tick(60)

click = False
while not click:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.quit()
            click = True