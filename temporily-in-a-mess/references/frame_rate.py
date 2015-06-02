#!/usr/bin/env python

import numpy as np
import cv2
from common import draw_str
from time import clock
from caminfo import cv_cap_set, cv_cap_info

import sys

if __name__ == '__main__':
    try: video_src = int(sys.argv[1])
    except: video_src = 0
    
    cam = cv2.VideoCapture(video_src)
    fcount, frate = 0, 0

    start = clock()
    while True:
        try:

            fcount += 1
            ret, frame = cam.read()
            if fcount == 10:
                end = clock()
                frate = 10/(end - start)
                start = clock()
                fcount = 0
            vis = frame.copy()
            draw_str(vis, (20, 20), '%f frames per second' % frate)

            cv2.imshow('fps', vis)

            ch = 0xFF & cv2.waitKey(1)
            if ch == 27:
                break
            elif ch == ord('p'):
                print cv_cap_info(cam)
            elif ch == ord('s'):
                # print cv_cap_set(cam, 'CV_CAP_PROP_FRAME_WIDTH', 800)
                # print cv_cap_set(cam, 'CV_CAP_PROP_FRAME_HEIGHT', 600)
                cv_cap_set(cam, 'CV_CAP_PROP_MODE', 2)

        except AttributeError:
            continue

    cv2.destroyAllWindows()

