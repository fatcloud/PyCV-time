import cv2
import numpy as np
from cam import OpenCV_Cam


if __name__ == '__main__':

    cam = OpenCV_Cam()
    w,h = cam.size
    cam.set('EXPOSURE', 0)
    dst = np.full((h, w, 3), 0, dtype=np.uint8)
    
    exp_list = range(-2, -9, -1)
    ratio = 1.0 / len(exp_list)
    for e in exp_list:
        cam.set('EXPOSURE', e)
        img = None
        while img is None:
            img = cam.read()
        dst = cv2.addWeighted(dst, 1.0, img, ratio,0)
        
        cv2.imshow(str(e), img)
        cv2.imshow('dst'+str(e), dst)
        cv2.waitKey(10)
    
    cv2.imshow('mix', dst)
    
    k = cv2.waitKey(0)