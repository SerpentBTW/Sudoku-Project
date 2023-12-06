import pygame

class Cell:
    def __init__(self, value, row, col, screen):
        # Initialize basic attributes
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.selected = False
        self.sketched_value = 0

    def set_value(self, value):
        # Set the value of the cell
        self.value = value

    def set_sketched_value(self, value):
        # Set the sketched value of the cell
        self.sketched_value = value

    def toggle_selected(self):
        # Toggle the selected status of the cell
        self.selected = not self.selected

    def draw(self):
        # Define cell size and margin
        cell_size = 50
        margin = 5

        # Calculate the position of the cell on the screen
        x, y = self.col * (cell_size + margin), self.row * (cell_size + margin)

        # Draw a white rectangle to represent the cell
        pygame.draw.rect(self.screen, (255, 255, 255), (x, y, cell_size, cell_size))

        # If the cell is selected, draw a red outline
        if self.selected:
            pygame.draw.rect(self.screen, (255, 0, 0), (x, y, cell_size, cell_size), 3)

        # Use Pygame font to draw the value inside the cell
        font = pygame.font.Font(None, 36)

        # Determine which value to draw and its color
        draw_value = self.value if self.value != 0 else self.sketched_value
        color = (0, 0, 0) if self.value != 0 else (128, 128, 128)

        # If there is a value to draw, render and display it
        if draw_value != 0:
            text = font.render(str(draw_value), True, color)
            text_rect = text.get_rect(center=(x + cell_size // 2, y + cell_size // 2))
            self.screen.blit(text, text_rect)

