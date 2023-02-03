import cv2
import imutils
import numpy as np

print ("librrias leidas")

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

while True:
    ret, frame = cap.read()
    hvs = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    #amarillo#
    amarillo_osc = np.array([25,70,120])
    amarillo_cla = np.array([30,255,255])
    #rojo#
    rojo_osc = np.array([0,50,120])
    rojo_cla = np.array([10,255,255])
    #verde#
    verde_osc = np.array([40,70,80])
    verde_cla = np.array([70,255,255])
    #azul#
    azul_osc = np.array([1,7,230])
    azul_cla = np.array([121,255,255])
    
    cara1 = cv2.inRange(hvs, amarillo_osc, amarillo_cla)
    cara2 = cv2.inRange(hvs, rojo_osc, rojo_cla)
    cara3 = cv2.inRange(hvs, verde_osc, verde_cla)
    cara4 = cv2.inRange(hvs, azul_osc, azul_cla)
    
    cnst1 = cv2.findContours(cara1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnst1 = imutils.grab_contours(cnst1)
    
    cnst2 = cv2.findContours(cara2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnst2 = imutils.grab_contours(cnst2)
    
    cnst3 = cv2.findContours(cara3, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnst3 = imutils.grab_contours(cnst3)
    
    cnst4 = cv2.findContours(cara4, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnst4 = imutils.grab_contours(cnst4)
    
    for c in cnst1:
        area1 = cv2.contourArea(c)
        if area1>5000:
            cv2.drawContours(frame, [c], -1, (0, 255, 0), 3)
            M = cv2.moments(c)
            cx = int(M["m10"]/M["m00"])
            cy = int(M["m01"] / M["m00"])
            
            cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
            cv2.putText(frame, "amarillo", (cx-20, cy-20), cv2.FONT_ITALIC, 2, (255, 255, 255), 2)
            
    for c in cnst2:
        area2 = cv2.contourArea(c)
        if area2>5000:
            cv2.drawContours(frame, [c], -1, (0, 255, 0), 3)
            M = cv2.moments(c)
            cx = int(M["m10"]/M["m00"])
            cy = int(M["m01"] / M["m00"])
            
            cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
            cv2.putText(frame, "rojo", (cx-20, cy-20), cv2.FONT_ITALIC, 2, (255, 255, 255), 2)        
    
    for c in cnst3:
        area3 = cv2.contourArea(c)
        if area3>5000:
            cv2.drawContours(frame, [c], -1, (0, 255, 0), 3)
            M = cv2.moments(c)
            cx = int(M["m10"]/M["m00"])
            cy = int(M["m01"] / M["m00"])
            
            cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
            cv2.putText(frame, "verde", (cx-20, cy-20), cv2.FONT_ITALIC, 2, (255, 255, 255), 2)        
            
    for c in cnst4:
        area4 = cv2.contourArea(c)
        if area4>5000:
            cv2.drawContours(frame, [c], -1, (0, 255, 0), 3)
            M = cv2.moments(c)
            cx = int(M["m10"]/M["m00"])
            cy = int(M["m01"] / M["m00"])
            
            cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
            cv2.putText(frame, "azul", (cx-20, cy-20), cv2.FONT_ITALIC, 2, (255, 255, 255), 2)        
            

                
    cv2.imshow("video", frame)
    k = cv2.waitKey(1)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
