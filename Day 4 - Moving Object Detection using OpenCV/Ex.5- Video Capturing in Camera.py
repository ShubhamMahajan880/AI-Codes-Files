"""import cv2
import time

cam = cv2.VideoCapture(0)
time.sleep(1)
while True:
    _,img = cam.read()
    cv2.imshow("cameraFeed",img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()
"""







import cv2
import time
#url = 'http://192.168.29.107:8080/video'
url = 'http://10.20.20.106:8080/video'
cam = cv2.VideoCapture(url)
time.sleep(1)
while True:
    _,img = cam.read()    
    cv2.imshow("cameraFeed",img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()

    
