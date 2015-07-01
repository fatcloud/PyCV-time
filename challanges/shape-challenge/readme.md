## 幾何挑戰 Shape Challenge!

### 概述

設計一個程式尋找相機畫面中的某種形狀，
先定義自己的目標，例如四邊形、長方形、正方形或三角形、五邊形，
再針對目標寫個小範例出來，
7/3 的拍電視時間 demo!

![shape_challenge](https://cloud.githubusercontent.com/assets/7896433/8407385/a81fce08-1e98-11e5-8657-49df326831f8.png)

### 參考程式碼

可以先下載 shape challenge 資料夾：[PyCV-time\challanges\shape-challenge](https://github.com/fatcloud/PyCV-time/tree/master/challanges/shape-challenge)
然後去修改 [find_polygon.py](https://github.com/fatcloud/PyCV-time/blob/master/challanges/shape-challenge/find_polygon.py) 裡的 TODO 區塊
來達成自己的目的


    # ================== TODO ===================
    
    # Modify these code to suit your need
    contours = [ctr for ctr in contours if cv2.contourArea(ctr) > 100]
    contours = [cv2.approxPolyDP(ctr, 5 , True) for ctr in contours]
    contours = [ctr for ctr in contours if cv2.isContourConvex(ctr)]
    
    # ============================================

### 提示

想要改進這個範例識別多邊形的能力大約有一千種方法，
舉例來說：

1. 可以比較被 approxPolyDP 簡化過的多邊形與原始形狀的面積比，
來確認形狀沒有被過度簡化。

2. 可以根據每個多邊形的尺寸（面積或週長？）代替上面的固定值 5 作為 approxPolyDP 簡化形狀時的容錯距離，
讓程式對大小不同的多邊形提供不同的逼近錯誤容忍值。

3. 如果想偵測特定邊數的多邊形，如三角形，也可以設立條件判斷 len( ctr) == 3 來確認 ctr 這條封閉路徑裡只有三個點。


### 資源

以下是一些用來對封閉路徑 (contour) 操作時可能派上用場的函數

- 算面積 area = cv2.contourArea(ctr)
- 算週長 perimeter = cv2.arcLength(ctr,True)
- 以多邊形逼近 approx = cv2.approxPolyDP(ctr, tolerance ,True)
- 確認一條路徑是凸多邊形 cv2.isContourConvex(ctr)
- 範例程式碼裡面的 drawContours(frame, contours, -1, (0,255,0), 3) 會把 contours 裡所有的封閉路徑畫出來，只要把參數 -1 換成 n 就可以只畫 contours[n] 那一條路徑

- 判斷是幾邊形可以靠 len 函數讀取說 contour 中包含幾個節點來得知
- 不要忘記，兩向量間的夾角可以用內積判定，這也不需要用到 opencv 的函數就能做到
- 在 python 的 opencv binding 中，所有的向量或圖片都是以數值運算套件 Numpy 使用的 numpy array 形式儲存，如果想要做向量加減法、內積外積等運算，可以搜尋 Numpy 的說明。

想更加了解如何在 python + opencv 環境下玩弄 contour，請見[教學](https://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_imgproc/py_contours/py_table_of_contents_contours/py_table_of_contents_contours.html#table-of-content-contours)，目前我對 opencv 的認識有一大半是來自這個教學網站。

如果你已經到達一個光看教學無法滿足的水準，也可以直接看[原始的 opencv api 文件](http://docs.opencv.org/modules/imgproc/doc/structural_analysis_and_shape_descriptors.html?highlight=contour#findcontours)