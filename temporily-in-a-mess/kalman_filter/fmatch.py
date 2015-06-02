import numpy as np
import cv2



def draw_match(img1, kp1,
               img2, kp2, 
               matches,
               output = None,
               matchColor = (255,0,0),
               matchesMask = None,
               *args, **kargs):
    h1 = img1.shape[0]
    w1 = img1.shape[1]
    
    h2 = img2.shape[0]
    w2 = img2.shape[1]
    
    w = w1 + w2
    h = max(h1, h2)
    
    outimg = np.full((h,w,3), 0, np.uint8)
    

    outimg[0:h1,0:w1, :] = cv2.cvtColor(img1, cv2.COLOR_GRAY2BGR)
    outimg[0:h2,w1:w1+w2, :] = cv2.cvtColor(img2, cv2.COLOR_GRAY2BGR)
    
    for i, m in enumerate(matches):
        if matchesMask is not None and matchesMask[i] == 0: continue
        i1 , i2  = m.queryIdx, m.trainIdx
        pt1, pt2 = kp1[i1].pt, kp2[i2].pt
        pt1 = ( int(pt1[0]), int(pt1[1])) 
        pt2 = ( int(w1 + pt2[0]), int(pt2[1]))
        cv2.line(outimg, pt1, pt2, matchColor)
    
    if output is not None:
        output = outimg.copy()
    
    return outimg
