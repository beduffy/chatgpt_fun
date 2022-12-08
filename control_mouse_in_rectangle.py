# Prompt after previous circle control stuff: What about in the path of a rectangle?
import pyautogui
import time
import math

# Set the width and height of the rectangle in pixels
width = 100
height = 200

# Calculate the center of the screen
screen_width, screen_height = pyautogui.size()
center_x, center_y = screen_width / 2, screen_height / 2

# Calculate the coordinates of the four corners of the rectangle
top_left_x = center_x - width / 2
top_left_y = center_y - height / 2
top_right_x = center_x + width / 2
top_right_y = center_y - height / 2
bottom_left_x = center_x - width / 2
bottom_left_y = center_y + height / 2
bottom_right_x = center_x + width / 2
bottom_right_y = center_y + height / 2

# Move the mouse to the top left corner of the rectangle
pyautogui.moveTo(top_left_x, top_left_y)

# Start the loop to move the mouse in a rectangle
for i in range(4):
    # Move the mouse to the top right corner of the rectangle
    pyautogui.moveTo(top_right_x, top_right_y)
    # Move the mouse to the bottom right corner of the rectangle
    pyautogui.moveTo(bottom_right_x, bottom_right_y)
    # Move the mouse to the bottom left corner of the rectangle
    pyautogui.moveTo(bottom_left_x, bottom_left_y)
    # Move the mouse back to the top left corner of the rectangle
    pyautogui.moveTo(top_left_x, top_left_y)

    # Sleep for a short amount of time to create a smooth movement
    time.sleep(0.01)