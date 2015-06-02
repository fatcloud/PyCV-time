import cv2
cvConst = [
    'CV_CAP_PROP_POS_MSEC'       ,# 'position (ms)'
    'CV_CAP_PROP_POS_FRAMES'     ,# 'frame number'
    'CV_CAP_PROP_POS_AVI_RATIO'  ,# 'position (%)'
    'CV_CAP_PROP_FRAME_WIDTH'    ,# 'frame width'
    'CV_CAP_PROP_FRAME_HEIGHT'   ,# 'frame height'
    'CV_CAP_PROP_FPS'            ,# 'frame rate'
    'CV_CAP_PROP_FOURCC'         ,# 'codec'
    'CV_CAP_PROP_FRAME_COUNT'    ,# 'total number of frame'
    'CV_CAP_PROP_FORMAT'         ,# 'Format of the Mat objects returned by retrieve() .'
    'CV_CAP_PROP_MODE'           ,# 'Backend-specific value indicating the current capture mode.'
    'CV_CAP_PROP_BRIGHTNESS'     ,# 'Brightness of the image (only for cameras).'
    'CV_CAP_PROP_CONTRAST'       ,# 'Contrast of the image (only for cameras).'
    'CV_CAP_PROP_SATURATION'     ,# 'Saturation of the image (only for cameras).'
    'CV_CAP_PROP_HUE'            ,# 'Hue of the image (only for cameras).'
    'CV_CAP_PROP_GAIN'           ,# 'Gain of the cameras'
    'CV_CAP_PROP_EXPOSURE'        # 'Exposure'
    ]


def cv_cap_set(capture, varname, value):
    capture.set(cvConst.index(varname), value)


def cv_cap_info(capture):
    info = "\n".join([item + ' = ' + str(capture.get(cvConst.index(item))) for item in cvConst])
    return info + "\n"
    
if __name__ == '__main__':
    cam = cv2.VideoCapture(0)
    while True:
        ret, frame = cam.read()
        cv2.imshow('info',frame)
        ch = 0xFF & cv2.waitKey(1)
        if ch == 27:
            break
        elif ch != None:
            print cv_cap_info(cam)