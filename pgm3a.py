import cv2
import numpy as np
img=cv2.imread('krishna.jpg',cv2.IMREAD_GRAYSCALE)
kernel=np.ones((5,5),np.uint8)
erosion_type=cv2.MORPH_RECT
erosion=cv2.erode(img, kernel,iterations=1)
subtracted=cv2.subtract(img, erosion)
cv2.namedWindow("Original Image",cv2.WINDOW_NORMAL)
cv2.resizeWindow("Original Image",400,500)
cv2.namedWindow("Eroded Image",cv2.WINDOW_NORMAL)
cv2.resizeWindow("Eroded Image",400,500)
cv2.namedWindow("Subtracted Image",cv2.WINDOW_NORMAL)
cv2.resizeWindow("Subtracted Image",400,500)
cv2.imshow("Original Image", img)
cv2.imshow("Eroded Image", erosion)
cv2.imshow("Subtracted Image",subtracted)
cv2.waitKey(0)
cv2.destroyAllWindows() 