## differential_screen_tracker

### 用法

利用Camera 拍攝程式產生閃爍畫面後，
程式將該閃爍區域獨立顯示，
例如將該閃爍區域放置於例如顯示器或投影機畫面中，
可用於自動尋找真實空間中的ROI(Region of Interest)。


我們將產生指定大小的黑白閃爍'main'視窗，
'screen finder'視窗會持續顯示Camera的影像， 
此時Camera將會利用MotionDetector()尋找出該區域， 
並將閃爍區域分離出來(此時將停止閃爍)， 
獨立顯示於'topview'視窗。

若是失敗或想重新調整則按"r"。



### 其他檔案的功能

- cam.py
	
  作者自寫的模組，方便用來調整相機亮暗、影像尺寸等參數

- motion_detect.py
  
  用來找出閃爍區域

- find_polygons.py
  
  傳回閃爍區域的四個角落座標

