import cv2
img = cv2.imread("spiderman.jpg")
cv2.imshow("Hey Spidey",img)
cv2.imwrite("Hey Spidey.jpg",img)
cv2.waitkey(0)
cv2.destoryAllWindows()
