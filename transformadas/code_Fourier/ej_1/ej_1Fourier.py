
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
    print("\n\t\t    ELIMINAR RUIDO REPETITIVO ")
    print("\n\n************************************************************")

    img = inputImg()   #carga imagen de entrada
    
    img_float32 = np.float32(img)       #mapea imagen de entrada a 32 bits/pixel

    mask = np.zeros((img.shape[0],img.shape[1], 2), np.uint8)  # Crea la mascara con dos canales
    mask[:,:] = 1  # colocamos fondo blanco a la mascara
    mask[ 0:img.shape[0], 80:90] = 0  # dibujamos rectangulos segun el espectro
    mask[0:img.shape[0], 170:180] = 0

    dft = cv2.dft(img_float32, flags = cv2.DFT_COMPLEX_OUTPUT)    #calcula la transf. Fourier 
    dft_shift = np.fft.fftshift(dft)    #proyecta los cuadrantes de la imagen 

    # Aplicar la mascara y aplicar la transformada inversa
    fshift = dft_shift*mask
    f_ishift = np.fft.ifftshift(fshift)
    img_back = cv2.idft(f_ishift)
    img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])

    print('Img height:', img.shape[0])
    print('Img width:', img.shape[1])

    plt.subplot(121),plt.imshow(img, cmap = 'gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img_back, cmap = 'gray')
    plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    plt.show()   
    