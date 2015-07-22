import cv2
from cam import OpenCV_Cam

if __name__ == '__main__':
    cam = OpenCV_Cam()
    cam.size = (640,480)
    fourcc = cv2.cv.CV_FOURCC(*'XVID')
    video = cv2.VideoWriter('output.avi',fourcc, 30.0, (640,480))

    while True:
        img = cam.read()
        cv2.imshow('img', img)
        video.write(img)
        k = cv2.waitKey(1000)
        if k == 27:
            break

    cv2.destroyAllWindows()
    cam.release()
    video.release()