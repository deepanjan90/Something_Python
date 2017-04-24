                                            #########################################
                                            ##Courtsey http://programarcadegames.com#
                                            #########################################



import pygame
import sys
from pygame.locals import *


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ASH = (178, 190, 181)
RED = (255, 0, 0)
BLUE = (135,206,250)
 
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 35.6
HEIGHT = 35.6
 
# This sets the margin between each cell
MARGIN = 5

def start(): 
        
    # Initialize pygame
    pygame.init()
     
    # Set the HEIGHT and WIDTH of the screen
    WINDOW_SIZE = [612, 612]
    screen = pygame.display.set_mode(WINDOW_SIZE)
    im = pygame.Surface(screen.get_size()) 
    # Set title of screen
    pygame.display.set_caption("QLearning")
     
    # Loop until the user clicks the close button.
    done = False
     
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    font = pygame.font.SysFont('Arial', 10)

def DrawGrid(grid): 
    
    # Set the HEIGHT and WIDTH of the screen
    WINDOW_SIZE = [612, 612]
    screen = pygame.display.set_mode(WINDOW_SIZE)
    clock = pygame.time.Clock()
    # Draw the grid
    for row in range(15):
        for column in range(15):
            color = WHITE
            if grid[row][column] == 1:
                color = BLUE
            if grid[row][column] == 2:
                color = ASH
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
            
    
    # Limit to 60 frames per second
    clock.tick(60)
    
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
