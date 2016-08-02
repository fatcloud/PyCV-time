from cam import OpenCV_Cam
import cv2
import os.path


cam = OpenCV_Cam(0)
cam.size = (1920, 1080)

KEY_ESC = 27
KEY_SPACE = ord(' ')
prevFrame = None
i = 0 

fname="frame.png"
if os.path.isfile(fname):
    prevFrame = cv2.imread(fname)


fourcc = cv2.cv.CV_FOURCC(*'XVID')
video = cv2.VideoWriter('output.avi',fourcc, 3.0, cam.size, isColor =True)


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
    
    if key_code is KEY_SPACE or key_code == 2228224:
        cv2.imwrite('frame'+str(i)+'.png', frame)
        video.write(frame)
        prevFrame = frame
        i += 1
    elif key_code is KEY_ESC:
        break
cv2.destroyAllWindows()	
cam.release()
video.release()
