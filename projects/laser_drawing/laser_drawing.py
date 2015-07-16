import cv2
import numpy as np

from screen_finder.screen_finder import ScreenFinder
from cam import OpenCV_Cam



def draw_burning(canvas, location):
    cv2.circle(canvas, (lx, ly), 5, (255, 0, 0, 255))
    return canvas
    
    
def laser_location(img):
    red_part = img[:,:,2]
    ly, lx = np.unravel_index(red_part.argmax(), red_part.shape)
    return np.array([lx, ly])
    
background = cv2.imread('wood.png')
cv2.imshow('Burn this page!', background)

sf = ScreenFinder()
sf.set_screen_img(background)

cam = OpenCV_Cam()
img = cam.read()
sf.find_screen_img(img)
sf.find_screen_loop(cam, False)

bs = background.shape
canvas = np.full((bs[0], bs[1], 4), 0, dtype=np.uint8)

show_top_view, show_cam_view = False, False
while True:
    img = cam.read()
    
    if show_cam_view:
        cv2.imshow('Cam view', img)
    
    if show_top_view:
        top_view = sf.screen_top_view(img)
        cv2.imshow('Top view', top_view)
    
    cam_laser = laser_location(img)
    
    lx, ly = tuple(sf.reverse_transform(cam_laser).reshape(-1))
    background = draw_burning(background, (lx, ly))
    cv2.imshow('Burn this page!', background)
    
    k = cv2.waitKey(10)
    if k == ord('a'):
        sf.find_screen_loop(cam, False)
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