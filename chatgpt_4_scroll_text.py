import pygame
import cv2
import time
import numpy as np

def create_animation(textfile, X, Y, Z, R):
    # Initialize Pygame
    pygame.init()
    
    # Set up the display
    window_size = (800, 600)
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Text Animation")
    
    # Set up the font and color
    font = pygame.font.Font(None, 36)
    text_color = (0, 0, 0)  # Black text
    bg_color = (255, 255, 255)  # White background

    # Load the text file
    with open(textfile, "r") as f:
        lines = f.readlines()

    def render_text(offset):
        screen.fill(bg_color)
        for i, line in enumerate(lines[int(offset):int(offset)+X]):
            rendered_line = font.render(line[:Y], True, text_color)
            screen.blit(rendered_line, (10, 10 + i * 40 - (offset % 1) * 40))

    # Set up the recording
    fps = 60  # Increase the frame rate for smoother animation
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter("animation.avi", fourcc, fps, window_size[::-1], True)

    start_time = time.time()
    current_offset = 0
    recording_time = R
    running = True

    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Calculate the elapsed time and update the offset
        elapsed_time = time.time() - start_time
        current_offset = Z * elapsed_time

        # Check if we have reached the end of the file
        if int(current_offset) + X >= len(lines):
            break

        # Render the text
        render_text(current_offset)

        # Record the frame
        frame = pygame.surfarray.array3d(screen)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        out.write(frame)

        # Update the display
        pygame.display.flip()
        pygame.time.Clock().tick(fps)

        # Check if we have recorded enough time
        if elapsed_time >= recording_time:
            break

    # Clean up
    pygame.quit()
    out.release()

# Example usage:
create_animation("chatgpt_4_scroll_text.py", 15, 50, 5, 10)
