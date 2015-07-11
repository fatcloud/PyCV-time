import cv2

# initialize the video source
cap = cv2.VideoCapture(0)


key_code = -1

while(key_code == -1):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # image processing functions
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Load the frame into a window named as 'Press any key to exit'
    cv2.imshow('Press any key to exit', frame_gray)
    
    # wait for the key
    key_code = cv2.waitKey(10)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()