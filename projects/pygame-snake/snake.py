import pygame

from constants import GREEN, DARK_GREEN, CELL_SIZE

# 
class Snake():
    def __init__(self):
        self.snake = [
            pygame.Rect(100, 100, CELL_SIZE, CELL_SIZE),
            pygame.Rect(75, 100, CELL_SIZE, CELL_SIZE),
            pygame.Rect(50, 100, CELL_SIZE, CELL_SIZE)
        ]

        self.direction = (1, 0)
        self.next_direction = (1, 0)

        self.food = pygame.Rect(300, 300, CELL_SIZE, CELL_SIZE)

        self.score = 0