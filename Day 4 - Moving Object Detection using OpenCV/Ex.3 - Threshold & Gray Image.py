import cv2
img = cv2.imread("mario.jpg")
grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
thresImg = cv2.threshold(grayImg,200,50,cv2.THRESH_BINARY) [1] # After gray image there is 2 parameters for handle sharpness of threshold command
#_,thresImg = cv2.threshold(grayImg,200,50,cv2.THRESH_BINARY) ( at the place of [1] we can also use _, )
cv2.imwrite("thresholdImage.jpg",thresImg)
