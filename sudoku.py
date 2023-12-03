from sudoku_generator import *
import pygame
import sys
from constants import *




# We need to be able to control what screens are shown
# Game start screen should have 3 buttoms, easy, medium, and hard
# Game in progress screen should have the board and Reset, restart, and exit
# Game won screen should have an exit button
# Game over screen should have restart button


class GameController:
   def __init__(self):
       pass


   #Game functionality
   def handle_button_click(self, click):
       if click == 'easy':
           pass
       elif click == 'medium':
           pass
       elif click == 'hard':
           pass
       elif click == 'reset':
           pass
       elif click == 'restart':
           pass
       elif click == 'exit':
           pass


   #Draw functions
   def draw_button(self, x_coordinate, y_coordinate):
       pass


   def draw_title(self, title, font):
       title_surface = font.render(title, 0, LINE_COLOR)
       title_rectangle = title_surface.get_rect(center=(WIDTH // 2, WIDTH // 4))
       screen.blit(title_surface, title_rectangle)


   def draw_numbers(self):
       number_surface = number_font.render('1', 0, LINE_COLOR)
       number_rectangle = number_surface.get_rect(center=(WIDTH / 2, WIDTH / 2))
       screen.blit(number_surface, number_rectangle)


   def draw_grid(self):
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




class GameScreens:
   controller = GameController()


   def __init__(self):
       pass


   def game_in_progress(self):
       self.controller.draw_grid()
       self.controller.draw_numbers()


   # Game start screen
   def game_start(self):
       screen.fill(BG_COLOR)
       self.controller.draw_title("Welcome to Sudoku", title_font)
       title_surface = title_2_font.render("Select Game Mode:", 0, LINE_COLOR)
       title_rectangle = title_surface.get_rect(center=(WIDTH // 2, WIDTH // 2))
       screen.blit(title_surface, title_rectangle)


   # Game Won!
   def game_won(self):
       screen.fill(BG_COLOR)
       self.controller.draw_title("Game Won!", title_font)


   # Game Over!
   def game_over(self):
       screen.fill(BG_COLOR)
       self.controller.draw_title("Game Over :(", title_font)




# initializing pygame, controller class, and the board
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
game_screen = GameScreens()
pygame.display.set_caption("Sudoku")


# Fonts
number_font = pygame.font.Font(None, NUMBER_FONT)
title_font = pygame.font.Font(None, TITLE_FONT)
title_2_font = pygame.font.Font(None, TITLE_2_FONT)




def main():
   # Start the game
   game_screen.game_start()


   while True:
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()
       pygame.display.update()




if __name__ == "__main__":
   main()