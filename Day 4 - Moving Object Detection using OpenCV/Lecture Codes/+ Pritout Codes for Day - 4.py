            """All Codes of Moving Object Detection using Open-CV"""


                # Code for Resizing an Image
import cv2
import imutils
img = cv2.imread("study.jpg")
resizeImg = imutils.resize(img,width=60) # By this width command we can esily increase as wll as decrease the size of an image
cv2.imwrite("resizedImg.jpg",resizeImg)



