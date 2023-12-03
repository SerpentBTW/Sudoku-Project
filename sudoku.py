from sudoku_generator import *
import pygame
import sys
from constants import *
#We need to be able to control what screens are shown
#Game start screen should have 3 buttoms, easy, medium, and hard
#Game in progress screen should have the board and Reset, restart, and exit
#Game won screen should have an exit button
#Game over screen should have restart button


class GameInProgress:
   def __init__(self):
       pass


   def draw_grid(self):
       #Drawing the sudoku board
       for i in range(1, 4):
           pygame.draw.line(
               screen,
               LINE_COLOR,
               (0, i * SQUARE_SIZE),
               (WIDTH, i * SQUARE_SIZE),
               BIG_LINE_WIDTH
           )
           pygame.draw.line(
               screen,
               LINE_COLOR,
               (i * SQUARE_SIZE, 0),
               (i * SQUARE_SIZE, HEIGHT - 100),
               BIG_LINE_WIDTH
           )
       for i in range(1, 9):
           if i % 3 != 0:
               pygame.draw.line(
                   screen,
                   LINE_COLOR,
                   (0, i * CELL_SIZE),
                   (WIDTH, i * CELL_SIZE)
               )
               pygame.draw.line(
                   screen,
                   LINE_COLOR,
                   (i * CELL_SIZE, 0),
                   (i * CELL_SIZE, HEIGHT - 100)
               )


class GameScreen:
   def __init__(self):
       pass


#initializing pygame and controller classes
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
controller = GameInProgress()
pygame.display.set_caption("Sudoku")


screen.fill(BG_COLOR)
controller.draw_grid()


while True:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           pygame.quit()
           sys.exit()
   pygame.display.update()
