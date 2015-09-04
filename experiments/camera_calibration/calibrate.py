#!/usr/bin/env python

import numpy as np
import cv2
import os
from common import splitfn

USAGE = '''
This example is copied from opencv 2.4.9
the origin file is opencv2\sources\samples\python2\calibrate.py

simple usage: >>>python calibrate.py
    this will generate camera_parameters.npz containing the following calibration data:
    mtx, dist, rvecs, tvecs

    what are they? I know mtx = camera_matrix becaues it is required by AR_static.py and AR_realtime.py
    I don't know about the other ones. Go figure it out!
    
complex: >>>python calibrate.py [--save <filename>] [--debug <output path>] [--square_size] [<image mask>]
    I haven't try this. 
    
    
    written by fatcloud 2015/5/4
'''



if __name__ == '__main__':
    import sys, getopt
    from glob import glob

    args, img_mask = getopt.getopt(sys.argv[1:], '', ['save=', 'debug=', 'square_size='])
    args = dict(args)
    try: img_mask = img_mask[0]
    except: img_mask = './origin/*.jpg'
    img_names = glob(img_mask)
    debug_dir = args.get('--debug')
    square_size = float(args.get('--square_size', 1.0))

    pattern_size = (8, 5)
    pattern_points = np.zeros( (np.prod(pattern_size), 3), np.float32 )
    pattern_points[:,:2] = np.indices(pattern_size).T.reshape(-1, 2)
    pattern_points *= square_size

    obj_points = []
    img_points = []
    h, w = 0, 0
    for fn in img_names:
        print 'processing %s...' % fn,
        img = cv2.imread(fn, 0)
        h, w = img.shape[:2]
        found, corners = cv2.findChessboardCorners(img, pattern_size)
        if found:
            term = ( cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_COUNT, 30, 0.1 )
            cv2.cornerSubPix(img, corners, (5, 5), (-1, -1), term)
        if debug_dir:
            vis = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
            cv2.drawChessboardCorners(vis, pattern_size, corners, found)
            path, name, ext = splitfn(fn)
            cv2.imwrite('%s/%s_chess.bmp' % (debug_dir, name), vis)
        if not found:
            print 'chessboard not found'
            continue
        img_points.append(corners.reshape(-1, 2))
        obj_points.append(pattern_points)

        print 'ok'

    rms, camera_matrix, dist_coefs, rvecs, tvecs = cv2.calibrateCamera(obj_points, img_points, (w, h))
    print "RMS:", rms
    print "camera matrix:\n", camera_matrix
    print "distortion coefficients: ", dist_coefs.ravel()
    np.savez('camera_parameters', mtx=camera_matrix, dist=dist_coefs, rvecs=rvecs, tvecs=tvecs)
    cv2.destroyAllWindows()
