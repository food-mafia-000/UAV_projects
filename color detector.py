import numpy as np
import cv2


cap = cv2.VideoCapture(0)

while True:
    _,frame=cap.read()

    
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # #Red vo
    low_red = np.array([160, 100, 10])
    high_red = np.array([179, 255, 255])

    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    anti_mask= cv2.bitwise_not(red_mask)
    red = cv2.bitwise_and(frame, frame, mask = red_mask)
    red_gray=cv2.bitwise_and(gray,gray, mask=anti_mask)

    al_red=np.stack((red_gray,)*3,axis=-1)
    final_red=cv2.add (red,al_red)

    cv2.imshow("frame",frame)
    cv2.imshow("RED", final_red)
    key = cv2.waitKey(1)
    if key == 27:
        break