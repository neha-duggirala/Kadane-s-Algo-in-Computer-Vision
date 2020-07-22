import cv2,numpy as np
array = np.zeros((300,300))
array[90:150,150:200] = 255
img = cv2.imread('img.jpeg',0)
cv2.imshow("img",array)
cv2.waitKey()
