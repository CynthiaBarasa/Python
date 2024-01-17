import cv2

img = cv2.imread("face.jpeg")
height , width = img.shape[: 2]
rotateimg = cv2.getRotationMatrix2D((width / 2, height / 2), 70, .5)
finalimg = cv2.warpAffine(img, rotateimg, (width, height))
cv2.imshow("Rotated Image", finalimg)
cv2.imshow("Original", img)


cv2.waitKey(0)
