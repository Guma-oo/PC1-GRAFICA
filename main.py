import cv2
import pickle
import numpy as np

entradas = []

with open('espacios.pkl', 'rb') as file:
    entradas = pickle.load(file)

video = cv2.VideoCapture('video.mp4')

fases = [0] * len(entradas)
libres = [0] * len(entradas)
conteos = [0] * len(entradas)

while True:
    check, img = video.read()

    if not check:
        break

    imgBN = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBN = cv2.GaussianBlur(imgBN, (5, 5), 0)
    imgTH = cv2.adaptiveThreshold(imgBN,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,51,20)
    imgMedian = cv2.medianBlur(imgTH, 7)
    kernel = np.ones((3, 3), np.uint8)
    imgDil = cv2.dilate(imgMedian,kernel,iterations=1)
    for i, (x, y, w, h) in enumerate(entradas):

        if i == 2:
            mitad = w // 2
            zonaEntrada = imgDil[y:y+h,x:x+mitad]
            zonaAntes = imgDil[y:y+h,x+mitad:x+w]

        else:
            mitad = h // 2
            zonaAntes = imgDil[y:y+mitad,x:x+w]
            zonaEntrada = imgDil[y+mitad:y+h,x:x+w]

        # Cantidad de pixeles blancos
        countAntes = cv2.countNonZero(zonaAntes)
        countEntrada = cv2.countNonZero(zonaEntrada)

        # Porcentajes diferentes para cada entrada
        if i == 0:
            porcentaje = 0.25

        elif i == 1:
            porcentaje = 0.10

        else:
            porcentaje = 0.15

        # Limites
        if i == 2:
            limiteAntes = int(mitad * h * porcentaje )
            limiteEntrada = int((w - mitad) * h * porcentaje)

        else:

            limiteAntes = int(w * mitad * porcentaje)
            limiteEntrada = int(w * (h - mitad) * porcentaje)

        antes = countAntes > limiteAntes
        entro = countEntrada > limiteEntrada

        # Estados
        if fases[i] == 0:

            if antes and not entro:
                fases[i] = 1

        elif fases[i] == 1:

            if entro:
                conteos[i] += 1
                fases[i] = 2

        elif fases[i] == 2:

            if not antes and not entro:

                libres[i] += 1

                if libres[i] > 5:
                    fases[i] = 0
                    libres[i] = 0

            else:
                libres[i] = 0

        if antes or entro:
            color = (0, 0, 255)
        else:
            color = (0, 255, 0)

        cv2.rectangle(img, (x, y),(x+w, y+h),color,2)

        if i == 2:

            cv2.line( img,(x+mitad, y),(x+mitad, y+h),(255, 0, 255),2)

        else:

            cv2.line(img,(x, y+mitad),(x+w, y+mitad),(255, 0, 255),2)

  
        cv2.putText( img,'Entrada ' + str(i+1) + ': ' + str(conteos[i]),(x, y-8),cv2.FONT_HERSHEY_SIMPLEX,0.6,color,2)

    cv2.putText(img,str(countAntes) + ' / ' + str(countEntrada),(x, y+h-10),cv2.FONT_HERSHEY_SIMPLEX,0.4,(255, 255, 0),1)
    total = sum(conteos)
    cv2.putText(img,'TOTAL ENTRADAS: ' + str(total),(20, 40), cv2.FONT_HERSHEY_SIMPLEX,1,(255, 255, 0),2)
    cv2.imshow('video', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()