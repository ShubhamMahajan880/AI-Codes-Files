    import cv2 
    import time 
    import imutils 
    url = 'http://192.168.29.107:8080/video'
    cam = cv2.VideoCapture(url) 
    time.sleep(0)

    firstFrame = None
    area = 400
    count = 0

    while True: 
        _,img = cam.read()
        text = "Normal"
        img = imutils.resize(img, width=500) 
        grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gauss = cv2.GaussianBlur(grayImg, (21, 21), 0)
        if firstFrame is None:
            firstFrame = gauss
            continue
        imgDiff = cv2.absdiff(firstFrame, gauss) 
        thres = cv2.threshold(imgDiff, 25, 255, cv2.THRESH_BINARY)[1]
        thres = cv2.dilate(thres, None, iterations=2) 
        cnts = cv2.findContours(thres.copy(), cv2.RETR_EXTERNAL,
                cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        for c in cnts:
            if cv2.contourArea(c) < area:
                continue
            (x, y, w, h) = cv2.boundingRect(c)

            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            count += 1
            text = "Moving Object Detected"
        print(text, count)
        num = str(count)
        cv2.putText(img, num, (420, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        cv2.putText(img, text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)
        cv2.putText(img, "Moving Object Count :", (230, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        cv2.putText(img, text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        cv2.imshow("cameraFeed",img)
        key = cv2.waitKey(1)& 0xFF 
        if key == ord("a"): 
            break
        
    cam.release()
    cv2.destroyAllWindows()
