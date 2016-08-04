from cam import OpenCV_Cam
import cv2
import os.path
import time

cam = OpenCV_Cam(0)
cam.size = (1920, 1080)

KEY_ESC = 27
KEY_SPACE = ord(' ')
PAGE_DOWN = 2228224 # This make the stop motion to be controllable by presenter. 
prevFrame = None
i = 0 


#Make a directory on current working directory with date and time as its name
timestr = time.strftime("%Y%m%d-%H%M%S")
cwd = os.getcwd()
dirName = cwd + "\\"+timestr 
os.makedirs(dirName)


fname= cwd + "\\frame_.png"
if os.path.isfile(fname):
    prevFrame = cv2.imread(fname)


#Make .avi file from collected frames
fourcc = cv2.cv.CV_FOURCC(*'XVID')
video = cv2.VideoWriter(dirName+"\\"+'output_.avi',fourcc, 3.0, cam.size, isColor =True)

while True:
    # Capture frame-by-frame
    frame = cam.read()
	
    # image processing functions
    
    # Load the frame into a window named as 'Press any key to exit'

    if (prevFrame is not None):
        showFrame = cv2.addWeighted(frame,0.7,prevFrame,0.3,0)
    else:
        showFrame = frame
    
    resizeShowFrame = cv2.resize(showFrame, (0,0), fx = 0.5, fy = 0.5 )
    cv2.imshow('Press ESC to exit', resizeShowFrame)
    
    # wait for the key
    key_code = cv2.waitKey(10)
    
    if key_code is KEY_SPACE or key_code == PAGE_DOWN:
        cv2.imwrite(dirName+"\\"+'frame'+str(i)+'_.png', frame)
        video.write(frame)
        prevFrame = frame
        i += 1
    elif key_code is KEY_ESC:
        cv2.imwrite(cwd + '\\frame_.png', prevFrame)
        break
cv2.destroyAllWindows()	
cam.release()
video.release()
