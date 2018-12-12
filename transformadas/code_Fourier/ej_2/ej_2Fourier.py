
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

    plt.subplot(1,2,1),plt.imshow(img, cmap = 'gray')
    plt.title(nombres[i]), plt.xticks([]), plt.yticks([])
    plt.subplot(1,2,2),plt.imshow(magnitude_spectrum, cmap = 'gray')
    plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    plt.show()   