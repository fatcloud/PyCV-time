import cv2
import numpy as np
from cam import OpenCV_Cam

def get_mask(img, lower, upper, blur=0):

    if lower[0] < 0:
        offset = -lower[0]
    else:
        offset = 0

    lower[0] = lower[0] + offset
    upper[0] = upper[0] + offset

    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hsv_img = cv2.blur(hsv_img, (blur, blur))
    shift = np.full_like(img, 0, np.uint8)
    shift[:,:,0] = offset

    hsv_img = hsv_img + shift



    lower = np.array(lower, dtype = "uint8")
    upper = np.array(upper, dtype = "uint8")
 
    mask = cv2.inRange(hsv_img, lower, upper)
    return mask


if __name__ == '__main__':

    cam = OpenCV_Cam()

    red_bound = ([-5, 150, 0], [15, 255, 255])
    green_bound = ([80, 100, 0], [105, 255, 255])

    while True:
        
        image = cam.read()
        red_mask   = get_mask(image, *red_bound)
        green_mask = get_mask(image, *green_bound)

        masks = cv2.bitwise_or(red_mask, green_mask)

        cv2.imshow('masks', np.hstack([red_mask, green_mask]))

        output = cv2.bitwise_and(image, image, mask = masks)
     
        # show the images
        cv2.imshow("images", np.hstack([image, output]))
        k = cv2.waitKey(10)
        if k == 27:
            break