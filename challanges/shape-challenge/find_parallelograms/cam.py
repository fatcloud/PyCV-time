"""
press 'p' to print camera information
press 's' to set camera property. Try 'p' first to see property names then insert them in console.
press 'f' to print measured frame rate (the frequency VideoCapture::read() is called).
"""

import cv2
from time import clock


class OpenCV_Cam(object):

    def __init__(self, src=None):
        self.start_cam(src)
        self.__fcount, self.__frate, self.__start = 0, 0, clock()
    
    @staticmethod
    def cam_count():
        cam_idx = 0
        cap = cv2.VideoCapture(cam_idx)
        while cap.read()[0]:
            cam_idx += 1
            cap = cv2.VideoCapture(cam_idx)
            
        return cam_idx

    def start_cam(self, src=None):
        if src is not None:
            self.cam = VideoCapture(src)
            if not self.cam.isOpened():
                raise ValueError('Cannot open ' + src + 'as VideoCapture')
            return
        
        idx = 1
        cam1, cam2 = cv2.VideoCapture(0), cv2.VideoCapture(1)
        while(cam2.read()[0]):
            cam1.release()
            cam1 = cam2
            idx += 1
            cam2 = cv2.VideoCapture(idx)
        
        self.cam = cam1
        if not self.cam.isOpened():
            raise Error('Cannot open any camera')
        
    @property
    def size(self):
        w = self.cam.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)
        h = self.cam.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)
        return (int(w), int(h))

    @size.setter
    def size(self, shape):
        self.cam.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH , shape[0])
        self.cam.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, shape[1])
        
    def read(self):
        self.__fcount += 1
        self.__frame = self.cam.read()[1]
        if self.__fcount == 10:
            end = clock()
            self.__frate = 10/(end - self.__start)
                
            self.__start = clock()
            self.__fcount = 0
        return self.__frame

    @property
    def frame_rate(self):
        return self.__frate
        
    @property
    def info(self):
        vars = [x[12:] for x in dir(cv2.cv) if 'CV_CAP_PROP' in x]
        ret = {}
        for p in vars:
            cmd = 'ret[\''+ p + '\'] = self.cam.get(cv2.cv.CV_CAP_PROP_' + p + ')'
            exec cmd
            
        return ret

    def set(self, property, value):
        cmd = 'self.cam.set( cv2.cv.CV_CAP_PROP_' + property + ', ' + str(value) + ')'
        print cmd
        exec cmd
    
    def cam_loop(self, func = lambda x:x , params = ()):
        while True:
            input = self.read()
            output = func(input, *params)
            
            window_name = func.__name__
            if window_name == '<lambda>': window_name = 'camera image'
            
            cv2.imshow(window_name, output)
            k = cv2.waitKey(5)
            if k == 27:
                break
            elif k == ord('p'):
                info = self.info
                for i in info:
                    print i,'=', info[i]
            elif k == ord('s'):
                p = raw_input('type property:')
                if ('cv2.cv.CV_CAP_PROP_' + p) not in dir(cv2.cv):
                    print p, ' is not a legal property name.'
                    print 'Here are legal ones:', [x[12:] for x in dir(cv2.cv) if 'CV_CAP_PROP' in x]
                else:
                    v = raw_input('type value:')
                    self.set(p,v)
                        
            elif k == ord('f'):
                print self.frame_rate
    
    # __enter__ + __exit__ = with MyCam as cam:
    # this ensures that the camera will be released
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.cam.release()
    
    def release(self):
        self.cam.release()
    
if __name__ == '__main__':
    print __doc__
    cam = OpenCV_Cam()
    cam.size = (800, 600)
    
    cam.cam_loop()
        