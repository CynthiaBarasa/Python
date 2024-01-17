import cv2

img = cv2.imread("face.jpeg")
rotateimg = cv2.transpose(img)

cv2.imshow("Transpose", rotateimg)
cv2.imshow("Original", img)

cv2.waitKey(0)
