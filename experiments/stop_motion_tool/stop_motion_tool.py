from cam import OpenCV_Cam
import cv2
cam = OpenCV_Cam()
cam.size = (1920, 1080)

KEY_ESC = 27
KEY_SPACE = ord(' ')
prevFrame = None
i = 0 

while True:
    # Capture frame-by-frame
    frame = cam.read()
	
    # image processing functions
    
    # Load the frame into a window named as 'Press any key to exit'

    if (prevFrame is not None):
        showFrame = cv2.addWeighted(frame,0.7,prevFrame,0.3,0)
    else:
        showFrame = frame
    
    cv2.imshow('Press ESC to exit', showFrame)
    
    # wait for the key
    key_code = cv2.waitKey(10)
	
    if key_code is KEY_SPACE:
        cv2.imwrite('frame'+str(i)+'.png', frame)
        prevFrame = frame
        i += 1
    elif key_code is KEY_ESC:
        break
	
cam.release()