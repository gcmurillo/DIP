
import cv2
import numpy as np
import glob

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# Esquinas internas a lo ancho del tablero
numCornersHor = int(input("Enter number of inner corners along width: ")) 

# Esquinas internas a lo largo del tablero
numCornersVer = int(input("Enter number of inner corners along height: "))

numSquares = numCornersHor * numCornersVer
board_sz = (numCornersHor, numCornersVer)

object_points = []
image_points = []
corners = []

cv2.namedWindow("img", cv2.WINDOW_NORMAL)

# capture = cv2.VideoCapture(0)
# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((numCornersHor*numCornersVer,3), np.float32)
objp[:,:2] = np.mgrid[0:numCornersHor,0:numCornersVer].T.reshape(-1,2)

images = glob.glob('./fotos/*.jpg')
print("Cantidad de imagenes: ", len(images))
for fname in images:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("img", gray)
    cv2.waitKey(0)

    
    ret, corners = cv2.findChessboardCorners(gray, board_sz, None)

    if ret:
        object_points.append(objp)

        cv2.cornerSubPix(gray, corners, (11,11), board_sz, criteria)
        image_points.append(corners)

        cv2.drawChessboardCorners(img, board_sz, corners, ret)
        cv2.imshow("img", img)
        cv2.waitKey(0)

cv2.destroyAllWindows()

# it returns the camera matrix, distortion coefficients, rotation and translation vectors etc.
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(object_points, image_points, gray.shape[::-1],None,None)

# it returns undistorted image with minimum unwanted pixels. So it may even remove some pixels at image corners
img = cv2.imread('image.jpg')
h,w = img.shape[:2]
newcameramtx, roi=cv2.getOptimalNewCameraMatrix(mtx,dist,(w,h),1,(w,h))

# undistort
dst = cv2.undistort(img, mtx, dist, None, newcameramtx)

# crop the image
x,y,w,h = roi
dst = dst[y:y+h, x:x+w]
cv2.imwrite('calibresult.png',dst)
