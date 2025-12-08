import pygame
import sys
import random

from constants import *

from snake import Snake

# 
class Game():
    def __init__(self):
        pygame.init()
        self.running = True

        # Set up the screen and clock
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Snake")
        self.clock = pygame.time.Clock()

        self.move_timer = 0

        # Create snake
        self.snake = Snake()

        # Font
        self.font = pygame.font.SysFont('Arial', 25)

        # Background music
        self.background = "background.wav"
        pygame.mixer.music.load(self.background)
        pygame.mixer.music.play(-1)

    # 
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Keydown events
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.snake.move("UP")
                    if event.key == pygame.K_DOWN:
                        self.snake.move("DOWN")
                    if event.key == pygame.K_LEFT:
                        self.snake.move("LEFT")
                    if event.key == pygame.K_RIGHT:
                        self.snake.move("RIGHT")

            # Timer
            if self.move_timer > MOVE_DELAY:
                self.move_timer = 0

                # Move the snake
                self.snake.update()

            # Calculate delta time
            dt = self.clock.tick(60)
            self.move_timer += dt

            # Clear the last frame
            self.screen.fill(BLACK)

            # Draw the snake and food
            for i, part in enumerate(self.snake.snake):
                if i == 0:
                    color = GREEN
                else:
                    color = DARK_GREEN
                
                # Draw the rect
                pygame.draw.rect(self.screen, color, part)

            # Draw food
            pygame.draw.rect(self.screen, RED, self.snake.food)

            # Draw the score
            score_text = self.font.render(f"Score: {self.snake.score}", True, WHITE)
            self.screen.blit(score_text, (5, 5))

            # Update the window
            pygame.display.flip()