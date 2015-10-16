概述
使用python利用棋盤格來校正攝影機的像差

中心概念
利用兩張圖片中棋盤格不同的旋轉角度及位置平移來計算matrix of intrinsic parameters
  |fx 0 Cx|
A=|0 fy Cy|
  |0  0  1|
fx,fy為攝影機的焦距
Cx,Cy為影像的中心的偏差

主要是利用影像中棋盤格的角點位置比較來達成我們要的攝影機內部校正
核心函數
cv2.findChessboardCorners 找出棋盤格的角點
cv2.calibrateCamera  校正相機內部參數
