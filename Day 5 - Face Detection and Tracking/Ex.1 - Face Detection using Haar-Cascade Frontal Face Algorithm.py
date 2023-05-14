"""import cv2

alg = "haarcascade_frontalface_default.xml"
haar_cascade = cv2.CascadeClassifier(alg)

url = 'http://192.168.29.107:8080/video'
cam = cv2.VideoCapture(url)

while True:
    _,img = cam.read()
    grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face = haar_cascade.detectMultiScale(grayImg,1.3,4)
    for (x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("FaceDetection",img)
    key = cv2.waitkey(1)
    if key == 27:
        break

cam.release()
cv2.destroyAllWindows()
"""
        
import cv2

cascade_face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#url = 'http://192.168.29.107:8080/video'
url = 'http://10.37.20.173:8080/video'
cap = cv2.VideoCapture(url)

while True:
    ret,img = cap.read()
    print(ret)
    g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    f = cascade_face.detectMultiScale(g, 1.3, 5)

    for (x,y,w,h) in f:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 4)

        cv2.imshow('img',img)
        k = cv2.waitkey(0) & 0xff
        if k == 27:
            break

cap.release()
cv2.destroyAllWindows

        
