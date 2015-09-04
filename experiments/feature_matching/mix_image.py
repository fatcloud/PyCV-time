#! /usr/bin/env python


import cv2
import numpy as np



def mix_image(back, fore, (x, y), in_place=False):
    """Back is a BGR image in background. Fore stands for a BGRA image to be paste in foreground.
    Fore will be paste at (x,y) in back. This function also support out-of bound (x,y)"""
    
    x, y = round(x), round(y)
    
    if in_place:
        ret = back
    else:
        ret = back.copy()
    
    fh, fw, fd = fore.shape
    bh, bw, bd = ret.shape
    
    if fd == 4:
        fore_alpha = lambda fy, h, fx, w: fore[fy:fy+h, fx:fx+w, 3]/255.0
    else:
        fore_alpha = lambda fy, h, fx, w: 1.0
    
    # check if foreground image is about to be placed in background image
    if True in [x + fw < 0, x > bw, y + fh < 0, y > bh]:
        return ret
    
    fx, fy = 0, 0
    bx, by = x, y

    w, h = fw, fh
    
    # fix fx, fy, bx, by if any of bx, by is negative
    if bx < 0:
        w = fw + bx
        fx = -bx
        bx = 0
    if by < 0:
        h = fh + by
        fy = -by
        by = 0
    
    # now fix w and h so that bx + w, by + h will not go out from background
    if bx + w > bw:
        w = bw - bx
    if by + h > bh:
        h = bh - by
    
    for c in range(0,3):
        ret[by:by+h, bx:bx+w, c] = \
        fore[fy:fy+h, fx:fx+w, c] * fore_alpha(fy, h, fx, w) +\
        ret[by:by+h, bx:bx+w, c] * (1.0 - fore_alpha(fy, h, fx, w))

    return ret
    
    
    




if __name__ == '__main__':
    
    back = cv2.imread("land.jpg")
    fore = cv2.imread("phppg.png", -1)
    
    sh = fore.shape
    b  = np.full_like(fore, 255, np.uint8)
    bb = mix_image(b, fore, (0, 0))
    
    cv2.imshow('fore', bb)
    cv2.imshow('back', back)
    
    from random import random as rdm
    w, h, d = back.shape
    
    for i in range(10):
        back = mix_image(back, fore, (w * 1.2 * (rdm() - 0.2),h * 1.2 * (rdm() - 0.2)))
        
    cv2.imshow('mixed', back)
    cv2.imwrite('mixed.png', back)
    cv2.waitKey(0)