import cv2
import numpy as np


class undistortor:

	def __init__(self, cal_data = 'c525.npz'):
		self.cal_data = 'c525.npz'
		with np.load('c525.npz') as X:
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

	ud = undistortor('c525.npz')
	img = cv2.imread('img.jpg')

	cv2.imshow('compare',np.hstack([img, ud.apply(img, crop=False)]))
	cv2.waitKey(0)