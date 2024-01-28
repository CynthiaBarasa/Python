import cv2
import numpy as np 


img = cv2.imread("face.jpeg")
kernel = np.ones((7, 7), np.float32) / 49
blurred = cv2.filter2D(img, -1, kernel)
cv2.imshow("Blurred", blurred)


cv2.waitKey(0)
