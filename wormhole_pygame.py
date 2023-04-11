import pygame
import math
import random

# Initialize Pygame
pygame.init()

# Set up the display
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Wormhole Animation")

# Set up colors
bg_color = (0, 0, 0)

def draw_circle(screen, color, pos, size):
    pygame.draw.circle(screen, color, pos, size, 1)

def create_color_gradient(n, start_color, end_color):
    colors = []
    for i in range(n):
        r = start_color[0] + (end_color[0] - start_color[0]) * i // n
        g = start_color[1] + (end_color[1] - start_color[1]) * i // n
        b = start_color[2] + (end_color[2] - start_color[2]) * i // n
        colors.append((r, g, b))
    return colors

def wormhole_animation():
    running = True
    angle = 0
    num_circles = 100
    colors = create_color_gradient(num_circles, (255, 0, 255), (0, 255, 255))
    clock = pygame.time.Clock()

    while running:
        screen.fill(bg_color)

        # Draw circles
        for i in range(num_circles):
            size = (i + 1) * 2
            pos = (int(window_size[0] / 2 + size * math.cos(angle + i * math.pi / 10)),
                   int(window_size[1] / 2 + size * math.sin(angle + i * math.pi / 10)))
            draw_circle(screen, colors[i], pos, size)

        # Update display
        pygame.display.flip()

        # Increase angle for spinning effect
        angle += 0.02

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        clock.tick(60)

    pygame.quit()

wormhole_animation()