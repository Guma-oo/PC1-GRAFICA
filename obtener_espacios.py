import cv2
import pickle

video = cv2.VideoCapture('video.mp4')
check, img = video.read()

if not check:
    print('No se pudo leer video.mp4')
    exit()

espacios = []

for i in range(10):
    espacio = cv2.selectROI('Seleccionar entradas - ENTER para guardar, C para terminar', img, False)
    cv2.destroyWindow('Seleccionar entradas - ENTER para guardar, C para terminar')

    if espacio == (0, 0, 0, 0):
        break

    espacios.append(espacio)

    for x, y, w, h in espacios:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,255), 2)

with open('espacios.pkl', 'wb') as file:
    pickle.dump(espacios, file)

print('Entradas guardadas:', len(espacios))
cv2.destroyAllWindows()