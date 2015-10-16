##概述
使用python利用棋盤格來校正攝影機的像差

##中心概念
利用兩張圖片中棋盤格不同的旋轉角度及位置平移來計算matrix of intrinsic parameters <br>
A= <br>
|fx 0 Cx|<br>
|0 fy Cy|<br>
|0  0  1|<br>
fx,fy為攝影機的焦距 <br>
Cx,Cy為影像的中心的偏差<br>

主要是利用影像中棋盤格的角點位置比較來達成我們要的攝影機內部校正<br>
##核心函數<br>
  >cv2.findChessboardCorners<br>
  找出棋盤格的角點<br>
  >cv2.calibrateCamera  <br>
  校正相機內部參數<br>
