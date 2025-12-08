import pygame
from random import randint

from constants import *

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

        self.food = pygame.Rect(300 + (CELL_SIZE * 0.1), 300 + (CELL_SIZE * 0.1), CELL_SIZE * 0.8, CELL_SIZE * 0.8)

        self.score = 0

    def reset(self):
        self.snake = [
            pygame.Rect(100, 100, CELL_SIZE, CELL_SIZE),
            pygame.Rect(75, 100, CELL_SIZE, CELL_SIZE),
            pygame.Rect(50, 100, CELL_SIZE, CELL_SIZE)
        ]

        self.direction = (1, 0)
        self.next_direction = (1, 0)

        self.score = 0

    def update(self):
        self.direction = self.next_direction

        current_head = self.snake[0]
        new_x = current_head.x + (self.direction[0] * CELL_SIZE)
        new_y = current_head.y + (self.direction[1] * CELL_SIZE)

        new_head = pygame.Rect(new_x, new_y, CELL_SIZE, CELL_SIZE)

        if not (self.check_wall_collision(new_head) or self.check_self_collision(new_head)):
            self.snake.insert(0, new_head)

            self.check_food(new_head)
        else:
            self.reset()

    def move(self, dir):
        match dir:
            case "UP":
                if self.direction != (0, 1):
                    self.next_direction = (0, -1)
            case "DOWN":
                if self.direction != (0, -1):
                    self.next_direction = (0, 1)
            case "LEFT":
                if self.direction != (1, 0):
                    self.next_direction = (-1, 0)
            case "RIGHT":
                if self.direction != (-1, 0):
                    self.next_direction = (1, 0)

    def check_food(self, new_head):
        if new_head.colliderect(self.food):
            self.score += 1

            self.food.x = (randint(0, int(SCREEN_WIDTH / CELL_SIZE) - 1) * CELL_SIZE) + (CELL_SIZE * 0.1)
            self.food.y = (randint(0, int(SCREEN_HEIGHT / CELL_SIZE) - 1) * CELL_SIZE) + (CELL_SIZE * 0.1)
        else:
            self.snake.pop()

    # Collisions
    def check_wall_collision(self, head):
        if head.left < 0 or head.right > SCREEN_WIDTH or head.top < 0 or head.bottom > SCREEN_HEIGHT:
            return True
        return False
    
    def check_self_collision(self, head):
        for part in self.snake[1:]:
            if head.colliderect(part):
                return True
        return False