import cv2
import numpy as np
from cam import MyCam
from find_polygons import draw_oriented_polylines
from fmatch import draw_match

class ScreenFinder(object):
    """This class find the location of the screen by feature matching
    a screen image set by set_screen_img with camera image loaded by
    find_screen_img.
    
    1. set_screen_img(your_image)
    
    2. find_screen_img(camera_image)
            After this, a tranform matrix along with a list of four corners
            of your screen is found and saved in ScreenFinder, which will be
            used to find the top view of the screen saw by the camera
            
    3. find_top_view(camera_image)
            return the top view of the screen found in camera
    
    """

    def __init__(self):
        
        self.screen_shape = None
        self._detector = cv2.SIFT()
        self._screen_img = None
        self._screen_features = None
        
        self.clear_found()
    
    @property
    def screen_is_found(self):
        return (self.cam2screen_matrix is not None)
    
    def clear_found(self):
        self.cam2screen_matrix = None
        self.screen2cam_matrix = None
        self._screen_corners = None
    
    def calibrate_color(self, cam_img, screen_img):
        cam_shot = self.find_top_view(cam_img)
        screen_img
    
    def set_screen_img(self, screen_img):
        self._screen_features = self._detector.detectAndCompute(screen_img,None)
        self._screen_img = screen_img
    
    def find_screen_img(self, cam_img, screen_img=None, debug=False):
        """
        Find screen_img in cam_img.
        If executed successfully, the function return True.
        Meanwhile self.recovery_matrix will be computed, which is used to
        map camera image to top view
        """
        
        try:
        
            MATCH_THRESHOLD = 10
            FLANN_INDEX_KDTREE = 0
            AREA_THRESHOLD = 1000
            
            if screen_img is None:
                kp1, des1 = self._screen_features
                screen_img = self._screen_img
            else:
                kp1, des1 = self._detector.detectAndCompute(screen_img,None)
            
            kp2, des2 = self._detector.detectAndCompute(cam_img,None)
            
            index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
            search_params = dict(checks = 50)
            flann = cv2.FlannBasedMatcher(index_params, search_params)
            
            matches = flann.knnMatch(des1,des2,k=2)
            
            # Perform Lowe's ratio test to select good points to proceed with.
            good = [m for m,n in matches if m.distance < 0.7*n.distance]
                    
            src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1,1,2)
            dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1,1,2)
            
            # check the property of the corners found out there
            self.screen2cam_matrix, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)
            matchesMask=mask.ravel().tolist()

            h,w = self._screen_img.shape
            pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
            self._screen_corners = cv2.perspectiveTransform(pts, self.screen2cam_matrix)
            
            if debug: cv2.imshow('debug', draw_match(screen_img, kp1, self.draw_screen_boundary(cam_img), kp2, good, matchesMask=matchesMask))
            else: cv2.destroyWindow('debug')
            
            if False in [cv2.isContourConvex(self._screen_corners),
                         cv2.contourArea(self._screen_corners) > AREA_THRESHOLD,
                         sum(matchesMask) > MATCH_THRESHOLD]:
            
                self.screen2cam_matrix = None
                self._screen_corners = None
                
                return False
            
            self.cam2screen_matrix, _ = cv2.findHomography(dst_pts, src_pts, cv2.RANSAC,5.0)
            
            return True
        
        except cv2.error:
        
            self.screen2cam_matrix = None
            self._screen_corners = None
            return False
        
    def draw_screen_boundary(self, cam_img):
    
        if self.screen2cam_matrix is None: return cam_img
        img = cam_img.copy()
        draw_oriented_polylines(img, self._screen_corners, True, (0,0,255), 3)

        return img
        
    
    def find_top_view(self, cam_img):
        shape = (self._screen_img.shape[1], self._screen_img.shape[0])
        img = cv2.warpPerspective(cam_img, self.cam2screen_matrix, shape)
        return img


if __name__ == '__main__':
    sf = ScreenFinder()
    cam = MyCam()
    cam.size = (640, 480)
    
    img = cv2.imread('seabunny_lying.png', 0)
    cv2.imshow('source', img)

    sf.set_screen_img(img)
    if img.shape[0] * img.shape[1] > cam.size[0] * cam.size[1]:
        img = cv2.resize(img, cam.size)

    while True:
        cam_img = cam.read()
        
        while not sf.screen_is_found:
            cam_img = cam.read()
            sf.find_screen_img(cam_img, debug=True)
            cv2.imshow('Type \'r\' to search for the screen', sf.draw_screen_boundary(cam_img))
            k = cv2.waitKey(5)
            if k == 27:
                break
        
        cv2.imshow('Type \'r\' to search for the screen', sf.draw_screen_boundary(cam_img))
        cv2.imshow('top view', sf.find_top_view(cam_img))
        k = cv2.waitKey(5)
        if k == 27:
            break
        elif k == ord('r'):
            sf.clear_found()