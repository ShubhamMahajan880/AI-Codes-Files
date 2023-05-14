import cv2
import imutils
img = cv2.imread("mario.jpg")
resizeImg = imutils.resize(img,width=20)
cv2.imwrite("resizedImg.jpg",resizeImg)

