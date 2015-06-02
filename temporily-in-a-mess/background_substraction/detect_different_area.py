import cv2
import cv2.cv as cv
import numpy as np
 
capture = cv2.VideoCapture(0)
size = (int(capture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),
        int(capture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))
fgbg = cv2.BackgroundSubtractorMOG()

while True:
    ret, img = capture.read()
    if ret is True:
        fgmask = fgbg.apply(img)
        cv2.imshow('forehead', fgmask)

    key = cv2.waitKey(50)
    if key is 27:
        break
    elif key is ord(' '):
        fgbg = cv2.BackgroundSubtractorMOG()
 
capture.release()
cv2.destroyAllWindows()
print('Done!')