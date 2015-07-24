import cv2
import numpy as np
def imgproc(frame):
    
    
    # convert color to gray scale and show it
    
    background = np.full_like(frame, 0) 
    background[:,:,1] = 162
    background[:,:,2] = 14
    

    img = frame - background
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # convert image to black and white and show it
    thresh1, thresh = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)
    
    # find contours!
    contours, hry = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # draw all the contours
    cpframe = frame.copy()
    cv2.drawContours(cpframe, contours, -1, (255,0,0), 3)
    cv2.imshow('contours', cpframe)
    
    # ================== TODO ===================
    
    # Every pill is surrounded by a contour in variable "contours" now
    
    # ============================================   

    color = []
    colors = []
    index = 0
    print len(contours)
    print (frame.shape, img.shape, gray.shape)
    for ctr in contours:
        M = cv2.moments(ctr)      
        cy = int(M['m10']/M['m00']) 
        cx = int(M['m01']/M['m00'])
        area = cv2.contourArea(ctr)
        cy2 = cy + 2
        cx2 = cx + 2
        cy3 = cy - 2
        cx3 = cx - 2
        cy4 = cy + 2
        cx4 = cx - 2
        cy5 = cy - 2
        cx5 = cx + 2       
        print index, frame[cx,cy,:], frame[cx2,cy2,:], frame[cx3,cy3,:], frame[cx4,cy4,:], frame[cx5,cy5,:], area
        color.append(frame[cx,cy, :])
        colors.append([frame[cx2, cy2, :], frame[cx3, cy3, :], frame[cx4, cy4, :], frame[cx5, cy5, :]])
        index += 1

    index = 0
    for ctr in contours:
        m = cv2.mean(ctr)
        org = int(m[0]), int(m[1])
        org_step = int(m[0]+10), int(m[1]+10)
        # cv2.putText(frame, "pill", org, cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        # color[index] = [255 255 255]
        if np.array_equal(color[index], np.array([255,255,255])):
            area = cv2.contourArea(ctr)
            if area > 3000.0:
                color_str = "10"
            elif 3000.0 > area and area > 1000.0:
                color_str = "7"
            else: 
                color_str = "9" 
        elif np.array_equal(color[index], np.array([0,223,223])):
            color_str = '5'    
        elif np.array_equal(color[index], np.array([158,148,255])):
            color_str = '6'
        elif np.array_equal(color[index], np.array([212,255,255])):
            color_str = '8'
        elif np.array_equal(color[index], np.array([255,60,251])):
            color_str = '2'
        elif np.array_equal(color[index], np.array([204,244,0])):
            color_str = '1'                
        else:
            if any([np.array_equal(x, np.array([0,0,0])) for x in colors[index]]):
                color_str = '3'
                # print color2[index], color3[index], color4[index], color5[index]
            else: 
                color_str = '4'

        cv2.putText(frame, color_str, org, cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        #cv2.putText(frame, str(index), org_step, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        index +=1
    return frame

if __name__ == "__main__":
    pills = cv2.imread('pill.png')
    print pills.shape
    cv2.imshow('pill challenge',imgproc(pills))
    cv2.waitKey(0)