import cv2

img = cv2.imread("face.jpeg")
print(img.shape)
print("Height: ", img.shape[0])
print("Width: ", img.shape[1])

cv2.waitKey(0)

