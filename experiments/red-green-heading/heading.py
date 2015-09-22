import cv2
import numpy as np

from numpy import linalg as LA
from cam import OpenCV_Cam
from get_color_mask import *


def find_contour_center(contour):
    if contour[0] is None:
        return None
    M = cv2.moments(contour[0])
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    return cx, cy

def get_mark_contour(img):
    ctrs, hry = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    ctrs = [ctr for ctr in ctrs if cv2.contourArea(ctr) > 10]
    ctrs = [ctr for ctr in ctrs if cv2.contourArea(ctr) < 2000]

    max_area = 0
    max_ctr = None
    for ctr in ctrs:
        area = cv2.contourArea(ctr)
        if area > max_area:
            max_ctr = ctr
            max_area = area

    return [max_ctr]



if __name__ == '__main__':

    cam = OpenCV_Cam()

    r_bound = ([0, 200, 50], [10, 255, 255])
    g_bound = ([80, 100, 50], [105, 255, 255])

    while True:
        
        image = cam.read()
        r_mask = get_mask(image, *r_bound, blur=3)
        g_mask = get_mask(image, *g_bound, blur=3)

        masks = cv2.bitwise_or(r_mask, g_mask)
        output = cv2.bitwise_and(image, image, mask = masks)

        r_ctr = get_mark_contour(r_mask)
        g_ctr = get_mark_contour(g_mask)
        cv2.drawContours(output, r_ctr, -1, (100,100,255), 2)
        cv2.drawContours(output, g_ctr, -1, (100,255,100), 2)
        
        r_center = find_contour_center(r_ctr)
        g_center = find_contour_center(g_ctr)

        if r_center is not None and g_center is not None:
            cv2.line(output, r_center, g_center, (255, 0, 0), 2)

        # show the images
        cv2.imshow("images", np.hstack([image, output]))
        k = cv2.waitKey(10)
        if k == 27:
            break