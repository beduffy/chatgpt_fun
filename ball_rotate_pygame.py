# pygame code for making a ball rotate in a circle
# I ran this code and see nothing, why?
# then it told me to add the fill for white
# how to make it rotate slower. speed
# how to make it change colour every second
# how would we make the ball orbit the mouse position?

import time, sys
import pygame
import math

# define screen size
SCREEN_SIZE = (400, 400)

# initialize pygame
pygame.init()

# create screen
screen = pygame.display.set_mode(SCREEN_SIZE)

# create ball
ball_image = pygame.Surface((20, 20))
ball_rect = ball_image.get_rect()
ball_image.fill((255, 255, 255))  # white

# set ball starting position
ball_rect.center = (SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2)

# set ball starting angle
angle = 0

# set ball rotation speed
speed = 0.0001

# clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()


# set initial ball color
ball_color = pygame.Color(255, 255, 255)  # black

# game loop
while True:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # get mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # calculate ball position
    x = mouse_x + 100 * math.cos(angle)
    y = mouse_y + 100 * math.sin(angle)
    ball_rect.center = (x, y)

    # calculate new ball position
    # x = SCREEN_SIZE[0] // 2 + 100 * math.cos(angle)
    # y = SCREEN_SIZE[1] // 2 + 100 * math.sin(angle)
    # ball_rect.center = (x, y)

    # rotate ball
    angle += speed

    # update ball color
    # elapsed_time = clock.tick()
    elapsed_time = pygame.time.get_ticks() - start_time
    print(elapsed_time)
    if elapsed_time >= 1000:  # 1 second has passed
        # change ball color
        print('change ball color')
        ball_color = pygame.Color(
            # 255 * (angle % 2),  # red
            # 255 * (angle % 3),  # green
            # 255 * (angle % 5),  # blue
            min(255, max(0, int(255 * (angle % 2)))),  # red
            min(255, max(0, int(255 * (angle % 3)))),  # green
            min(255, max(0, int(255 * (angle % 5)))),  # blue
        )

    # set ball color
    ball_image.fill(ball_color)

    # clear screen
    screen.fill((0, 0, 0))

    # draw ball
    screen.blit(ball_image, ball_rect)

    # update screen
    pygame.display.flip()
    # time.sleep(0.01)