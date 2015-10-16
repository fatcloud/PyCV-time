## Augmented Reality

## 問題
利用feature matching抓出棋盤格的的pose，並且在圖像空間中投射出3D的箭頭。

### 用法

```
python AR_realtime.py
```

程式會開啟棋盤格畫面的視窗，以及攝影機目前的畫面。如果程式在攝影機畫面中偵測到棋盤格，
將會在內部做校正，找出棋盤格代表平面的<x, y, z>，並且將三個代表的小向量投影在棋盤平面上。

![chessboard](chessboard.jpg)


![results](result.png)




