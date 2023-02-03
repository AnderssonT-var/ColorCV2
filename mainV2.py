import numpy as np
import cv2

def nada(x):
    pass


cap = cv2.VideoCapture(0)


while(1):
    ret, frame = cap.read()
    if ret:


        hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        Tmin=cv2.inRange
        Tmax=cv2.getTrackbarPos('Tonalidad Maxima','Parametros')
        Pmin=cv2.getTrackbarPos('Pureza Minima', 'Parametros')
        Pmax=cv2.getTrackbarPos('Pureza Maxima', 'Parametros')
        Lmin=cv2.getTrackbarPos('Luminosidad Minima', 'Parametros')
        Lmax=cv2.getTrackbarPos('Luminosidad Maxima', 'Parametros')


        color_oscuro=np.array([Tmin, Pmin, Lmin])
        color_brilla=np.array([Tmax, Pmax, Lmax])

        mascara=cv2.inRange (hsv, color_oscuro, color_brilla)

        kernelx = cv2.getTrackbarPos ('Kernel X', 'Parametros')
        kernely = cv2.getTrackbarPos ('Kernel Y', 'Parametros')
        
        kernel=np.ones((kernelx, kernely), np.uint8)
        mascara=cv2.morphologyEx (mascara, cv2.MORPH_CLOSE, kernel)
        mascara=cv2.morphologyEx (mascara, cv2.MORPH_OPEN, kernel)
        contornos, _ =cv2.findContours (mascara, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(frame, contornos, -1, (0,0,0),2)
        cv2.imshow("Camara", frame)
        cv2.imshow("Mascara", mascara)

        k=cv2.waitKey(5)
        if k == 27:
            cv2.destroyAllWindows()
            break
        
        
cap.release()


