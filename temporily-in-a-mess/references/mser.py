#!/usr/bin/env python

'''
MSER detector demo
==================

Usage:
------
    mser.py [<video source>]

Keys:
-----
    ESC   - exit

'''

import numpy as np
import cv2

if __name__ == '__main__':
    import sys
    try: video_src = sys.argv[1]
    except: video_src = 0

    cam = cv2.VideoCapture(video_src)
    mser = cv2.MSER()
    while True:
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        vis = img.copy()

        regions = mser.detect(gray, None)
        # hulls = [cv2.convexHull(p.reshape(-1, 1, 2)) for p in regions]
        
        cv2.polylines(vis, hulls, 1, (0, 255, 0))

        cv2.imshow('img', vis)
        k = 0xFF & cv2.waitKey(5)
        if k == 27:
            break
        elif k == ord('p'):
            print regions[0]
    cv2.destroyAllWindows()
