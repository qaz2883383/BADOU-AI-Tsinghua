import cv2
import numpy as np

scale = 700/512

img = cv2.imread("test.png")

shape = img.shape

new_shape = (int(shape[0]*scale), int(shape[1]*scale), shape[2])

print(shape)
print(new_shape)

new_img = np.zeros(new_shape, np.uint8)

for i in range(new_shape[0]):
    for j in range(new_shape[1]):
        for c in range(new_shape[2]):
            #new_img[i][j] = img[int(i/scale+0.5)][int(j/scale+0.5)]
            x_s = i/scale - int(i/scale)
            y_s = j/scale - int(j/scale)
            x0 = int(i/scale)
            x1 = min(int(i/scale)+1, shape[0] - 1)
            y0 = int(j/scale)
            y1 = min(int(j/scale)+1, shape[1] - 1)
            
            d1 = int((1-x_s)*img[x0][y0][c] + x_s*img[x1][y0][c])
            d2 = int((1-x_s)*img[x0][y1][c] + x_s*img[x1][y1][c])
            new_img[i][j][c] = int((1-y_s)*d1 + y_s*d2 + 0.5)
        
        
cv2.imshow("new", new_img)
cv2.waitKey(0)
#print(img)
print(new_img)