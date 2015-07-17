import numpy as np
import cv2
from webcam_gui import webcam_gui

def edge_filter(frame_in):
    # convert into gray scale
    frame_gray = cv2.cvtColor(frame_in, cv2.COLOR_BGR2GRAY)
    # blur the image to reduce noise
    frame_blur = cv2.blur(frame_gray, (3,3))
    # Canny edge detection
    frame_out = cv2.Canny(frame_blur, 30, 120)
    
    return frame_out
def threshold(frame_in,min):
    # blur the image to reduce noise
    frame_blur = cv2.blur(frame_in, (3,3))
    # threshold
    thresh1, thresh = cv2.threshold(frame_blur, min, 255, cv2.THRESH_BINARY)
    frame_out = thresh
    return frame_out 
def adap_threshold(frame_in):
    # blur the image to reduce noise
    frame_blur = cv2.blur(frame_in, (3,3))
    # threshold
    thresh = cv2.adaptiveThreshold(frame_blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
    frame_out = thresh
    return frame_out
def canny_filter(frame_in):
    # blur the image to reduce noise
    frame_blur = cv2.blur(frame_in, (3,3))
    # threshold
    canny = cv2.Canny(frame_blur,100,200)
    frame_out = canny
    return frame_out       
def gray_filter(frame_in):
    # convert into gray scale
    frame_out = cv2.cvtColor(frame_in, cv2.COLOR_BGR2GRAY)
    return frame_out
def angle_cos(p0, p1, p2):
    d1, d2 = (p0-p1).astype('float'), (p2-p1).astype('float')
    return abs( np.dot(d1, d2) / np.sqrt( np.dot(d1, d1)*np.dot(d2, d2) ) )
 
def equal(p0,p1,p2,tolerance):
    d1, d2 = (p0-p1).astype('float'), (p2-p1).astype('float')
    l1 = np.sqrt(d1[0]**2+d1[1]**2)
    l2 = np.sqrt(d2[0]**2+d2[1]**2)
    if l1<=l2*(1+tolerance) and l1>=l2*(1-tolerance):
        return True
    else :
        return False

def find_square(frame_in):
    frame_out = frame_in.copy()
    frame_gray = cv2.cvtColor(frame_in, cv2.COLOR_BGR2GRAY)
    #thresh = threshold(frame_gray,110)
    thresh = adap_threshold(frame_gray)
    frame_blur = cv2.blur(thresh, (3,3))
    #cv2.imshow('Threhold',thresh)
    contours, hry = cv2.findContours(frame_blur, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #identify squares
    squares = []
    for cnt in contours:
        # Calculate the perimeter
        cnt_len = cv2.arcLength(cnt, True)
        # Simpler Contour approximation 
        cnt = cv2.approxPolyDP(cnt, 0.01 * cnt_len, True)
        if  cv2.contourArea(cnt) > 10 and len(cnt) == 4 and cv2.isContourConvex(cnt) :
            cnt = cnt.reshape(-1, 2) # cnt is divided into two column 
            max_cos = np.max([angle_cos( cnt[i], cnt[(i+1) % 4], cnt[(i+2) % 4] ) for i in xrange(4)])
            if max_cos < 0.1 and equal(cnt[0], cnt[1], cnt[2],0.2):
                 squares.append(cnt)
    cv2.drawContours(frame_out , squares, -1, (0,255,0), 2)
   
    return frame_out 

if __name__ == "__main__":
    webcam_gui(find_square)
 
