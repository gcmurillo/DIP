''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''                     LABORATORIO 5 - PARTE 1
     DETECCIÓN DE ROSTROS Y SUS CARACTERÍSTICAS - USANDO HAARCASCADE
                   PROCESAMIENTO DIGITAL DE IMÁGENES
'''            
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import cv2

#Archivos de haarcascade para caracteristicas de...
    #detección de rostros
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    #detección de ojos
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    #detección de boca
mouth_cascade = cv2.CascadeClassifier('haarcascade_mcs_mouth.xml')
    #detección de nariz
nose_cascade = cv2.CascadeClassifier('haarcascade_mcs_nose.xml')


capture = cv2.VideoCapture(0)   #captura señal de video de cámara

cv2.namedWindow("CAPTURE", cv2.WINDOW_AUTOSIZE)

while(True):
    #Lectura del frame
    ret, frame = capture.read()

    #Convertir a escala de grises
    frameGris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Deteccion de rostro
    faces = face_cascade.detectMultiScale(frameGris, 1.1, 5)

    for (x,y,w,h) in faces:     #x,y posición TL del box del rostro, w es ancho, h es alto
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)    #dibuja rectangulo del rostro detectado - color Azul

        #Extrae ROI del rostro detectado
        roi_gray = frameGris[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        #Detección de ojos a partir de ROI extraido
        eyes = eye_cascade.detectMultiScale(roi_gray)
        
        for (ex,ey,ew,eh) in eyes:  #ex,ey posición TL del box del ojo, ew es ancho, eh es alto
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)  #dibuja rectangulo del ojo detectado  - color Verde

        #Detección de boca a partir de ROI extraido
        bocas = mouth_cascade.detectMultiScale(roi_gray)

        for (mx,my,mw,mh) in bocas:
            cv2.rectangle(roi_color,(mx,my),(mx+mw,my+mh),(0,0,255),2)  #dibuja rectangulo de boca detectada  - color Rojo

        #Deteccion de nariz a partir de ROI extraido
        narices = nose_cascade.detectMultiScale(roi_gray)

        for (nx,ny,nw,nh) in narices:
            cv2.rectangle(roi_color,(nx,ny),(nx+nw,ny+nh),(255,255,255),2)  #dibuja rectangulo de nariz detectada  - color Blanco

    #Muestra el video resultante con el rostro y sus características detectadas
    cv2.imshow("CAPTURE",frame)

    key = cv2.waitKey(33) #Retraso en milisegundos para leer el siguiente frame
    #Termina presionando la tecla Esc
    if (key==27):
        break

capture.release()
cv2.destroyAllWindows()
