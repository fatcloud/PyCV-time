__author__ = 'fatcloud'
import cv2
import numpy as np
from cam import MyCam



class MotionDetector(object):

    def __init__(self, N=1, shape=(480,640,3)):
        self._N = N
        self._frame = [None] * (2 * N + 1)
        self._index = 0
        for i in range(2 * N + 1):
            self._frame[i] = np.full(shape, 0, np.uint8)
    
    def three_frames(self):
        n  = self._N
        f0 = self._frame[self._index]
        f1 = self._frame[(self._index + n) % (2 * n)]
        f2 = self._frame[(self._index + 2 * n) % (2 * n)]
        return [f0, f1, f2]
    
    def diff_img(self):
        f0, f1, f2 = self.three_frames()
        d1 = cv2.absdiff(f1, f0)
        d2 = cv2.absdiff(f2, f1)
        self.diff = cv2.bitwise_and(d1, d2)

    def feed_image(self, image):
        self._index = (self._index + 1) % (2 * self._N)
        self._frame[self._index] = image
        self.diff_img()
        

        
if __name__ == '__main__':

    winName = "cam test"
    cv2.namedWindow(winName, cv2.CV_WINDOW_AUTOSIZE)
    # Read three images first:

    cam = MyCam()
    md = MotionDetector(N=2, shape=cam.read().shape)

    while True:
        
        md.feed_image(cam.read())
        cv2.imshow(winName, md.diff)
        
        key = cv2.waitKey(10)
        if key == 27 or key == 32:
            cam.release()
            cv2.destroyWindow(winName)
            break

    print "Goodbye"
