'''
find_parallelograms.py
=========
Spot all the pentagon by webcam

Usage
-----
python find_parallelograms.py

'''


import numpy as np
from numpy import linalg as LA

import cv2
from cam import OpenCV_Cam


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
    contours = [ctr for ctr in contours if cv2.contourArea(ctr) > 400]
    contours = [cv2.approxPolyDP(ctr, 3 , True) for ctr in contours]
    contours = [ctr for ctr in contours if len(ctr) == 5]
    parallelograms = find_milkbox(contours)
        
    # ============================================
    
    # draw on the frame
    cv2.drawContours(frame, parallelograms, -1, (0,255,0), 3)
    
    return frame

    
def find_milkbox(contours):
    pentagons = []
    for ctr in contours:
        vecs = zip(ctr, np.roll(ctr, 1))
        normalized_vecs = []
        for vec in vecs: 
            length = LA.norm(vec[0] - vec[1])
            norm_vec = (vec[0] - vec[1]) / length
            normalized_vecs.append(norm_vec)
        
        paired_vecs = zip(normalized_vecs, np.roll(normalized_vecs, 2))
        count = 0
        for pair in paired_vecs:
            angle = np.inner(pair[0], pair[1])
            if angle < 0.05:
                count = count + 1
        if count != 2:
            continue

        pentagons.append(ctr)
        
    return pentagons

    
if __name__ == "__main__":
    cam = OpenCV_Cam()
    cam.cam_loop(contour_proc)
