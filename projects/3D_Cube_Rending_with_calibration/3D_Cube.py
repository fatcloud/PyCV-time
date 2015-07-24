import numpy as np
import cv2
import glob

def webcam_gui(filter_func, video_src=0):
    
    cap = cv2.VideoCapture(video_src)
    cap.set(6, 100) 
   
    key_code = -1
    
    while(key_code == -1):
        # read a frame
        ret, frame = cap.read()
        
        # run filter with the arguments
        frame_out = filter_func(frame)
        
        # show the image
        cv2.imshow('Press any key to exit', frame_out)
        
        # wait for the key
        key_code = cv2.waitKey(10)

    cap.release()
    cv2.destroyAllWindows()


def draw2(img, corners, imgpts):
    imgpts = np.int32(imgpts).reshape(-1,2)
    print imgpts
    # draw ground floor in green
    cv2.drawContours(img, [imgpts[:4]],-1,(0,255,0),-3)
    
    
    # draw pillars in blue color
    for i,j in zip(range(4),range(4,8)):
        cv2.line(img, tuple(imgpts[i]), tuple(imgpts[j]),(255),3)

    # draw top layer in red color
        cv2.drawContours(img, [imgpts[4:]],-1,(0,0,255),3)

    return img

def draw(img, corners, imgpts):
    corner = tuple(corners[0].ravel())
    cv2.line(img, corner, tuple(imgpts[0].ravel()), (255,0,0), 5)
    cv2.line(img, corner, tuple(imgpts[1].ravel()), (0,255,0), 5)
    cv2.line(img, corner, tuple(imgpts[2].ravel()), (0,0,255), 5)
    return img

# mtx, dist, rvecs, tvecs

mtx = np.load("mtx.npy")
dist = np.load("dist.npy")
rvecs = np.load("rvecs.npy")
tvecs = np.load("tvecs.npy")

def cube(img):
    #img_in = cv2.imread("Picture 27.jpg")
    #img = cv2.resize(img_in,None,fx=0.5, fy=0.5, interpolation = cv2.INTER_CUBIC)
        #cv2.imshow('img',img)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        #cv2.imshow('gray',gray)
    ret, corners = cv2.findChessboardCorners(gray, (8,7),None)
        # print ret,corners

    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
    objp = np.zeros((7*8,3), np.float32)
    objp[:,:2] = np.mgrid[0:8,0:7].T.reshape(-1,2)

    #axis = np.float32([[3,0,0], [0,3,0], [0,0,-3]]).reshape(-1,3)
    axis = np.float32([[0,0,0], [0,3,0], [3,3,0], [3,0,0],
                       [0,0,-3],[0,3,-3],[3,3,-3],[3,0,-3] ])

    if ret == True:
        cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
            
            
                # Find the rotation and translation vectors.
        rvecs, tvecs, inliers = cv2.solvePnPRansac(objp, corners, mtx, dist)

                # project 3D points to image plane
        imgpts, jac = cv2.projectPoints(axis, rvecs, tvecs, mtx, dist)
        #print imgpts
        img = draw2(img,corners,imgpts)
        
    return img

   

if __name__ == "__main__":
    # mtx, dist, rvecs, tvecs

    mtx = np.load("mtx.npy")
    dist = np.load("dist.npy")
    rvecs = np.load("rvecs.npy")
    tvecs = np.load("tvecs.npy")
    
    webcam_gui(cube)