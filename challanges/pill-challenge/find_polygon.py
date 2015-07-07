
import cv2
from webcam_gui import webcam_gui

def imgproc(frame):
    
    # convert color to gray scale and show it
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray', gray)
    
    blur = cv2.blur(gray, (5,5))
    edge = cv2.Canny(blur, 30, 100)
    edge = cv2.blur(edge, (2,2))
    cv2.imshow('blured edge', edge)
    
    
    # convert image to black and white and show it
    thresh1, thresh = cv2.threshold(edge, 60, 255, cv2.THRESH_BINARY)
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
    contours = [cv2.approxPolyDP(ctr, 5 , True) for ctr in contours]
    contours = [ctr for ctr in contours if cv2.isContourConvex(ctr)]
    
    # ============================================
    
    
    # draw on the frame
    cv2.drawContours(frame, contours, -1, (0,255,0), 3)
    
    return frame

if __name__ == "__main__":
    webcam_gui(imgproc, video_src=1)