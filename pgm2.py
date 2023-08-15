import cv2
import numpy as np
img=cv2.imread('krishna.jpg')
print('SIZE OF ORIGINAL IMAGE:HEIGHT WIDTH')
height,width=img.shape[:2]
print(height,width)
rows,cols=img.shape[:2]
M=cv2.getRotationMatrix2D((cols/2,rows/2),45,1)
rotated_img=cv2.warpAffine(img,M,(cols,rows))
scaled_img=cv2.resize(img,None,fx=0.2,fy=0.2,interpolation=cv2.INTER_LINEAR)
print('SIZE OF SCALED IMAGE:HEIGHT WIDHT')
height,widht=scaled_img.shape[:2]
print(height,width)
M=np.float32([[1,0,100],[0,1,50]])
translated_img=cv2.warpAffine(img,M,(cols,rows))

cv2.namedWindow('Original Image',cv2.WINDOW_NORMAL)
cv2.namedWindow('Rotated Image',cv2.WINDOW_NORMAL)
cv2.namedWindow('Scaled Image',cv2.WINDOW_NORMAL)
cv2.namedWindow('Translated Image',cv2.WINDOW_NORMAL)
cv2.resizeWindow('Original Image',300,300)
cv2.resizeWindow('Rotated Image',300,300)
cv2.resizeWindow('Scaled Image',300,300)
cv2.resizeWindow('Translated Image',300,300)

cv2.imshow('Original image',img)
cv2.imshow('Rotated Image',rotated_img)
cv2.imshow('Scaled Image',scaled_img)
cv2.imshow('Translated Image',translated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()