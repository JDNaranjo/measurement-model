import cv2
import numpy as np
from object_detector import *
from matplotlib import pyplot as plt

im = cv2.imread('./script_picture/images/test2.jpg')

parametros = cv2.aruco.DetectorParameters_create()
diccionario = cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_1000)

detector = DetectorFondoHomogeneo()

#plt.figure(figsize=(20, 20))
#imgplot = plt.imshow(im, interpolation='nearest')
# plt.show()

#im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

esquinas, ids, rejectedImgPoints = cv2.aruco.detectMarkers(
    im, diccionario, parameters=parametros)

print(esquinas)

if ids is not None:
    print('detected: {}'.format(len(ids)))
    # for i, corner in zip(ids, corners):
    # print('ID: {}; Corners: {}'.format(i, corner))

    im = cv2.aruco.drawDetectedMarkers(im, esquinas, borderColor=(255, 0, 0))
else:
    print("NONE")

#plt.figure(figsize=(20, 20))
#imgplot = plt.imshow(im, interpolation='nearest')
# plt.show()

print(esquinas)
esquinas_ent = np.int0(esquinas)
cv2.polylines(im, esquinas_ent, True, (0, 0, 255), 5)
print(esquinas_ent)
perimetro_aruco = cv2.arcLength(esquinas_ent[0], True)
print("perimetro aruco:")
print(perimetro_aruco)

proporcion_cm = perimetro_aruco / 16

# while True:

contornos = detector.deteccion_objetos(im)
print(contornos)

for con in contornos:
    rectangulo = cv2.minAreaRect(con)
    (x, y), (an, al), angulo = rectangulo

    ancho = an / proporcion_cm
    alto = al / proporcion_cm

    cv2.circle(im, (int(x), int(y)), 5, (255, 255, 0), -1)

    rect = cv2.boxPoints(rectangulo)
    rect = np.int0(rect)

    cv2.polylines(im, [rect], True, (0, 255, 0), 2)

    cv2.putText(im, "Ancho: {} cm".format(
        round(ancho, 1)), (int(x), int(y-15)), cv2.LINE_AA, 0.8, (150, 0, 255), 2)

    cv2.putText(im, "Largo: {} cm".format(
        round(alto, 1)), (int(x), int(y+15)), cv2.LINE_AA, 0.8, (75, 0, 75), 2)

    cv2.namedWindow("Hola", cv2.WINDOW_NORMAL)
    cv2.imshow('Hola', im)
    cv2.waitKey(0)

    # if t == 27:
    #    break
"""

# Cargar el detector
detector = DetectorFondoHomogeneo()

cap = cv2.VideoCapture(1)
cap.set(3, 640)
cap.set(4, 480)


while True:

    ret, frame = cap.read()
    if ret == False:
        break
    cv2.imwrite(
        'D:/Universidad/S9/PdG/workspace/script_picture/images/cap2.png', frame)

    esquinas, _, _ = cv2.aruco.detectMarkers(
        im, diccionario, parameters=parametros)

    print(esquinas)
    esquinas_ent = np.int0(esquinas)
    cv2.polylines(frame, esquinas_ent, True, (0, 0, 255), 5)
    print(esquinas_ent)
    perimetro_aruco = cv2.arcLength(esquinas_ent[0], True)

    proporcion_cm = perimetro_aruco / 16

# Detectar los objetos
    contornos = detector.deteccion_objetos(frame)

    for con in contornos:
        rectangulo = cv2.minAreaRect(con)
        (x, y), (an, al), angulo = rectangulo

        ancho = an / proporcion_cm
        alto = al / proporcion_cm

        #cv2.circle(frame, (int(x), int(y)), 5, (255, 255, 0), -1)

        rect = cv2.boxPoints(rectangulo)
        rect = np.int0(rect)

        cv2.polylines(frame, [rect], True, (0, 255, 0), 2)

        # cv2.putText(frame, "Ancho: {} cm".format(
        #    round(ancho, 1)), (int(x), int(y-15)), cv2.LINE_AA, 0.8, (150, 0, 255), 2)

        # cv2.putText(frame, "Largo: {} cm".format(
        #    round(alto, 1)), (int(x), int(y+15)), cv2.LINE_AA, 0.8, (75, 0, 75), 2)

    cv2.imshow('Medicion de Objetos', frame)

    t = cv2.waitKey(1)
    if t == 27:
        break

cap.release()
cv2.destroyAllWindows()
"""
