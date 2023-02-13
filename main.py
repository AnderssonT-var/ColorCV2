import cv2
import imutils
import numpy as np
import json

import conexionc

cursor = conexionc.con.conexion.cursor()

cap = cv2.VideoCapture(1)
cap.set(3, 640)
cap.set(4, 480)

while True:
    ret, frame = cap.read()
    #print("lectura camara")
    hvs = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #print("fin lectura camara")

    #azul oscuro#
    azul_osc = np.array([100, 100, 20],np.uint8)
    azul_cla = np.array([125, 255, 255],np.uint8)
    #naranja#
    naranja_osc = np.array([15, 100, 20],np.uint8)
    naranja_cla = np.array([17, 255, 255],np.uint8)
    #plomo#
    plomo_osc = np.array([68, 84, 106])
    plomo_cla = np.array([92, 114, 144])
    #verde#
    verde_osc = np.array([40, 70, 80])
    verde_cla = np.array([70, 255, 255])
    #rosa#
    rosa_osc = np.array([255, 0, 220])
    rosa_cla = np.array([255, 0, 255])
    #celeste#
    celeste_osc = np.array([186, 126, 65])
    celeste_cla = np.array([223, 120, 17])
    #rojo#
    rojo_osc = np.array([0, 100, 20],np.uint8)
    rojo_cla = np.array([8, 255, 253],np.uint8)
    #plomoneg#
    plomoneg_osc = np.array([128, 128, 128])
    plomoneg_cla = np.array([166, 166, 166])
    #negro#
    negro_osc = np.array([0, 0, 0],np.uint8)
    negro_cla = np.array([0, 0, 0],np.uint8)
    #amarillo#
    amarillo_osc = np.array([45, 255, 255],np.uint8)
    amarillo_cla = np.array([45, 255, 255],np.uint8)

    cara1 = cv2.inRange(hvs, azul_osc, azul_cla)
    cara2 = cv2.inRange(hvs, naranja_osc, naranja_cla)
    cara3 = cv2.inRange(hvs, plomo_osc, plomo_cla)
    cara4 = cv2.inRange(hvs, verde_osc, verde_cla)
    cara5 = cv2.inRange(hvs, rosa_osc, rosa_cla)
    cara6 = cv2.inRange(hvs, celeste_osc, celeste_cla)
    cara7 = cv2.inRange(hvs, rojo_osc, rojo_cla)
    cara8 = cv2.inRange(hvs, plomoneg_osc, plomoneg_cla)
    cara9 = cv2.inRange(hvs, negro_osc, negro_cla)
    cara10 = cv2.inRange(hvs, amarillo_osc, amarillo_cla)

    cnst1 = cv2.findContours(cara1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnst1 = imutils.grab_contours(cnst1)

    cnst2 = cv2.findContours(cara2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnst2 = imutils.grab_contours(cnst2)

    cnst3 = cv2.findContours(cara3, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnst3 = imutils.grab_contours(cnst3)

    cnst4 = cv2.findContours(cara4, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnst4 = imutils.grab_contours(cnst4)

    cnst5 = cv2.findContours(cara5, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnst5 = imutils.grab_contours(cnst5)

    cnst6 = cv2.findContours(cara6, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnst6 = imutils.grab_contours(cnst6)

    cnst7 = cv2.findContours(cara7, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnst7 = imutils.grab_contours(cnst7)

    cnst8 = cv2.findContours(cara8, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnst8 = imutils.grab_contours(cnst8)

    cnst9 = cv2.findContours(cara9, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnst9 = imutils.grab_contours(cnst9)

    cnst10 = cv2.findContours(cara10, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnst10 = imutils.grab_contours(cnst10)

    for c in cnst1:
        area1 = cv2.contourArea(c)
        if area1>5000:
            cv2.drawContours(frame, [c], 0, (255, 0, 0), 3)
            M = cv2.moments(c)
            cx = int(M["m10"]/M["m00"])
            cy = int(M["m01"] / M["m00"])

            cv2.circle(frame, (cx, cy), 7, (0, 255, 0), -1)
            cv2.putText(frame, "azul oscuro", (cx-20, cy-20), cv2.FONT_ITALIC, 2, (255, 255, 255), 2)


            cursorInsert = conexionc.con.conexion.cursor()
            consulta = "INSERT INTO dbo.coloresDatos(clr_name) VALUES ('azul oscuro');"
            cursorInsert.execute(consulta)
            cursorInsert.commit()
            cursorInsert.close()

            datosjson = {1: 'azul oscuro'}
            with open('datos.json', 'w') as fp:
                json.dump(datosjson, fp, indent=4, sort_keys=True)

    for c in cnst2:
        area2 = cv2.contourArea(c)
        if area2>5000:
            cv2.drawContours(frame, [c], -1, (0, 196, 255), 3)
            M = cv2.moments(c)
            cx = int(M["m10"]/M["m00"])
            cy = int(M["m01"] / M["m00"])

            cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
            cv2.putText(frame, "naranja", (cx-20, cy-20), cv2.FONT_ITALIC, 2, (255, 255, 255), 2)

            cursorInsert = conexionc.con.conexion.cursor()
            consulta = "INSERT INTO dbo.coloresDatos(clr_name) VALUES ('naranja');"
            cursorInsert.execute(consulta)
            cursorInsert.commit()
            cursorInsert.close()

            datosjson = {2: 'naranja'}
            with open('datos.json', 'w') as fp:
                json.dump(datosjson, fp, indent=4, sort_keys=True)

    for c in cnst3:
        area3 = cv2.contourArea(c)
        if area3>5000:
            cv2.drawContours(frame, [c], -1, (0, 255, 0), 3)
            M = cv2.moments(c)
            cx = int(M["m10"]/M["m00"])
            cy = int(M["m01"] / M["m00"])

            cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
            cv2.putText(frame, "plomo", (cx-20, cy-20), cv2.FONT_ITALIC, 2, (255, 255, 255), 2)

            cursorInsert = conexionc.con.conexion.cursor()
            consulta = "INSERT INTO dbo.coloresDatos(clr_name) VALUES ('plomo');"
            cursorInsert.execute(consulta)
            cursorInsert.commit()
            cursorInsert.close()

            datosjson = {3: 'plomo'}
            with open('datos.json', 'w') as fp:
                json.dump(datosjson, fp, indent=4, sort_keys=True)

    for c in cnst4:
        area4 = cv2.contourArea(c)
        if area4>5000:
            cv2.drawContours(frame, [c], -1, (255, 0, 0), 3)
            M = cv2.moments(c)
            cx = int(M["m10"]/M["m00"])
            cy = int(M["m01"] / M["m00"])

            cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
            cv2.putText(frame, "verde", (cx-20, cy-20), cv2.FONT_ITALIC, 2, (255, 255, 255), 2)

            cursorInsert = conexionc.con.conexion.cursor()
            consulta = "INSERT INTO dbo.coloresDatos(clr_name) VALUES ('verde');"
            cursorInsert.execute(consulta)
            cursorInsert.commit()
            cursorInsert.close()

            datosjson = {4: 'verde'}
            with open('datos.json', 'w') as fp:
                json.dump(datosjson, fp, indent=4, sort_keys=True)

    for c in cnst5:
        area5 = cv2.contourArea(c)
        if area5>5000:
            cv2.drawContours(frame, [c], -1, (255, 0, 0), 3)
            M = cv2.moments(c)
            cx = int(M["m10"]/M["m00"])
            cy = int(M["m01"] / M["m00"])

            cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
            cv2.putText(frame, "rosa", (cx-20, cy-20), cv2.FONT_ITALIC, 2, (255, 255, 255), 2)

            cursorInsert = conexionc.con.conexion.cursor()
            consulta = "INSERT INTO dbo.coloresDatos(clr_name) VALUES ('rosa');"
            cursorInsert.execute(consulta)
            cursorInsert.commit()
            cursorInsert.close()

            datosjson = {5: 'rosa'}
            with open('datos.json', 'w') as fp:
                json.dump(datosjson, fp, indent=4, sort_keys=True)

    for c in cnst6:
        area6 = cv2.contourArea(c)
        if area6>5000:
            cv2.drawContours(frame, [c], -1, (255, 0, 0), 3)
            M = cv2.moments(c)
            cx = int(M["m10"]/M["m00"])
            cy = int(M["m01"] / M["m00"])

            cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
            cv2.putText(frame, "celeste", (cx-20, cy-20), cv2.FONT_ITALIC, 2, (255, 255, 255), 2)

            cursorInsert = conexionc.con.conexion.cursor()
            consulta = "INSERT INTO dbo.coloresDatos(clr_name) VALUES ('celeste');"
            cursorInsert.execute(consulta)
            cursorInsert.commit()
            cursorInsert.close()

            datosjson = {6: 'cleste'}
            with open('datos.json', 'w') as fp:
                json.dump(datosjson, fp, indent=4, sort_keys=True)

    for c in cnst7:
        area7 = cv2.contourArea(c)
        if area7>5000:
            cv2.drawContours(frame, [c], -1, (0, 0, 255), 3)
            M = cv2.moments(c)
            cx = int(M["m10"]/M["m00"])
            cy = int(M["m01"] / M["m00"])

            cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
            cv2.putText(frame, "rojo", (cx-20, cy-20), cv2.FONT_ITALIC, 2, (255, 255, 255), 2)

            cursorInsert = conexionc.con.conexion.cursor()
            consulta = "INSERT INTO dbo.coloresDatos(clr_name) VALUES ('rojo');"
            cursorInsert.execute(consulta)
            cursorInsert.commit()
            cursorInsert.close()

            datosjson = {7: 'rojo'}
            with open('datos.json', 'w') as fp:
                json.dump(datosjson, fp, indent=4, sort_keys=True)

    for c in cnst8:
        area8 = cv2.contourArea(c)
        if area8>5000:
            cv2.drawContours(frame, [c], -1, (255, 0, 0), 3)
            M = cv2.moments(c)
            cx = int(M["m10"]/M["m00"])
            cy = int(M["m01"] / M["m00"])

            cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
            cv2.putText(frame, "plomoneg", (cx-20, cy-20), cv2.FONT_ITALIC, 2, (255, 255, 255), 2)

            cursorInsert = conexionc.con.conexion.cursor()
            consulta = "INSERT INTO dbo.coloresDatos(clr_name) VALUES ('plomoneg');"
            cursorInsert.execute(consulta)
            cursorInsert.commit()
            cursorInsert.close()

            datosjson = {8: 'plomoneg'}
            with open('datos.json', 'w') as fp:
                json.dump(datosjson, fp, indent=4, sort_keys=True)

    for c in cnst9:
        area9 = cv2.contourArea(c)
        if area9>5000:
            cv2.drawContours(frame, [c], -1, (255, 0, 0), 3)
            M = cv2.moments(c)
            cx = int(M["m10"]/M["m00"])
            cy = int(M["m01"] / M["m00"])

            cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
            cv2.putText(frame, "negro", (cx-20, cy-20), cv2.FONT_ITALIC, 2, (255, 255, 255), 2)

            cursorInsert = conexionc.con.conexion.cursor()
            consulta = "INSERT INTO dbo.coloresDatos(clr_name) VALUES ('negro');"
            cursorInsert.execute(consulta)
            cursorInsert.commit()
            cursorInsert.close()

            datosjson = {9: 'negro'}
            with open('datos.json', 'w') as fp:
                json.dump(datosjson, fp, indent=4, sort_keys=True)


    for c in cnst10:
        area10 = cv2.contourArea(c)
        if area10>5000:
            cv2.drawContours(frame, [c], 0, (255, 0, 0), 3)
            M = cv2.moments(c)
            cx = int(M["m10"]/M["m00"])
            cy = int(M["m01"] / M["m00"])

            cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
            cv2.putText(frame, "amarillo", (cx-20, cy-20), cv2.FONT_ITALIC, 2, (255, 255, 255), 2)

            cursorInsert = conexionc.con.conexion.cursor()
            consulta = "INSERT INTO dbo.coloresDatos(clr_name) VALUES ('amarillo');"
            cursorInsert.execute(consulta)
            cursorInsert.commit()
            cursorInsert.close()

            datosjson = {10: 'amarillo'}
            with open('datos.json', 'w') as fp:
                json.dump(datosjson, fp, indent=4, sort_keys=True)


    cv2.imshow("video", frame)
    k = cv2.waitKey(1)
    if k == 27:
        break

#conexion()
cap.release()
cv2.destroyAllWindows()
