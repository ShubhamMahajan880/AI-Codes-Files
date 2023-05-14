import cv2
img = cv2.imread("Shubh.jpg")
gaussianBlurImg = cv2.GaussianBlur(img,(101,101),0)
cv2.imwrite("gaussianImage.jpg",gaussianBlurImg)
