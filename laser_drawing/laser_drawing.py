import cv2
import numpy as np

from mix_image import mix_image
from convertPts import mapping, calibrate
from cam import OpenCV_Cam


cam = OpenCV_Cam()
img = cam.read()
M = calibrate('screen_img', img)
find_laser = mapping(M)
canvas = np.full((600,800,4), 255, dtype=np.uint8)

while True:
    img    = cam.read()
    x, y   = get_laser(img)
    lx, ly = find_laser(x, y)
    canvas = draw_point(canvas, (lx, ly))
    out    = mix_image(img, canvas)
    cv2.imshow(,out)
    k = waitkey(10)
    if k == ord( 'c' ):
        calibrate again
    else if  k == ord( 'r' ):
        canvas = np.full((600,800,4), 255, dtype=np.uint8)