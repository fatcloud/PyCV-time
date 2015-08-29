from cv2 import *
import numpy as np
from motion_detect import MotionDetector
from cam import MyCam
from find_polygons import find_polygons, draw_oriented_polylines


class ScreenFinder(object):
    """This class find the location of the screen by checking
    if there is a quadrangle area that varies with respect to time"""

    def __init__(self, depth=2):
        self.screens = None
        self.screen_size = None
        self._md = None
        self._mapping_matrix = None
        self.real_screen_shape = None
        
    def put_calibrate_images(self, screen_image, cam_img):
        """calibrate(self, screen_image, cam_img) -> None
        Find the screen corners, transform matrix, and light state"""
    
        # find screen corners by comparing the difference between previous taken images
        if self._md is None:
            self._md = MotionDetector(N=2, shape=cam_img.shape)
    
        self._md.feed_image(cam_img.copy())
        
        gray_diff = cvtColor(self._md.diff, COLOR_BGR2GRAY)
        quadrangles = find_polygons(gray_diff, 4, 0.1, 1000, True, 10)
        
        if quadrangles != []:
            self.screens = quadrangles
    
        if self.screens is not None:
            self.compute_transform(screen_img)
        
        
    
    def compute_transform(self, screen_img):
        
        if self.screens is None:
            print 'Warning: calibration failed for the screen is not found yet'
            return
        
        # load the width and height of the real screen
        w, h = screen_img.shape[1], screen_img.shape[0]
        self.real_screen_shape = (w, h)
        
        # prepare the points
        src_pts = self.screens[0].astype(np.float)
        h, w = screen_img.shape[0], screen_img.shape[1]
        dst_pts = np.array([[0, 0], [0, h], [w, h], [w, 0]], dtype=np.float)
        
        # find transformation matrix
        self._mapping_matrix, mask = findHomography(src_pts, dst_pts, RANSAC, 5.0)
        
    
    def findTopView(self, cam_img):
        img = warpPerspective(cam_img, self._mapping_matrix, self.real_screen_shape)
        return img
    
    def find_laser_spots(self, screen_img, cam_img):
        # find location of green/red spots on camera image
        
        # transform the point and compute where it is
        pass
        
        
        
    def reset(self):
        self.screens = None
            
    def find(self):
        pass


if __name__ == '__main__':
    
    from random import randint
    win_size = (600, 800, 3)

    cam = MyCam()
    sf = ScreenFinder()
    
    black = np.full(win_size, (0, 0, 0), np.uint8)
    
    while True:
        k = waitKey(5)
        if k == 27:
            break
        if k == ord('r'):
            sf.reset()
        
        cam_img = cam.read()
        on = True
        while sf.screens is None:
            
            on = not on
            x = on * 255
            screen_img = np.full(win_size, (x, x, x), np.uint8)
            imshow('main', screen_img)
            imshow('screen finder', cam_img)
            # wait so that the camera can capture images completely loaded
            k = waitKey(20)
            cam_img = cam.read()
            sf.put_calibrate_images(screen_img, cam_img)
            
            # delay again to make sure that the image will not change during the camera taking picture
            k = waitKey(20)
            
        for rect in sf.screens:
            draw_oriented_polylines(cam_img, rect, 0, (0, 0, 255), 3)
        
        imshow('topview', sf.findTopView(cam_img))
        
        imshow('main', black)
        imshow('screen finder', cam_img)
            
        
        