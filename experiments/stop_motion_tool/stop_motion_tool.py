from cam import OpenCV_Cam
import cv2
cam = OpenCV_Cam()
cam.size = (1920, 1080)

KEY_ESC = 27
KEY_ENTER = 13
f1 = None
f2 = None

fdiff = None
fadd = None
prevFrame = None
resPrevFrame = None

while True:
    # Capture frame-by-frame
    frame = cam.read()
	
    # image processing functions
    
    # Load the frame into a window named as 'Press any key to exit'
    
    resFrame = cv2.resize(frame,None,fx=0.3, fy=0.3, interpolation = cv2.INTER_CUBIC)

    if (resPrevFrame is not None):
        resFrame = cv2.addWeighted(resFrame,0.7,resPrevFrame,0.3,0)
    
    cv2.imshow('Press ESC to exit', resFrame)
    
    if f2 is not None:
        fadd = cv2.addWeighted(f1,0.7,f2,0.3,0)
        resAdd = cv2.resize(fadd,None,fx=0.3, fy=0.3, interpolation = cv2.INTER_CUBIC)
        cv2.imshow('Diff', resAdd)
	
    # wait for the key
    key_code = cv2.waitKey(10)
	
    if key_code == KEY_ENTER:
        f2 = f1
        f1 = frame
            #fdiff = cv2.absdiff(f1,f2)
    elif key_code is ord(' '):
        f1 = frame
    elif key_code is ord('s'):
        cv2.imwrite('frame.png', frame)
        prevFrame = frame
        resPrevFrame = cv2.resize(prevFrame,None,fx=0.3, fy=0.3, interpolation = cv2.INTER_CUBIC)
        print "haha"
    elif key_code is KEY_ESC:
        break
	
	
	
cam.release()