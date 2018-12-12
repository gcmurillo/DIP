
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

    dft = cv2.dft(img_float32, flags = cv2.DFT_COMPLEX_OUTPUT)    #calcula la transf. Fourier 
    dft_shift = np.fft.fftshift(dft)    #proyecta los cuadrantes de la imagen 

    magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))    #encuentra la magnitud, usa mapeo logaritmico y absoluto de la imagen real e imaginaria

    ret, mag = cv2.threshold(magnitude_spectrum, 180, 190, cv2.THRESH_BINARY)
    mask2 = np.zeros((img.shape[0],img.shape[1], 2), np.uint8)  # Crea la mascara con dos canales
    mask2[:,:,0] = 1  # colocamos fondo blanco a la mascara
    mask2[:,:,1] = 1  # colocamos fondo blanco a la mascara


    mask = np.zeros((img.shape[0],img.shape[1], 3), np.uint8)  # Crea la mascara con dos canales
    mask[:,:] = (255,255,255)  # colocamos fondo blanco a la mascara

    ret, binary_mask = cv2.threshold(mask2, 180, 190, cv2.THRESH_BINARY)

    for j in range(mag.shape[1]):
        # print(mag[mag.shape[0]//2][j])
        if mag[mag.shape[0]//2][j] == 190:
            right = j
            break

    
    for j in range(mag.shape[1], 0 , -1):
        # print(mag[i][j])
        if mag[mag.shape[0]//2][mag.shape[1] - j] == 190:
            left = j
            break
    
    print(right)
    print(left)
    mask2[0:img.shape[0], right:right+10] = 0
    mask2[0:img.shape[0], left-10:left] = 0
    
    mask[0:img.shape[0], right:right+10] = (0,0,0)
    mask[0:img.shape[0], left-10:left] = (0,0,0)

    # Aplicar la mascara y aplicar la transformada inversa
    dft_shift = dft_shift*mask2
    '''
    dft_shift[0:img.shape[0], right:right+10,0] = 0
    dft_shift[0:img.shape[0], left-10:left,0] = 0
    dft_shift[0:img.shape[0], right:right+10,1] = 0
    dft_shift[0:img.shape[0], left-10:left,1] = 0
    '''
    f_ishift = np.fft.ifftshift(dft_shift)
    img_back = cv2.idft(f_ishift)
    img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])

    product = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1])) 
    product[np.isneginf(product)] = 0  # cambiando -inf por 0

    print(product[0:img.shape[0], right:right+10])
    
    plt.subplot(1,5,1),plt.imshow(img, cmap = 'gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])

    plt.subplot(1,5,2),plt.imshow(magnitude_spectrum, cmap = 'gray')
    plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    
    plt.subplot(1,5,3),plt.imshow(mask, cmap = 'gray')
    plt.title('Mask'), plt.xticks([]), plt.yticks([])

    plt.subplot(1,5,4),plt.imshow(product, cmap = 'gray')
    plt.title('Product'), plt.xticks([]), plt.yticks([])
    
    plt.subplot(1,5,5),plt.imshow(img_back, cmap = 'gray')
    plt.title('Back'), plt.xticks([]), plt.yticks([])
    plt.show()   
    