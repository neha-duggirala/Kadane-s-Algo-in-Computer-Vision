import cv2,numpy as np
import time,Brute_force,optimised_method

array = np.zeros((300,300))
array[90:150,150:200] = 255
array_1d = np.reshape(array,(90000,1))
print(sum(array_1d))
# Brute_force.brute_force(array_1d)
optimised_method.kadanes(array_1d)
img = cv2.imread('img.jpeg',0)
cv2.imshow("img",array)
cv2.waitKey()
