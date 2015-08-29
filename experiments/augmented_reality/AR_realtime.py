"""
usage: >>>python AR_realtime.py

This program tries to detect chessboard from camera image
and draw axis in real-time

In case the camera matrix file "camera_parameters.npz" does not exist,
run calibration example to generate one
"""

import cv2
import numpy as np
import glob
from time import sleep
# Load previously saved data
with np.load('camera_parameters.npz') as X:
    mtx, dist, _, _ = [X[i] for i in ('mtx','dist','rvecs','tvecs')]

    
print 'data loaded...'


def draw(img, corners, imgpts):
    corner = tuple(corners[0].ravel())
    cv2.line(img, corner, tuple(imgpts[0].ravel()), (255,0,0), 5)
    cv2.line(img, corner, tuple(imgpts[1].ravel()), (0,255,0), 5)
    cv2.line(img, corner, tuple(imgpts[2].ravel()), (0,0,255), 5)
    
    return img
    


shp = (8, 6)
    
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
objp = np.zeros((shp[1]*shp[0],3), np.float32)
objp[:,:2] = np.mgrid[0:shp[0],0:shp[1]].T.reshape(-1,2)

axis = np.float32([[3,0,0], [0,3,0], [0,0,-3]]).reshape(-1,3)


camera = cv2.VideoCapture(1)
if not camera.isOpened():
    camera = cv2.VideoCapture(0)

chbd = cv2.imread('chessboard.jpg')
cv2.imshow('chessboard', chbd)

print chbd.shape

while True:
    
    img = camera.read()[1]
    img = cv2.flip(img, 1)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret, corners = cv2.findChessboardCorners(gray, shp, None)

    if ret == True:
        cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)

        # Find the rotation and translation vectors.
        rvecs, tvecs, inliers = cv2.solvePnPRansac(objp, corners, mtx, dist)

        # project 3D points to image plane
        imgpts, jac = cv2.projectPoints(axis, rvecs, tvecs, mtx, dist)

        img = draw(img,corners,imgpts)  
    
    cv2.imshow('img',img)
    
    k = cv2.waitKey(5) & 0xff
    if k == 27:
        break
    elif k == ord('s'):
        cv2.imwrite('result.png', img)

cv2.destroyAllWindows()