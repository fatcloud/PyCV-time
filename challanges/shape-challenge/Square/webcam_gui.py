import cv2


def webcam_gui(filter_func, video_src=0):

    cap = cv2.VideoCapture(video_src) 
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


        

def edge_filter(frame_in):
    # convert into gray scale
    frame_gray = cv2.cvtColor(frame_in, cv2.COLOR_BGR2GRAY)
    # blur the image to reduce noise
    frame_blur = cv2.blur(frame_gray, (3,3))
    # Canny edge detection
    frame_out = cv2.Canny(frame_blur, 30, 120)
    
    return frame_out

def threshold(frame_in):
    # convert into gray scale
    frame_gray = cv2.cvtColor(frame_in, cv2.COLOR_BGR2GRAY)
    # blur the image to reduce noise
    frame_blur = cv2.blur(frame_gray, (3,3))
    # threshold
    thresh1, thresh = cv2.threshold(frame_blur, 130, 255, cv2.THRESH_BINARY)
    frame_out = thresh
    return frame_out
    
def adap_threshold(frame_in):
    # convert into gray scale
    frame_gray = cv2.cvtColor(frame_in, cv2.COLOR_BGR2GRAY)
    # blur the image to reduce noise
    frame_blur = cv2.blur(frame_gray, (3,3))
    # threshold
    thresh = cv2.adaptiveThreshold(frame_blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
    frame_out = thresh
    return frame_out
    
def gray_filter(frame_in):
    # convert into gray scale
    frame_out = cv2.cvtColor(frame_in, cv2.COLOR_BGR2GRAY)
    
    return frame_out
    
    
    
if __name__ == "__main__":
    webcam_gui(adap_threshold)
 