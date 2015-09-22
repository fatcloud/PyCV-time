import cv2
import numpy as np

from numpy import linalg as LA
from cam import OpenCV_Cam
from shape_utils import *
from get_color_mask import *


def contour_proc(frame, debug=False):
    
    # convert color to gray scale and show it
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if debug: cv2.imshow('gray', gray)
    
    # blur the result from edge detection to ensure continuity
    edge = cv2.Canny(gray, 30, 100)
    edge = cv2.blur(edge, (2,2))
    if debug: cv2.imshow('blured edge', edge)
    
    
    # convert image to black and white and show it
    thresh1, thresh = cv2.threshold(edge, 60, 255, cv2.THRESH_BINARY)
    if debug: cv2.imshow('thresh', thresh)
    
    # find contours!
    contours, hry = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
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


    
if __name__ == '__main__':

    cam = OpenCV_Cam()

    red_bound = ([-5, 150, 0], [15, 255, 255])
    green_bound = ([80, 100, 0], [105, 255, 255])

    while True:
        
        image = cam.read()
        red_mask   = get_mask(image, *red_bound)
        green_mask = get_mask(image, *green_bound)

        masks = cv2.bitwise_or(red_mask, green_mask)

        cv2.imshow('masks', np.hstack([red_mask, green_mask]))

        output = cv2.bitwise_and(image, image, mask = masks)
     
        # show the images
        cv2.imshow("images", np.hstack([image, output]))
        k = cv2.waitKey(10)
        if k == 27:
            break