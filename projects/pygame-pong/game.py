import pygame
import sys
import asyncio

from constants import *

# Game class
class Game():
    def __init__(self):
        pygame.init()

        # Screen
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Pong")
        
        self.clock = pygame.time.Clock()

        # Game running boolean
        self.running = True

        # Game objects
        self.player = pygame.Rect(10, (SCREEN_HEIGHT / 2 - PADDLE_HEIGHT / 2), PADDLE_WIDTH, PADDLE_HEIGHT)
        self.player_speed = 0
        self.player_score = 0

        self.opponent = pygame.Rect(SCREEN_WIDTH - 25, (SCREEN_HEIGHT / 2 - PADDLE_HEIGHT / 2), PADDLE_WIDTH, PADDLE_HEIGHT)
        self.opponent_speed = 5
        self.opponent_score = 0

        self.ball = pygame.Rect((SCREEN_WIDTH / 2 - BALL_SIZE / 2), (SCREEN_HEIGHT / 2 - BALL_SIZE / 2), BALL_SIZE, BALL_SIZE)

        # Font for displaying score
        self.font = pygame.font.Font(None, 74)

    # Run function
    async def run(self):
        global BALL_SPEED_X, BALL_SPEED_Y

        while self.running:
            # Game events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running == False
                    pygame.quit()
                    sys.exit()
                # Keydown events
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.player_speed = 6
                    elif event.key == pygame.K_UP:
                        self.player_speed = -6
                # Keyup events
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_DOWN:
                        self.player_speed = 0
                    elif event.key == pygame.K_UP:
                        self.player_speed = 0

            # Draw the new frame
            self.screen.fill(NAVY)

            pygame.draw.aaline(self.screen, WHITE, (SCREEN_WIDTH / 2, 0), (SCREEN_WIDTH / 2, SCREEN_HEIGHT))

            pygame.draw.rect(self.screen, WHITE, self.player)
            pygame.draw.rect(self.screen, WHITE, self.opponent)
            pygame.draw.ellipse(self.screen, WHITE, self.ball)

            # Update the objects on the screen
            self.ball.x += BALL_SPEED_X
            self.ball.y += BALL_SPEED_Y

            if self.ball.top <= 0 or self.ball.bottom >= SCREEN_HEIGHT:
                BALL_SPEED_Y *= -1

            self.player.y += self.player_speed

            if self.player.top <= 0:
                self.player.top = 0
            if self.player.bottom >= SCREEN_HEIGHT:
                self.player.bottom = SCREEN_HEIGHT

            # Move opponent's paddle
            self.opponent.y += self.opponent_speed

            if self.opponent.bottom >= SCREEN_HEIGHT:
                self.opponent_speed *= -1
            elif self.opponent.top <= 0:
                self.opponent_speed *= -1
            
            # Check for collisions
            if self.ball.colliderect(self.player) or self.ball.colliderect(self.opponent):
                BALL_SPEED_X *= -1

            # Check if the ball went out
            if self.ball.left < 0:
                self.opponent_score += 1
                self.ball.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                BALL_SPEED_X *= -1

            if self.ball.right > SCREEN_WIDTH:
                self.player_score += 1
                self.ball.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                BALL_SPEED_X *= -1

            # Draw Score
            player_text = self.font.render(str(self.player_score), True, WHITE)
            self.screen.blit(player_text, (SCREEN_WIDTH / 2 - 50, 10))
            
            opponent_text = self.font.render(str(self.opponent_score), True, WHITE)
            self.screen.blit(opponent_text, (SCREEN_WIDTH / 2 + 20, 10))

            # Update the screen
            pygame.display.flip()
            self.clock.tick(60)

            # Wait for asyncio
            await asyncio.sleep(0)