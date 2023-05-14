            """ All Codes of Computer Vision and it's Libraries"""

#code for Insertion of an image
import cv2
img = cv2.imread("pietro.png")
cv2.imshow("blue folder",img)
cv2.imwrite("bluefolder.png",img)
cv2.waitkey(0)
cv2.destoryAllWindows()

#Code for getting Properties of any image
import cv2
img = cv2.imread("Sunny.jpg")
print(img.shape)
print(img.size)
print(img.dtype)#what kind of property


#code for color cvt to Gray_img
import cv2
img = cv2.imread("mario.jpg")
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("GrayImage.jpg",grayImg)
cv2.imshow("Original",img)
cv2.imshow("GrayImage",grayImg)
cv2.waitKey(0)#Here zero(0) is uses for hold the image. It behaves as infinity time seconds
cv2.destroyAllWindows()













