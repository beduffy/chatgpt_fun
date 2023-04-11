import pygame

def create_image():
    # Initialize Pygame
    pygame.init()

    # Set up the display
    window_size = (800, 600)
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Man Running After Panda")

    # Load images
    man_img = pygame.image.load("man.png")
    panda_img = pygame.image.load("panda.png")

    # Scale images
    man_img = pygame.transform.scale(man_img, (100, 100))
    panda_img = pygame.transform.scale(panda_img, (100, 100))

    # Draw background
    bg_color = (255, 255, 255)
    screen.fill(bg_color)

    # Draw the man and the panda
    man_pos = (100, window_size[1] - 150)
    panda_pos = (300, window_size[1] - 150)
    screen.blit(man_img, man_pos)
    screen.blit(panda_img, panda_pos)

    # Save the image
    pygame.display.flip()
    pygame.image.save(screen, "man_running_after_panda.png")

    # Quit Pygame
    pygame.quit()

create_image()
