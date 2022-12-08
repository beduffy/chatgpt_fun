import random
import time

# define screen size
SCREEN_SIZE = (40, 20)

# define snake starting position
START_POS = (SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2)

# define snake starting direction
START_DIR = (1, 0)

# define snake movement speed
SPEED = 1

# define block size
BLOCK_SIZE = 1

# create snake
snake = [START_POS]

# set snake direction
direction = START_DIR

# create apple
apple = (0, 0)

# create screen
screen = [[' ' for _ in range(SCREEN_SIZE[0])] for _ in range(SCREEN_SIZE[1])]

# game loop
while True:
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
        sys.exit()

    # clear screen
    screen = [[' ' for _ in range(SCREEN_SIZE[0])] for _ in range(SCREEN_SIZE[1])]

    # draw snake
    for x, y in snake:
        screen[y][x] = '#'

    # draw apple
    screen[apple[1]][apple[0]] = '@'

    # update screen
    for row in screen:
        print(''.join(row))

    # handle key events
    key = input()
    if key == 'a':
        direction = (-1, 0)
    elif key == 'd':
        direction = (1, 0)
    elif key == 'w':
        direction = (0, -1)
    elif key == 's':
        direction = (0, 1)

    # wait for next frame
    time.sleep(0.1)