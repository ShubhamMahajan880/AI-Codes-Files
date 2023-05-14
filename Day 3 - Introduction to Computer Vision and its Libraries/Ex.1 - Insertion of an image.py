import cv2
img = cv2.imread("pietro.png")
cv2.imshow("blue folder",img)
cv2.imwrite("bluefolder.png",img)
cv2.waitkey(0)
cv2.destoryAllWindows()








