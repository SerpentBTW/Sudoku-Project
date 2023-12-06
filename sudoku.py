from sudoku_generator import *
import pygame
import sys
from constants import *


class GameController:
    def __init__(self):
        pass

    # Draw/create functions

    def create_board(self, difficulty):
        sudoku = SudokuGenerator(difficulty, 9)
        sudoku.fill_values()
        end = copy.deepcopy(sudoku.get_board())
        sudoku.remove_cells()
        begin = copy.deepcopy(sudoku.get_board())
        return sudoku, end, begin

    def draw_button(self, x, y, button_text):
        btn_text = button_font.render(button_text, 0, (0, 0, 0))
        button_surface = pygame.Surface((btn_text.get_size()[0] + 20, btn_text.get_size()[1] + 20))
        button_surface.fill(BUTTON_COLOR)
        button_surface.blit(btn_text, (10, 10))

        button_rectangle = button_surface.get_rect(
            center=(x, y)
        )

        screen.blit(button_surface, button_rectangle)

    def draw_title(self, title, font):
        title_surface = font.render(title, 0, LINE_COLOR)
        title_rectangle = title_surface.get_rect(center=(WIDTH // 2, WIDTH // 4))
        screen.blit(title_surface, title_rectangle)

    def draw_numbers(self, board):
        # Go through each number in the board, and add it if isn't 0
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if board[row][col] != 0:
                    number_surface = number_font.render(str(board[row][col]), 0, LINE_COLOR)
                    number_rectangle = number_surface.get_rect(
                        center=(col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2))
                    screen.blit(number_surface, number_rectangle)

    def establish_numbers(self, board):
        numbers_can_not_change = []
        numbers_can_change = []
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if board[row][col] != 0:
                    numbers_can_not_change.append((row, col))
                else:
                    numbers_can_change.append((row, col))
        return numbers_can_not_change, numbers_can_change

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

    # Change the parameter for removed_cells to match the button's choice
    def game_in_progress(self, difficulty):
        # Every time this function is called, a new board should be made
        board, end, begin = self.controller.create_board(difficulty)
        screen.fill(BG_COLOR)
        self.controller.draw_grid()
        self.controller.draw_numbers(board.board)
        can_not_change, can_change = self.controller.establish_numbers(board.board)
        self.controller.draw_button(100, 725, "Reset")
        self.controller.draw_button(335, 725, "Restart")
        self.controller.draw_button(575, 725, "Exit")
        return board, end, begin, can_not_change, can_change

    # Game start screen
    def game_start(self):
        screen.fill(BG_COLOR)
        self.controller.draw_title("Welcome to Sudoku", title_font)
        title_surface = title_2_font.render("Select Game Mode:", 0, LINE_COLOR)
        title_rectangle = title_surface.get_rect(center=(WIDTH // 2, WIDTH // 2))
        screen.blit(title_surface, title_rectangle)
        self.controller.draw_button(100, 500, "Easy")
        self.controller.draw_button(335, 500, "Medium")
        self.controller.draw_button(570, 500, "Hard")

    # Game Won!
    def game_won(self):
        screen.fill(BG_COLOR)
        self.controller.draw_title("Game Won!", title_font)
        self.controller.draw_button(335, 350, "  Exit  ")

    # Game Over!
    def game_over(self):
        screen.fill(BG_COLOR)
        self.controller.draw_title("Game Over :(", title_font)
        self.controller.draw_button(335, 350, "Restart")


# initializing pygame, controller class, and screens
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
game_screen = GameScreens()
pygame.display.set_caption("Sudoku")

# Fonts
number_font = pygame.font.Font(None, NUMBER_FONT)
title_font = pygame.font.Font(None, TITLE_FONT)
title_2_font = pygame.font.Font(None, TITLE_2_FONT)
button_font = pygame.font.Font(None, BUTTON_FONT)


# Main Function
def main():
    # Start the game
    game_screen.game_start()
    current_screen = "start"
    numInput = 0
    selected = False
    # Main Loop for different actions
    while True:
        for event in pygame.event.get():
            # Listening for user events
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Gets location of mouse button and which cell is being clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not selected:
                    x, y = event.pos
                    row = y // SQUARE_SIZE
                    col = x // SQUARE_SIZE
                    row_cell = y // CELL_SIZE
                    col_cell = x // CELL_SIZE
                    print(row_cell, col_cell, row, col)
                if current_screen == "in progress":
                    if row == 0 or row == 1 or row == 2:
                        if not selected:
                            pygame.draw.rect(screen, (255, 0, 0), (col_cell * 75, row_cell * 75, CELL_SIZE, CELL_SIZE), 3)
                            selected = True
                        elif selected:
                            continue
                # Use different coordinates depending on the screen shown
                if current_screen == 'start':
                    if row == 2:
                        # Set difficulty and change the screen accordingly
                        if col == 0:
                            difficulty = EASY
                        elif col == 1:
                            difficulty = MEDIUM
                        elif col == 2:
                            difficulty = HARD
                        board, end, begin, can_not_change, can_change = game_screen.game_in_progress(difficulty)
                        current_screen = 'in progress'

                if current_screen == 'in progress':
                    if row == 3:
                        if col == 0:
                            # When use clicks "Reset" Button, it will redraw the board with the beginning tiles
                            board.board = copy.deepcopy(begin)
                            screen.fill(BG_COLOR)
                            game_screen.controller.draw_grid()
                            game_screen.controller.draw_numbers(begin)
                            game_screen.controller.draw_button(100, 725, "Reset")
                            game_screen.controller.draw_button(335, 725, "Restart")
                            game_screen.controller.draw_button(575, 725, "Exit")
                            selected = False
                            continue
                        # "Restart" Function will bring user back to main menu
                        elif col == 1:
                            selected = False
                            game_screen.game_start()
                            current_screen = 'start'
                        # Quits Game
                        elif col == 2:
                            pygame.quit()
                            sys.exit()
                # Buttons for the game over screen
                if current_screen == 'game over':
                    if row == 1 and col == 1:
                        game_screen.game_start()
                        current_screen = 'start'
                if current_screen == 'game won':
                    if row == 0 and col == 0:
                        pygame.quit()
                        sys.exit()
            # Detects a KeyDown action and get a number based on which key is pressed
            if event.type == pygame.KEYDOWN:
                if current_screen == 'in progress':
                    if numInput == 0:
                        match event.key:
                            case (pygame.K_1):
                                numInput = 1
                            case (pygame.K_2):
                                numInput = 2
                            case (pygame.K_3):
                                numInput = 3
                            case (pygame.K_4):
                                numInput = 4
                            case (pygame.K_5):
                                numInput = 5
                            case (pygame.K_6):
                                numInput = 6
                            case (pygame.K_7):
                                numInput = 7
                            case (pygame.K_8):
                                numInput = 8
                            case (pygame.K_9):
                                numInput = 9
                            case (pygame.K_0):
                                continue
                    # Detects when Backspace or return button is pressed
                    match event.key:
                        case (pygame.K_BACKSPACE):
                            # If the number was at the beginning it will go back to the beginning
                            if board.board[row_cell][col_cell] == begin[row_cell][col_cell]:
                                continue
                            # Else the backspace will delete the user's input at said row,col and  will redraw
                            # accordingly
                            if selected:
                                board.board[row_cell][col_cell] = 0
                                screen.fill(BG_COLOR)
                                game_screen.controller.draw_grid()
                                game_screen.controller.draw_numbers(board.board)
                                game_screen.controller.draw_button(100, 725, "Reset")
                                game_screen.controller.draw_button(335, 725, "Restart")
                                game_screen.controller.draw_button(575, 725, "Exit")
                                numInput = 0
                                selected = False
                                continue
                        case (pygame.K_RETURN):
                            # If the cell is editable and the current board doesn't have a number in there already
                            if begin[row_cell][col_cell] == 0 and board.board[row_cell][col_cell] == 0:
                                # The board will confirm the input
                                board.board[row_cell][col_cell] = numInput
                                numInput = 0
                                screen.fill(BG_COLOR)
                                game_screen.controller.draw_grid()
                                game_screen.controller.draw_numbers(board.board)
                                game_screen.controller.draw_button(100, 725, "Reset")
                                game_screen.controller.draw_button(335, 725, "Restart")
                                game_screen.controller.draw_button(575, 725, "Exit")
                                selected = False

                                # Check if there are empty spaces
                                finished = True
                                for i in board.board:
                                    if 0 in i:
                                        finished = False
                                        break
                                # if no empty spaces, then check if everything matches to the solution
                                if finished:
                                    for i in range(9):
                                        # If there is a discrepancy, then it will show you lose
                                        for j in range(9):
                                            if end[i][j] != board.board[i][j]:
                                                game_screen.game_over()
                                                current_screen = "game over"
                                                continue
                                    # if no discrepancy then you win
                                    if current_screen != "game over":
                                        game_screen.game_won()
                                        current_screen = 'game won'

                                continue
                    # If the starting board at said row,cell was given or the current board has a number in place
                    if begin[row_cell][col_cell] != 0 or board.board[row_cell][col_cell] != 0:
                        continue
                    # Otherwise print the new number at said location
                    number_surface = number_font.render(str(numInput), 0, LINE_COLOR)
                    number_rectangle = number_surface.get_rect(
                        center=(col_cell * CELL_SIZE + CELL_SIZE // 2, row_cell * CELL_SIZE + CELL_SIZE // 2))
                    screen.blit(number_surface, number_rectangle)
        pygame.display.update()


if __name__ == "__main__":
    main()
