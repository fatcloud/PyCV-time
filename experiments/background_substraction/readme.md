reference: http://docs.opencv.org/master/d1/dc5/tutorial_background_subtraction.html

## Background subtraction (BS) 

### 說明:
Background subtraction (背景相減)，簡單說是下一個frame減掉現在的frame，一般來說影像相減時會得到一個全黑的畫面，但此時如果物體有移動的話，移動的物件會因為和靜態的背景有明顯的差別，所以可以清楚的看到變化的地方。


<center><img src="http://docs.opencv.org/master/Background_Subtraction_Tutorial_Scheme.png"></img></center>

### 用法:
python motion_detect.py

### 結果
物件沒有移動:全黑
<img src="https://github.com/fatcloud/PyCV-time/blob/master/experiments/background_substraction/opencv%20bs-1.PNG"></img>

物件有移動: 移動的地方有變化
<img src="https://github.com/fatcloud/PyCV-time/blob/master/experiments/background_substraction/opencv%20bs-2.PNG"></img>


#### Background modeling 會考慮到下面兩點:

-- 背景初始化

-- 背景更新 



Noah 20151016
