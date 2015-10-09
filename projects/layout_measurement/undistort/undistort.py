import cv2
import numpy as np
from glob import glob



class undistortor:

	def __init__(self, cal_data = None):
		if cal_data is None:
			npz_mask = '*.npz'
			self.cal_data = glob(npz_mask)[0]
		else:
			self.cal_data = cal_data

		with np.load(self.cal_data) as X:
		    self.mtx, self.dist, _, _ = [X[i] for i in ('mtx','dist','rvecs','tvecs')]
	
	def apply(self, img, crop = True):
		h,  w = img.shape[:2]
		newcameramtx, roi=cv2.getOptimalNewCameraMatrix(self.mtx, self.dist,(w,h),1,(w,h))

		# undistort
		dst = cv2.undistort(img, self.mtx, self.dist, None, newcameramtx)

		# crop the image
		if crop is not True:
			return dst

		x,y,w,h = roi
		dst = dst[y:y+h, x:x+w]

		return dst

if __name__ == "__main__":

	ud = undistortor()
	img = cv2.imread('img.jpg')

	cv2.imshow('compare',np.hstack([img, ud.apply(img, crop=False)]))
	cv2.waitKey(0)