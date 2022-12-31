import cv2
#import matplotlib.pyplot as plt
import numpy as np

height=int(input(" Enter height :"))
cap = cv2.VideoCapture(0)   
while(True):
    ret, frame = cap.read()
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lwr=np.array([0,160,20])
    upr=np.array([10,180,225])
   
    #setting all values of not red h as 0
    h,s,v=cv2.split(hsv)
    h[h>180]=0
    h[h<150]=0

#    cv2.imshow('1',hsv)

    #nomalizing to increase contrat and make clearer image
    normed = cv2.normalize(h, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8UC1)   #cv_8uc1-needed for contours
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, ksize=(3,3))    #creating kernel
    opened = cv2.morphologyEx(normed, cv2.MORPH_OPEN, kernel)                   #open morph 
    
    
    #finding contours and taking contours from output
    items = cv2.findContours(opened, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contours = items[0] #if len(items) == 2 else items[1]

    #making a destination frame on which rectangle will be drawn
    dst = frame.copy()

    for cnt in contours:
        ## Get the stright bounding rect
        bbox = cv2.boundingRect(cnt)
        x,y,w,h = bbox
        if (w<60 or h < 60) and (w*h <2900  or w > 500):
            continue

        ## Draw rect
        font=cv2.FONT_HERSHEY_COMPLEX
        cv2.rectangle(dst, (x,y), (x+w,y+h), (255,0,0), 1, 16)
        yc=y
        px=height/h
        y=px*w

        cv2.putText(dst,str(y),(x,yc),font,1,(255,255,255),1,cv2.LINE_AA)

    
  
 
    cv2.imshow("red box",dst)
    
       
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release() 
cv2.destroyAllWindows()
