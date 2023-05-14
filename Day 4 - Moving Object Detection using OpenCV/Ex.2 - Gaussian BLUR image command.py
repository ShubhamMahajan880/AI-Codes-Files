import cv2
img = cv2.imread("mario.jpg")
gaussianBlurImg = cv2.GaussianBlur(img,(21,21),0)#This odd parameters's value are responsible for BLURNESS of image and 0 is standard format for blur image
cv2.imwrite("gaussianImage.jpg",gaussianBlurImg)
