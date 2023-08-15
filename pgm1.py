#Write a Program to read a digital image. Split and display image into 4 quadrants, up, down, right and left.

import cv2
import numpy as np

# Load the image
img = cv2.imread('krishna.jpg')

# Check if image was loaded successfully
if img is None:
    print("Error: Could not read image")
    exit()

# Get the dimensions of the image
height, width = img.shape[:2]
print(height,width)
# Calculate the center of the image
center_x, center_y = int(width/2), int(height/2)

# Split the image into four quadrants
top_left = img[0:center_y, 0:center_x]
top_right = img[0:center_y, center_x:width]
bottom_left = img[center_y:height, 0:center_x]
bottom_right = img[center_y:height, center_x:width]

# Create named windows for each quadrant
cv2.namedWindow('Top Left', cv2.WINDOW_NORMAL)
cv2.namedWindow('Top Right', cv2.WINDOW_NORMAL)
cv2.namedWindow('Bottom Left', cv2.WINDOW_NORMAL)
cv2.namedWindow('Bottom Right', cv2.WINDOW_NORMAL)

# Resize the windows
cv2.resizeWindow('Top Left', 400, 400)
cv2.resizeWindow('Top Right', 400, 400)
cv2.resizeWindow('Bottom Left', 400, 400)
cv2.resizeWindow('Bottom Right', 400, 400)

# Display the four quadrants
cv2.imshow('Top Left', top_left)
cv2.imshow('Top Right', top_right)
cv2.imshow('Bottom Left', bottom_left)
cv2.imshow('Bottom Right', bottom_right)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()