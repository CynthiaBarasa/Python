import cv2

img = cv2.imread("face.jpeg")
canny = cv2.Canny(img, 20, 170)
cv2.imshow("Canny", canny)

cv2.waitKey(0)
