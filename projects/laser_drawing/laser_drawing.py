import cv2
import numpy as np

from screen_finder.screen_finder import ScreenFinder
from cam import OpenCV_Cam



def draw_burning(canvas, location):
    cv2.circle(canvas, (lx, ly), 5, (255, 0, 0, 255))
    return canvas
    
    
def find_laser_loc(img, threshold):
    red_part = img[:,:,2]
    max_pos = red_part.argmax()
    ly, lx = np.unravel_index(max_pos, red_part.shape)
    if red_part[ly, lx] < threshold:
        return None
    return np.array([lx, ly])

def find_threshold(cam):
    img = cam.read()
    hx, hy = find_laser_loc(img, 0)
    threshold = img[hy, hx, 2] + 10
    print "The red threshold is automatically determined to be", threshold
    return threshold

background = cv2.imread('wood.png')
cv2.imshow('Burn this page!', background)

sf = ScreenFinder()
sf.set_screen_img(background)

cam = OpenCV_Cam()
cam.size = 640, 480
img = cam.read()
sf.find_screen_img(img)
sf.find_screen_loop(cam, False)

bs = background.shape
canvas = np.full((bs[0], bs[1], 4), 0, dtype=np.uint8)

# prepare threshold
thresh = find_threshold(cam)

show_top_view, show_cam_view = False, False
while True:
    img = cam.read()
    
    if show_cam_view:
        cv2.imshow('Cam view', img)
    
    if show_top_view:
        top_view = sf.screen_top_view(img)
        cv2.imshow('Top view', top_view)
    
    cam_laser = find_laser_loc(img, thresh)
    if cam_laser is not None:    
        lx, ly = tuple(sf.reverse_transform(cam_laser).reshape(-1))
        background = draw_burning(background, (lx, ly))

    cv2.imshow('Burn this page!', background)
    
    k = cv2.waitKey(10)
    if k == ord('a'):
        sf.find_screen_loop(cam, False)
        thresh = find_threshold(cam)
    elif k == ord('s'):
        background = cv2.imread('wood.png')
    elif k == ord('d'):
        show_top_view = not show_top_view
        if show_top_view is False:
            cv2.destroyWindow('Top view')
    elif k == ord('f'):
        show_cam_view = not show_cam_view
        if show_cam_view is False:
            cv2.destroyWindow('Cam view')
    elif k == 27:
        break