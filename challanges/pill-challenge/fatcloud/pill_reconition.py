import cv2
import numpy as np


def equal(p0,p1,p2,tolerance):
    d1, d2 = (p0-p1).astype('float'), (p2-p1).astype('float')
    l1 = np.sqrt(d1[0]**2+d1[1]**2)
    l2 = np.sqrt(d2[0]**2+d2[1]**2)
    if l1<=l2*(1+tolerance) and l1>=l2*(1-tolerance):
        return True
    else :
        return False

def imgproc(frame):
    
    # convert color to gray scale and show it
    
    background = np.full_like(frame, 0)
    background[:,:,1] = 162
    background[:,:,2] = 14
    
    
    img = frame - background
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # convert image to black and white and show it
    thresh1, thresh = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)
    
    # find contours!
    contours, hry = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    
    squares = []
    quadrangles = []
    big_cycle = []
    white_small_cycle = []
    blue_small_cycle =[]
    pink_oval=[]
    white_oval =[]
    yellow_oval=[]
    capsule_3 = []
    capsule_4 = []
    for cnt in contours:
        # Calculate the perimeter
        cnt_len = cv2.arcLength(cnt, True)
        # Simpler Contour approximation 
        cnt = cv2.approxPolyDP(cnt, 0.02 * cnt_len, True)
        # ================== Step 1 Quadrangles ===================
        if cv2.isContourConvex(cnt):
            if len(cnt) == 4:
                cnt = cnt.reshape(-1, 2) # cnt is divided into two column 
                if equal(cnt[0], cnt[1], cnt[2],0.1):
                    squares.append(cnt)
                else:
                    quadrangles.append(cnt)
                    
        # ================== Step 2 Cycle ===================
            else:
                cnt = cnt.reshape(-1, 2)
                rect = cv2.minAreaRect(cnt)
                box = cv2.cv.BoxPoints(rect)
                box = np.int0(box)
                if equal(box[0], box[1], box[2],0.1):
                    if cv2.contourArea(cnt) > 1000 :
                        big_cycle.append(cnt)
       # ================== Step 3 By Color ===================             
                    else:
                        cg = np.mean(cnt,axis=0)
                        org = int(cg[0]), int(cg[1])
                        rgb = img[org[1]][org[0]] 
                        rgb_mean = np.average(rgb)
                        if rgb_mean > 180:
                            white_small_cycle.append(cnt)
                        else:
                            blue_small_cycle.append(cnt)
                else:           
                    cg = np.mean(cnt,axis=0)
                    org = int(cg[0]), int(cg[1])
                    rgb = img[org[1]][org[0]] 
                    rgb_mean = np.average(rgb)
                    
                    if rgb_mean > 200:
                        pink_oval.append(cnt)
                    elif rgb[0] == 255:
                        white_oval.append(cnt)
                    elif rgb_mean > 180:
                        capsule_4.append(cnt)
                    elif rgb_mean < 95:
                        yellow_oval.append(cnt)
                    else:
                        capsule_3.append(cnt)
    
    drug_list = [(squares         , '8'),
                (quadrangles      , '2'),
                (big_cycle        , '10'),
                (white_small_cycle, '9'),
                (blue_small_cycle , '1'),
                (pink_oval        , '6'),
                (white_oval       , '7'),
                (yellow_oval      , '5'),
                (capsule_3        , '3'),
                (capsule_4        , '4')]
    
    for drug, index in drug_list:
        for ctr in drug:
            m = np.mean(ctr,axis=0)
            org = int(m[0]), int(m[1])
            cv2.putText(frame, index, org, cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    

    return frame

if __name__ == "__main__":
    pills = cv2.imread('pill.png')
    cv2.imshow('pill challenge',imgproc(pills))
    cv2.waitKey(0)