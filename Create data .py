import cv2
import os
import numpy as np
detector=cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')
id=1
if id == 1:
    num = 0
    tong = 0
    for i in os.listdir('C:/hocphanki5/TTNT/BTL/data'):
        num +=1
        for j in range (1,21):
            filename = 'data/'  + str(i) + '/' +str(j) + '.png'
            frame = cv2.imread(filename)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            fa = detector.detectMultiScale(gray, 1.1, 5)
            for(x,y,w,h) in fa:
                cv2.rectangle(frame,(x,y),(x+w, y+h),(0,255,0), 2)
                if not os.path.exists('dataset'):
                    os.makedirs('dataset')
                cv2.imwrite(f"dataset/anh{num}.{j}.jpg", gray[y:y+h,x:x+w])
                print(f"ghi xong {num}.{ j}")
                tong +=1
                print (tong)
    
        
if id == 2:
    cap = cv2.VideoCapture(0)
    detector=cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')
    sampleNum = 0
    while(True):
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        fa = detector.detectMultiScale(gray, 1.1, 5)
        for(x,y,w,h) in fa:
            cv2.rectangle(frame,(x,y),(x+w, y+h),(0,255,0), 2)
            if not os.path.exists('dataset2'):
                os.makedirs('dataset2')
            sampleNum+=1
            cv2.imwrite('dataset2/anh'+str(1)+'.'+str(sampleNum)+'.jpg', gray[y:y+h,x:x+w])
        cv2.imshow('frame',frame)
        if sampleNum > 19:
            break;
    cap.release()
    cv2.destroyAllWindows()
