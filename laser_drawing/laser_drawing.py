import cv2
import numpy as np

from mix_image import mix_image
from screen_finder.screen_finder import ScreenFinder
from cam import OpenCV_Cam



def draw_burning(canvas, location):
    cv2.circle(canvas, (lx, ly), 5, (255, 0, 0, 255))
    return canvas
    
    
def laser_location(img):
    red_part = img[:,:,2]
    ly, lx = np.unravel_index(red_part.argmax(), red_part.shape)
    return lx, ly
    
background = cv2.imread('wood.png')
cv2.imshow('Burn this page!', background)

sf = ScreenFinder()
sf.set_screen_img(background)

cam = OpenCV_Cam()
img = cam.read()
sf.find_screen_img(img)
sf.find_screen_loop(cam, False)

bs = background.shape
canvas = np.full((bs[1], bs[0], 4), 0, dtype=np.uint8)

while True:
    img = cam.read()
    
    top_view = sf.screen_top_view(img)
    cv2.imshow('Top view', top_view)
    
    lx, ly = laser_location(top_view)
    canvas = draw_burning(canvas, (lx, ly))
    out    = mix_image(background, canvas)
    cv2.imshow('Burn this page!', out)
    
    k = cv2.waitKey(10)
    if k == ord( 'c' ):
        sf.find_screen_loop(cam, False)
    elif k == ord( 'r' ):
        canvas = np.full((bs[1], bs[0], 4), 0, dtype=np.uint8)
    elif k == 27:
        break