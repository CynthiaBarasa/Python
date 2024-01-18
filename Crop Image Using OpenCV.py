import cv2

img = cv2.imread("face.jpeg")
height, width = img.shape[: 2]
start_row, start_col = int(height * .15), int(width * .15)
end_row, end_col = int(height * .65), int(width * .65)

cropped = img[start_row: end_row, start_col: end_col]
cv2.imshow("Cropped", cropped)
cv2.imshow("Original", img)

cv2.waitKey(0)
