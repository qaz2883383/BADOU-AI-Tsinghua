import cv2
import numpy as np

scale = 0.6

img = cv2.imread("test.png")

shape = img.shape

new_shape = (int(shape[0]*scale), int(shape[1]*scale), shape[2])

print(shape)
print(new_shape)

new_img = np.zeros(new_shape, np.uint8)

for i in range(new_shape[0]):
    for j in range(new_shape[1]):
        new_img[i][j] = img[int(i/scale+0.5)][int(j/scale+0.5)]
        
cv2.imshow("new", new_img)
cv2.waitKey(0)
#print(img)
print(new_img)