import cv2
import numpy as np
from cam import MyCam
from mix_image import mix_image

def buildpyr(img_in):

    h = img_in.shape[0]
    w = img_in.shape[1]
    d = img_in.shape[2]
    
    img_out = np.full((h + h/2, w, d), 0, np.uint8)
    img_pyr = img_in
    x, y = 0, 0
    dx, dy = w, h
    
    
    for i in range(10):
        # place image at x, y
        img_out = mix_image(img_out, img_pyr, (x, y))
        
        if i % 2 == 0:
            y = y + dy
        else:
            x = x + dx
        
        dx, dy = dx/2, dy/2
        
        img_pyr = cv2.pyrDown(img_pyr)
    
    
    return img_out
    

if __name__ == "__main__":
    cam = MyCam()
    cam.cam_loop(buildpyr)
    # cv2.waitKey(0)