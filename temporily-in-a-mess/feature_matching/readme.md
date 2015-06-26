## Feature Matching

### 用法

使用 SIFT 或 ORB 演算法做 feature matching 的範例，
以下命令都可以直接執行：

	python realtime_ORB.py
	python realtime_ORB.py

兩個命令都是開啟相機去找和預設圖片 matching 的影像，
差別只在於一個用 ORB 演算法，
一個用 SIFT 演算法。

如果你沒有外接的相機能拿來對著螢幕找預設圖片，
也可以按 's' 立刻拍照，
然後開始做 matching。

如果你的電腦完全沒有相機，也可以執行

	python SIFT.py



### 其他檔案的功能


- cam.py

	自寫的模組，方便用來調整相機亮暗、影像尺寸等參數

- fmatch.py
	
	這個模組裡只有 draw_match 這個函數重要，用來畫 feature matching 的結果

- mix.py

	用來把兩張圖合體在一張上