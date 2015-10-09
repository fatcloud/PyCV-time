## 概述

這個範例展示如何用棋盤圖來校正攝影機的像差



## 使用方法

這個範例包含了三隻小程式，使用新相機時必須依序執行。

1. cam.py
2. calibrate.py
3. undistort.py


### cam.py

正常的執行順序是先用播放相片軟體開啟　chessboard.jpg，讓螢幕顯示黑白的西洋棋盤，接著執行

	> python cam.py

程式啟動後，會出現一個即時預覽視窗，只要按下空白鍵就可以拍照存到 calibratin_shot 這個資料夾裡。

把相機對準黑白的棋盤，拍十四張以上的影像（越多越好），完成後按 Esc 關閉 cam.py


### calibrate.py

只要確認 calibration_shot 裡面有超過十四張影像，就可以開始執行校正。

	> python calibrate.py

執行完將算出一個校正矩陣的資料 calibration_shots.npz


### undistort.py

執行

	> python undistort.py

畫面中將顯示兩張圖片，左邊是未經校正，右圖是校正後的成品。
