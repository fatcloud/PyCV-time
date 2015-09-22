import cv2
import numpy as np

def angle(p1, p2, p3):
    v1 = p1 - p2
    v2 = p3 - p2
    v1 = v1.astype(float)
    v2 = v2.astype(float)
    v1 = v1 / np.sqrt(np.dot(v1, v1))
    v2 = v2 / np.sqrt(np.dot(v2, v2))
    return np.degrees(np.arccos(np.dot(v1, v2)))


def is_circle(contour, area_ratio_threshold = 0.8):
    area = cv2.contourArea(contour)
    area_threshold = 40
    if area < area_threshold: return False
    
    simp_ctr = cv2.approxPolyDP(contour, 3, True)
    simp_area = cv2.contourArea(simp_ctr)
    if simp_area < area_threshold: return False
    
    equivalent_radius = cv2.arcLength(simp_ctr,True) / (2 * 3.1416)
    equivalent_area = (2 * 3.1416) * (equivalent_radius ** 2)

    area_ratio = simp_area / equivalent_area
    if area_ratio > area_ratio_threshold:
        return True
    else:
        print area_ratio
        return False