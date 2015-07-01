## 使用 Webcam

這個小實驗示範了要如何用 opencv 從網路攝影機讀取影像、
對它做灰階處理、
再顯示到一個視窗上。


### 用法

執行

	> python webcam.py

或者

	> python webcam_gui.py

就會跳出一個視窗，即時顯示灰階處理後的網路攝影機影像，畫面如下：

![](gray.png)

想關閉程式只要隨便按鍵盤上的任意鍵就行了，按右上角的 x 按鈕是沒有用的。

webcam\_gui.py 與 webcam.py 的功能是相同的，
差異僅在於 webcam\_gui.py 裡把啟動相機、顯示視窗、偵測鍵盤事件這些常用的功能包成單一的函數，像這樣：

	def webcam_gui(filter_func, video_src=0):
		...
		...

只要把


## 程式碼說明

	
首先引入 opencv 2 模組，
然後創造一個 VideoCapture 物件，
參數 0 會啟動連接電腦上的第一台相機相機。

	import cv2
	
	# initialize the video source
	cap = cv2.VideoCapture(0)

接著進入迴圈

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

	
這個迴圈裡的內容只有四行程式碼，依序解讀他的功能分別是：

1. 讀取影像存到 frame 裡

2. 把 frame 的顏色從藍綠紅彩色轉換成灰階

3. imshow 把影像用一個視窗顯示出來。

4. waitKey(10) 等待鍵盤命令 10ms，把收到的信號存入 key_code（沒信號的話會回傳 -1）

比較特別的是 imshow 與 waitKey 之間有種神秘的關係，
沒有呼叫 waitKey 之前，
imshow 只會創造視窗，不會顯示出任何畫面來。


	# When everything done, release the capture
	cap.release()
	cv2.destroyAllWindows()

最後，
cap.release() 關閉相機，
cv2.destroyAllWindows() 關閉所有視窗


## 練習

1. 修改 webcam\_gui.py，把最下方程式碼裡的 gray\_filter 改成 edge\_filter 再執行看看：

		if __name__ == "__main__":
	    	webcam_gui(edge_filter)

	程式畫面：
	

2. 承上閱讀 edge\_filter 這個函數的內容（一樣寫在 webcam_gui.py 裡），嘗試修改 Canny edge detectiion 的畫面再執行，看看會產生什麼差別。

2. 使用 threshold 函數把灰階處理過的影像依亮度門檻調成黑白影像再顯示出來，
參考做法：

		ret, frame_th = cv2.threshold(frame_gray, 127, 255, cv2.THRESH_BINARY)


	![](threshold.png)

	想更深入瞭解 threshold 可以參考 [教學](https://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_imgproc/py_thresholding/py_thresholding.html#thresholding)
	或者 [api 文件](http://docs.opencv.org/modules/imgproc/doc/miscellaneous_transformations.html#threshold)