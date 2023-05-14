import cv2
img = cv2.imread("spiderman.jpg")
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("GrayImage.jpg",grayImg)
cv2.imshow("Original",img)
cv2.imshow("GrayImage",grayImg)
cv2.waitKey(100)
cv2.destroyAllWindows()
