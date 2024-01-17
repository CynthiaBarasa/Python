import cv2

img = cv2.imread("face.jpeg")

cv2.imwrite("output.jpeg", img)

cv2.waitKey(0)
