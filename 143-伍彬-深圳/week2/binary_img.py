import cv2
import numpy as np

img = cv2.imread("test.png")

print(img)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_binary = img_gray.copy()

img_binary[img_gray > 125] = 255
img_binary[img_gray < 125] = 0

cv2.imshow("bin", img_binary)
cv2.waitKey(0)

print(img_gray)
print(img_binary)