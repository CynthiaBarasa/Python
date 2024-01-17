import cv2

img = cv2.imread("face.jpeg")
cv2.imshow("Output Image", img)

cv2.waitKey(0)
