import cv2
img = cv2.imread("wannda.png")
cv2.imshow("pink folder",img)
cv2.imwrite("pinkfolder.png",img)
cv2.waitkey(0)
cv2.destoryAllWindows()

