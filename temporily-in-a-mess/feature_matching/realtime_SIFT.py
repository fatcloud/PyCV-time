"""
Press 's' to take a picture or 'l' to load one and start real-time
"""

import cv2
import numpy as np
from cam import MyCam

from fmatch import draw_match


MIN_MATCH_COUNT = 10

# Initiate SIFT detector
sift = cv2.SIFT()
cam = MyCam()
cam.size = (160, 120)
img1 = cv2.imread('seabunny1600.png', 0)
cv2.imshow('source', img1)

if img1.shape[0] * img1.shape[1] > cam.size[0] * cam.size[1]:
    img1 = cv2.resize(img1, cam.size)

kp1, des1 = sift.detectAndCompute(img1,None)
    
while True:
    
    img2 = cv2.flip(cv2.cvtColor(cam.read(), cv2.COLOR_BGR2GRAY), 1)
    k = cv2.waitKey(5)
    if k == ord('s'):
        img1 = img2.copy()
        kp1, des1 = sift.detectAndCompute(img1,None)
        cv2.imwrite('campic.png', img1)
    if k == ord('r'):
        print cam.frame_rate
    elif k== 27:
        break
    
    kp2, des2 = sift.detectAndCompute(img2,None)


    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks = 50)

    flann = cv2.FlannBasedMatcher(index_params, search_params)

    matches = flann.knnMatch(des1,des2,k=2)

    # store all the good matches as per Lowe's ratio test.
    good = []
    for m,n in matches:
        if m.distance < 0.7*n.distance:
            good.append(m)

    if len(good)>MIN_MATCH_COUNT:
        src_pts = np.float32([ kp1[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
        dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good ]).reshape(-1,1,2)

        M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)
        matchesMask = mask.ravel().tolist()

        h,w = img1.shape
        pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
        dst = cv2.perspectiveTransform(pts,M)

        cv2.polylines(img2,[np.int32(dst)],True,255,3)

    else:
        print "Not enough matches are found - %d/%d" % (len(good),MIN_MATCH_COUNT)
        matchesMask = None
        
        
    draw_params = dict(matchColor = (0,255,0), # draw matches in green color
                       singlePointColor = None,
                       matchesMask = matchesMask, # draw only inliers
                       flags = 2)

    # print [x for x in dir(kp1[0]) if not '__' in x]

    # print [x for x in dir(good[0]) if not '__' in x]
    img3 = draw_match(img1,kp1,img2,kp2,good,None,**draw_params)
    cv2.imshow('matches', img3)
    