import cv2

img = cv2.imread("test.png")

print(img)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

print(img_gray)
cv2.imshow("Gray", img_gray)
cv2.waitKey(0) 