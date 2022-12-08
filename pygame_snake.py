# prompt: pygame code for snake

import pygame
import random
import time

# define screen size
SCREEN_SIZE = (400, 400)

# define snake starting position
START_POS = (SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2)

# define snake starting direction
START_DIR = (1, 0)

# define snake movement speed
SPEED = 5

# define block size
BLOCK_SIZE = 10

# initialize pygame
pygame.init()

# create screen
screen = pygame.display.set_mode(SCREEN_SIZE)

# create snake
snake = [START_POS]

# set snake direction
direction = START_DIR

# create apple
apple = (40, 40)

# create clock
clock = pygame.time.Clock()

# game loop
while True:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # handle key events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = (-1, 0)
            elif event.key == pygame.K_RIGHT:
                direction = (1, 0)
            elif event.key == pygame.K_UP:
                direction = (0, -1)
            elif event.key == pygame.K_DOWN:
                direction = (0, 1)

    # move snake
    snake.insert(0, (snake[0][0] + direction[0] * SPEED, snake[0][1] + direction[1] * SPEED))

    # check for collision with apple
    if snake[0] == apple:
        # move snake
        snake.insert(0, (snake[0][0] + direction[0] * SPEED, snake[0][1] + direction[1] * SPEED))

    # check for collision with apple
    if snake[0] == apple:
        # generate new apple
        apple = (random.randint(0, SCREEN_SIZE[0] // BLOCK_SIZE - 1) * BLOCK_SIZE, random.randint(0, SCREEN_SIZE[1] // BLOCK_SIZE - 1) * BLOCK_SIZE)
    else:
        # remove last block of snake
        snake.pop()

    # check for game over
    if snake[0][0] < 0 or snake[0][0] >= SCREEN_SIZE[0] or snake[0][1] < 0 or snake[0][1] >= SCREEN_SIZE[1] or snake[0] in snake[1:]:
        # game over
        print("Game Over!")
        time.sleep(3)
        pygame.quit()
        sys.exit()

    # clear screen
    screen.fill((0, 0, 0))

    # draw snake
    for block in snake:
        pygame.draw.rect(screen, (255, 255, 255), (block[0], block[1], BLOCK_SIZE, BLOCK_SIZE))

    # draw apple
    pygame.draw.rect(screen, (255, 0, 0), (apple[0], apple[1], BLOCK_SIZE, BLOCK_SIZE))

    # update screen
    pygame.display.flip()

    # limit frame rate
    clock.tick(10)