import pyautogui
import time
import math

# Set the radius of the circle in pixels
radius = 100

# Calculate the center of the screen
screen_width, screen_height = pyautogui.size()
center_x, center_y = screen_width / 2, screen_height / 2

# Move the mouse to the center of the screen
pyautogui.moveTo(center_x, center_y)

# Start the loop to move the mouse in a circle
for i in range(360):
    # Calculate the new x and y coordinates for the mouse
    x = center_x + radius * math.cos(math.radians(i))
    y = center_y + radius * math.sin(math.radians(i))

    # Move the mouse to the new coordinates
    pyautogui.moveTo(x, y)

    # Sleep for a short amount of time to create a smooth movement
    # time.sleep(0.01)