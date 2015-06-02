__author__ = 'fatcloud'
import cv2
import numpy as np

class MotionDetector(object):

    def __init__(self, N=1, cam=cv2.VideoCapture(1)):
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

cam = cv2.VideoCapture(1)

if not cam.isOpened():
    cam = cv2.VideoCapture(0)

md = MotionDetector(N=2, cam=cam)
cam_x, cam_y, _ = cam.read()[1].shape

mser = cv2.MSER()

try:
    prev_hulls = []
    while True:
        md.loop()

        
        gray = cv2.cvtColor(md.diff, cv2.COLOR_BGR2GRAY)
        regions = mser.detect(gray, None)
        
        hulls = []
        if regions != []:
            regions = np.concatenate(tuple(regions))
            # hulls = [cv2.convexHull(p.reshape(-1, 1, 2)) for p in regions]
            hulls = [cv2.convexHull(regions.reshape(-1, 1, 2))]
            # cv2.polylines(md.diff, [hulls], 1, (0, 255, 0))
            
            prev_hulls = hulls
        else:
            hulls = prev_hulls
        
        mask = np.zeros((cam_x, cam_y, 1), dtype=np.uint8)
        cv2.drawContours(mask, hulls, -1, (255,), -1)
        
        ret, mask = cv2.threshold(mask, 100, 255, cv2.THRESH_BINARY)
        
        vis = md._frame[md._index].copy()
        vis = cv2.bitwise_and(vis,vis,mask=mask)
        
        cv2.imshow(winName, vis)
        
        key = cv2.waitKey(10)
        if key == 27 or key == 32:
            md.cam.release()
            cv2.destroyWindow(winName)
            break
        elif key == ord('p'):
            print type(md.diff)
            print md.diff.shape
        elif key == ord('z'):
            print regions
            print regions.shape
        elif key == ord('x'):
            print regions[0]
            print regions[0].shape
except Exception as e:
    md.cam.release()
    print 'oops! something goes wrong'
    print dir(e), type(e), e
    
print "Goodbye"
