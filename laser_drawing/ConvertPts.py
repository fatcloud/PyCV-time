import cv2

def calibrate(image_name, frame):
	"""
	Input : None
	Output
	"""
	MATCH_THRESHOLD = 10
    FLANN_INDEX_KDTREE = 0
    AREA_THRESHOLD = 1000

	detector = cv2.SIFT()
    ref_img = cv2.imread(image_name, 0)
    kp1, des1 = detector.detectAndCompute(ref_img, None)
    kp2, des2 = detector.detectAndCompute(frame, None)
    
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks = 50)
    flann = cv2.FlannBasedMatcher(index_params, search_params)
    
    matches = flann.knnMatch(des1,des2,k=2)
    
    # Perform Lowe's ratio test to select good points to proceed with.
    good = [m for m,n in matches if m.distance < 0.7*n.distance]
            
    src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1,1,2)
    dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1,1,2)
    
    # check the property of the corners found out there
    screen2cam_matrix, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)
    matchesMask = mask.ravel().tolist()

    h,w = ref_img.shape
    pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
    screen_corners = cv2.perspectiveTransform(pts, screen2cam_matrix)
    
    
    if False in [cv2.isContourConvex(screen_corners),
                 cv2.contourArea(screen_corners) > AREA_THRESHOLD,
                 sum(matchesMask) > MATCH_THRESHOLD]:
    
        screen2cam_matrix = None
        screen_corners = None
        
        return False
    
    cam2screen_matrix, _ = cv2.findHomography(dst_pts, src_pts, cv2.RANSAC,5.0)
            
	return cam2screen_matrix

def mapping(M):
    def f(X):
        return cv2.perspectiveTransform(X, M)
    return f
