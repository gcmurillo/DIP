'''''''''''''''''''''''''''''''''''''''''''''
        PROCESAMIENTO DIGITAL DE IMÁGENES

                LABORATORIO 7
       TRANSFORMADA DE FOURIER CON OPENCV
'''''''''''''''''''''''''''''''''''''''''''''

import cv2
import numpy as np
from matplotlib import pyplot as plt


def inputImg():
    img = None
    while(True):
        ruta = input("\n\tIngrese ruta de la imagen: ")
        img = cv2.imread(ruta,0)
        if (type(img)!=type(None)):
            return img
        else:
            print("\n\tNo se pudo abrir la imagen.\n")

    #return img


while(True):
    print("\n\n************************************************************")
    print("\n\t\tPROCESAMIENTO DIGITAL DE IMÁGENES")
    print("\n\t\t    TRANSFORMADA DE FOURIER")
    print("\n\n************************************************************")

    img = inputImg()   #carga imagen de entrada
    cv2.imshow("Img",img)
    cv2.waitKey(0)
    
    img_float32 = np.float32(img)       #mapea imagen de entrada a 32 bits/pixel

    dft = cv2.dft(img_float32, flags = cv2.DFT_COMPLEX_OUTPUT)    #calcula la transf. Fourier 
    dft_shift = np.fft.fftshift(dft)    #proyecta los cuadrantes de la imagen 

    magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))    #encuentra la magnitud, usa mapeo logaritmico y absoluto de la imagen real e imaginaria

    plt.subplot(121),plt.imshow(img, cmap = 'gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
    plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    plt.show()   
