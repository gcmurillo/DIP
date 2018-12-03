
import cv2
import numpy as np
from matplotlib import pyplot as plt

nombres = ['original', 'suavizada', 'ruido', 'trasladada', 'perfilada', 'rotada', 'reducida']

for i in range(0, len(nombres)):
    img = cv2.imread(str(i+1) + '.jpg',0)
    
    
    f = np.fft.fft2(img)
    #Se centran los valores de frecuencia al eje 0
    fshift = np.fft.fftshift(f)
    
    magnitude_spectrum = 20*np.log(np.abs(fshift))
    '''
    img_float32 = np.float32(img)       #mapea imagen de entrada a 32 bits/pixel

    dft = cv2.dft(img_float32, flags = cv2.DFT_COMPLEX_OUTPUT)    #calcula la transf. Fourier 
    dft_shift = np.fft.fftshift(dft)    #proyecta los cuadrantes de la imagen 

    magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))    #encuentra la magnitud, usa mapeo logaritmico y absoluto de la imagen real e imaginaria
    '''

    plt.subplot(1,2,1),plt.imshow(img, cmap = 'gray')
    plt.title(nombres[i]), plt.xticks([]), plt.yticks([])
    plt.subplot(1,2,2),plt.imshow(magnitude_spectrum, cmap = 'gray')
    plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    plt.show()   