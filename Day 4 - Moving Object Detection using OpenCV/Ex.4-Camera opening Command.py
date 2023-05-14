import cv2
import time

cam = cv2.VideoCapture(0)#For initialize camera and arguement(0)uses for laptop in-built camera (1) for USB camera and any other command for ip address such as cameram
time.sleep(1)
_,img = cam.read()
cv2.imwrite("imagefromCamera.jpg",img)
cam.release()


"""
import cv2
import time
url = 'http://10.10.20.106:8080/video'
cam = cv2.VideoCapture(url)#For initialize camera and arguement(0)uses for laptop in-built camera (1) for USB camera and any other command for ip address such as cameram
time.sleep(0)#commad is uses for performing action after (time in second) run the code
_,img = cam.read()
cv2.imwrite("imagefromCamera.jpg",img)
cam.release()#To avoid such command as camera is already in use" That's why release the camera option is here

"""
