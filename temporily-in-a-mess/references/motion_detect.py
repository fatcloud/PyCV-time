__author__ = 'fatcloud'
import cv2




class MotionDetector(object):

    def __init__(self, N=1, cam=cv2.VideoCapture(0)):
        self.cam = cam
        self._N = N
        self._frame = [None] * (2 * N + 1)
        self._index = 0
        for i in range(2 * N + 1):
            self._frame[self._index] = cam.read()[1]
            self._index += 1
    # cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
    
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

    def loop(self):
        self._index = (self._index + 1) % (2 * self._N)
        self._frame[self._index] = self.cam.read()[1]
        self.diff_img()
        
    

winName = "cam test"
cv2.namedWindow(winName, cv2.CV_WINDOW_AUTOSIZE)
# Read three images first:
md = MotionDetector(N=2)

while True:
    md.loop()
    cv2.imshow(winName, md.diff)
    
    key = cv2.waitKey(10)
    if key == 27 or key == 32:
        md.cam.release()
        cv2.destroyWindow(winName)
        break

print "Goodbye"
