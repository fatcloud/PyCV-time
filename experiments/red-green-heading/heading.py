import cv2
import numpy as np

from numpy import linalg as LA
from cam import OpenCV_Cam
from shape_utils import *
from get_color_mask import *


def contour_proc(frame, debug=False):
    pass
    '''
    
    # draw all the contours
    cpframe = frame.copy()
    cv2.drawContours(cpframe, contours, -1, (0,255,0), 3)
    if debug: cv2.imshow('cpframe', cpframe)
    
    # ================== TODO ===================
    
    # Modify these code to suit your need
    

    circles = find_circles(contours, 0)
    
    # ============================================
    
    # draw on the frame
    cv2.drawContours(frame, circles, -1, (0,255,0), 3)    
    return frame
    '''



if __name__ == '__main__':

    cam = OpenCV_Cam()

    r_bound = ([-5, 150, 0], [15, 255, 255])
    g_bound = ([80, 100, 0], [105, 255, 255])

    while True:
        
        image = cam.read()
        r_mask = get_mask(image, *r_bound, blur=3)
        g_mask = get_mask(image, *g_bound, blur=3)

        r_ctr, r_hry = cv2.findContours(r_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        g_ctr, g_hry = cv2.findContours(g_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        r_ctr = [ctr for ctr in r_ctr if is_circle(ctr)]
        
        masks = cv2.bitwise_or(r_mask, g_mask)
        
        output = cv2.bitwise_and(image, image, mask = masks)
        cv2.drawContours(output, r_ctr, -1, (0,0,255), 3)


        # show the images
        cv2.imshow("images", np.hstack([image, output]))
        k = cv2.waitKey(10)
        if k == 27:
            break