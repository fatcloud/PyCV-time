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
    
    img1_ = img1.copy()
    img2_ = img2.copy()
    
    if len(img1.shape) == 2 or img1.shape[2] == 1:
        img1_= cv2.cvtColor(img1_, cv2.COLOR_GRAY2BGR)
        
    if len(img2.shape) == 2 or img2.shape[2] == 1:
        img2_= cv2.cvtColor(img2_, cv2.COLOR_GRAY2BGR)
    
    outimg[0:h1,0:w1, :] = img1_
    outimg[0:h2,w1:w1+w2, :] = img2_
    
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

    
    
def test_feature_matching_realtime(detetor=cv2.ORB()):
    from cam import MyCam
    """
    Press 's' to take a picture or 'l' to load one and start real-time
    """

    MIN_MATCH_COUNT = 10

    cam = MyCam()
    cam.size = (640, 480)
    img1 = img1 = cv2.imread('box.png', 0)

    cv2.imshow('source', img1)
    while True:
        
        img2 = cv2.flip(cv2.cvtColor(cam.read(), cv2.COLOR_BGR2GRAY), 1)
        k = cv2.waitKey(5)
        if k == ord('s'):
            img1 = img2.copy()
            cv2.imwrite('campic.png', img1)
        elif k== 27:
            break
        
        
        
        # find the keypoints and descriptors with ORB
        if k is not None:
            cv2.destroyWindow('preview') 
            kp1, des1 = detetor.detectAndCompute(img1,None)
            
        kp2, des2 = detetor.detectAndCompute(img2,None)
        
        
        # If nothing match then continue
        if des2 is None:
            img3 = img3 = draw_match(img1,kp1,img2,kp2,[])
            continue
        
        des1 = des1.astype(np.uint8, copy=False)    # Fix the data type
        des2 = des2.astype(np.uint8, copy=False)
        
        
        # Now match describers
        bf = cv2.BFMatcher(cv2.NORM_HAMMING)
        # matches = bf.match(des1,des2)
        
        matches = bf.knnMatch(des1,des2, k=2)
        
        # m = matches[0][0]
        # p1, p2 = np.float32(kp1[m.queryIdx].pt), np.float32(kp2[m.trainIdx].pt)
        # print m.distance, p1, p2
        
        # Apply ratio test
        good = []
        try:
            for m,n in matches:
                if m.distance < 0.7*n.distance:
                    good.append(m)
        except ValueError:
            good = []
        
        if len(good)>MIN_MATCH_COUNT:
            src_pts = np.float32([ kp1[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
            dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good ]).reshape(-1,1,2)

            M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
            matchesMask = mask.ravel().tolist()
            
            h,w = img1.shape
            pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
            dst = cv2.perspectiveTransform(pts,M)
            
            cv2.polylines(img2,[np.int32(dst)], True, (0,0,255) ,3)

        else:
            # print "Not enough matches are found - %d/%d" % (len(good),MIN_MATCH_COUNT)
            matchesMask = None
            good = []
        
        img3 = draw_match(img1,kp1,img2,kp2,good, matchesMask=matchesMask)
        
        
        cv2.imshow('matches', img3)
        
    print 'press any key to continue'
    
if __name__ == '__main__':
    test_feature_matching_realtime()