import pygame
import sys
# Initialize Pygame
pygame.init()
# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball Simulation")
# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
# Ball properties
ball_radius = 25
x, y = WIDTH // 2, HEIGHT // 2
speed_x, speed_y = 5, 4  # velocity components
# Clock for frame rate
clock = pygame.time.Clock()
# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # Move the ball
    x += speed_x
    y += speed_y
    # Bounce off walls (reverse direction)
    if x - ball_radius <= 0 or x + ball_radius >= WIDTH:
        speed_x = -speed_x
    if y - ball_radius <= 0 or y + ball_radius >= HEIGHT:
        speed_y = -speed_y
    # Fill background
    screen.fill(BLACK)
    # Draw ball
    pygame.draw.circle(screen, RED, (x, y), ball_radius)
    # Update display
    pygame.display.flip()
    # Control frame rate
    clock.tick(60)
