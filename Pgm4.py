import cv2
import numpy as np
img=cv2.imread('img.jpg', 0)
blur=cv2.GaussianBlur(img , (3,3), 0)
edges=cv2.Canny(blur, 50, 150)
sobelx=cv2.Sobel(blur, cv2.CV_64F, 1, 0, ksize=3)
sobely=cv2.Sobel(blur, cv2.CV_64F, 0, 1, ksize=3)
mag=np.sqrt(sobelx**2 + soely**2)
mag=np.uint8(mag)
cv2.imshow('Original image', img)
cv2.imshow('Edges', edges)
cv2.imshow('Texture', mag)
cv2.waitKey(0)
cv2.destroyAllWindows()
