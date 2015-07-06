
import cv2
import numpy as np
from webcam_gui import webcam_gui

def angle(p1, p2, p3):
    v1 = p1 - p2
    v2 = p3 - p2
    v1 = v1.astype(float)
    v2 = v2.astype(float)
    v1 = v1 / np.sqrt(np.dot(v1, v1))
    v2 = v2 / np.sqrt(np.dot(v2, v2))
    return np.degrees(np.arccos(np.dot(v1, v2)))
    

def isArrow(heptagon):
    hull = cv2.convexHull(heptagon, returnPoints = False)

    if len(hull) > 2:
        defects = cv2.convexityDefects(heptagon, hull)
        if defects is None or len(defects) != 2: 
            return False
      
        farpoints = [d[0][2] for d in defects]    
        if not np.abs(farpoints[0] - farpoints[1]) in [3, 4]:
            return False

        for defect in defects:
            s, e, f, d = defect[0]
            #    print defects
            #    s, e, f, d = defect[0]
            ps = heptagon[s, 0]
            pe = heptagon[e, 0]
            pd = heptagon[f, 0]
            if angle(ps, pd, pe) < 120:
                return True    

        return False

def tip(arrow):
    hull = cv2.convexHull(arrow, returnPoints = False)
    defects = cv2.convexityDefects(arrow, hull)
    farpoints = [d[0][2] for d in defects]
    if np.abs(farpoints[0] - farpoints[1]) == 4:
        return arrow[sum(farpoints) / 2, 0]
    else:
        return arrow[0, 0]


def imgproc(frame):
    
    # convert color to gray scale and show it
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray', gray)
    
    blur = cv2.blur(gray, (5,5))
    edge = cv2.Canny(blur, 10, 100)
    edge = cv2.blur(edge, (2,2))
    cv2.imshow('blured edge', edge)
    
    
    # convert image to black and white and show it
    thresh1, thresh = cv2.threshold(edge, 60, 120, cv2.THRESH_BINARY)
    cv2.imshow('thresh', thresh)
    
    # find contours!
    contours, hry = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # draw all the contours
    cpframe = frame.copy()
    cv2.drawContours(cpframe, contours, -1, (0,255,0), 3)
    cv2.imshow('cpframe', cpframe)
    
    # ================== TODO ===================
    
    # Modify these code to suit your need
    contours = [ctr for ctr in contours if cv2.contourArea(ctr) > 100]
    contours = [cv2.approxPolyDP(ctr, 5, True) for ctr in contours]
    heptagons = [ctr for ctr in contours if len(ctr) == 7]
    arrows = [hepta for hepta in heptagons if isArrow(hepta)]
    #tips = [ tip(a) for a in arrows ]
    
    #contours = [ctr for ctr in contours if cv2.isContourConvex(ctr)]
    
    # ============================================
    
    
    # draw on the frame
    #cv2.drawContours(frame, heptagons, -1, (0,255,0), 3)
    cv2.drawContours(frame, arrows, -1, (255, 0, 0), -1)
    # draw tips
    #for t in tips:
    #    cv2.circle(frame, tuple(t), 5, (0, 0, 255), -1)

    return frame

if __name__ == "__main__":
    webcam_gui(imgproc, 1)
