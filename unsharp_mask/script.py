import cv2
import numpy as np
from matplotlib import pyplot as plt

def unsharp_mask(img_name, k=0.2):
    img = cv2.imread(img_name)
    blur = cv2.blur(img, (3,3))  # applying low pass filter
    smooth = img - blur
    sharp = img + float(k) * smooth
    sharp = np.maximum(sharp, np.zeros(sharp.shape))  # eliminar valores extremos
    sharp = np.minimum(sharp, 255 * np.ones(sharp.shape))
    sharp  = sharp.round().astype(np.uint8)
    return sharp

def unsharp_mask2(img_name, kernel_size=(5, 5), sigma=1.0, amount=1.0, threshold=0):
    """Return a sharpened version of the image, using an unsharp mask."""
    # For details on unsharp masking, see:
    # https://en.wikipedia.org/wiki/Unsharp_masking
    # https://homepages.inf.ed.ac.uk/rbf/HIPR2/unsharp.htm
    image = cv2.imread(img_name)
    blurred = cv2.GaussianBlur(image, kernel_size, sigma)
    sharpened = float(amount + 1) * image - float(amount) * blurred
    sharpened = np.maximum(sharpened, np.zeros(sharpened.shape))
    sharpened = np.minimum(sharpened, 255 * np.ones(sharpened.shape))
    sharpened = sharpened.round().astype(np.uint8)
    if threshold > 0:
        low_contrast_mask = np.absolute(image - blurred) < threshold
        np.copyto(sharpened, image, where=low_contrast_mask)
    return sharpened


img = cv2.imread('foto.png')
filtered = unsharp_mask('foto.png')

cv2.imshow('foto', filtered)
cv2.imshow('foto ori', img)
cv2.waitKey(0)

'''
plt.subplot(1,3,1),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])

plt.subplot(1,3,2),plt.imshow(filtered, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    
plt.subplot(1,3,3),plt.imshow(filtered, cmap = 'gray')
plt.title('Mask'), plt.xticks([]), plt.yticks([])
plt.show()  
'''