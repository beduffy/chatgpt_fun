import cv2
import numpy as np

# Read the input text file
with open("chatgpt_3_5_scroll_text.py", "r") as f:
    text = f.read()

# Set the font and font size
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1

# Get the text size and create a blank image of the same size
text_size, _ = cv2.getTextSize(text, font, font_scale, thickness=2)
img = np.zeros((text_size[1], text_size[0], 3), dtype=np.uint8)

# Define the video codec and frame rate
fourcc = cv2.VideoWriter_fourcc(*'XVID')
fps = 25.0

out = cv2.VideoWriter('output.avi', fourcc, fps, (img.shape[1], img.shape[0]))

print(img.shape[1], img.shape[0])

# Loop through each character in the text and add it to the image
x, y = 0, text_size[1]
for char in text:
    char_size, _ = cv2.getTextSize(char, font, font_scale, thickness=2)
    img_temp = np.zeros((char_size[1], char_size[0], 3), dtype=np.uint8)
    cv2.putText(img_temp, char, (0, char_size[1]), font, font_scale, (255, 255, 255), thickness=2)
    img[y - char_size[1]:y, x:x + char_size[0]] = img_temp
    x += char_size[0]

    # Scroll the image vertically
    if x >= text_size[0]:
        x = 0
        y += char_size[1]
        if y >= img.shape[0]:
            y = text_size[1]

    # Display the image
    cv2.imshow("Scrolling Text Animation", img)
    cv2.waitKey(25)

    # Save each frame of the animation to an AVI file
    out.write(img)

# Release the video writer and close the OpenCV window
out.release()
cv2.destroyAllWindows()