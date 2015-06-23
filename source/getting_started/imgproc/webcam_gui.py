import cv2



def webcam_gui(exp_func, video_index=0, *arg, **kwarg):

    cap = cv2.VideoCapture(video_index)

    key_code = -1

    while(key_code == -1):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # image processing functions
        frame_out = exp_func(frame=frame, *arg, **kwarg)
        
        # Load the frame into a window named as 'Press any key to exit'
        cv2.imshow('Press any key to exit', frame_out)
        
        # wait for the key
        key_code = cv2.waitKey(10)

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
    

if __name__ == "__main__":

    webcam_gui(cv2.cvtColor, cv2.COLOR_BGR2GRAY)