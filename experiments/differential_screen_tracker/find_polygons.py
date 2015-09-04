import cv2
import numpy as np
from cam import MyCam
from time import time

def draw_oriented_polylines(img, pts_in, is_closed, color_start, thickness=1, color_end=(0,0,0)):
    img_out = img
    
    pts = pts_in.reshape(-1, 2)
    if len(img.shape) == 2 or img.shape[2] == 1:
        img_out = cv2.cvtColor(img_out, cv2.COLOR_GRAY2BGR)
    
    cs, ce = color_start, color_end
    n = len(pts)
    for idx, pt in enumerate(pts):
    
        if idx == n and not is_closed: break
    
        next_pt = pts[(idx + 1) % n]
        
        color = ((cs[0]*(n-idx) + ce[0]*idx) / n,\
                 (cs[1]*(n-idx) + ce[1]*idx) / n,\
                 (cs[2]*(n-idx) + ce[2]*idx) / n)
        cv2.line(img_out, tuple(pt), tuple(next_pt), color, thickness)
            

def find_polygons(gray_image_in, edge_num, tolerance=0.1, area_threshold=100, convex_only=True, edge_threshold=60, orientation=1.0):
    """find contours that appears to be a """
    img = gray_image_in.copy()
    lo, hi = 100, 150
    
    # cv2.imshow('img', img)
    edge = cv2.Canny(img, lo, hi)
    # imshow('edge', edge)
    thresh1, dst = cv2.threshold(edge,edge_threshold,255, cv2.THRESH_BINARY)
    # imshow('thresh', dst)
    ctr, hry = cv2.findContours(dst, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.imshow('fndctr', dst)
    
    if hry is None: return []
    hry = hry[0]
    
    polygons = []
    for cnt in ctr:

        # kill the contour if it doesn't look like a square
        cnt = cnt.reshape(-1,2)
        epsilon = tolerance * 2 * ((3.14 * cv2.contourArea(cnt)) ** 0.5)
        tmp = cv2.approxPolyDP(cnt,epsilon,True)

        if len(tmp) != edge_num: continue
        if convex_only and not cv2.isContourConvex(tmp): continue 
        if cv2.contourArea(tmp) < area_threshold: continue
        
        # now sort the points in counter clock wise so we can eliminate similar solutions
        cross_product = np.cross(tmp[1] - tmp[0], tmp[2] - tmp[1])[0]
        if cross_product * orientation > 0:
            tmp = np.flipud(tmp)
        
        # rearrange the points so that the returned point array always start with
        # the point that is closest to origin
        tmp = tmp.reshape(-1,2)
        distance_from_origin = map(lambda pt: pt[0] ** 2 + pt[1] ** 2, tmp)
        val, idx = min((val, idx) for (idx, val) in enumerate(distance_from_origin))
        
        if idx > 0:
            up, down = np.vsplit(tmp, [idx])
            tmp = np.vstack((down, up))
        
        polygons.append(tmp)
    
    return polygons
    
if __name__ == "__main__":
    cam = MyCam()
    while True:
        img = cam.read()
        polygons = find_polygons(img, 4)
        for ctr in polygons:
            draw_oriented_polylines(img, ctr, 0, (0,0,255), 2, (255,0,0))
        cv2.imshow('find quadrangles',img)
        k = cv2.waitKey(5)
        if k == 27:
            break