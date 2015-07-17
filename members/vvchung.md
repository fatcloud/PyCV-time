## 自我介紹
我是 vivia，<br>
![](http://1.bp.blogspot.com/-xUw-eoxefso/VY-jEqVV0wI/AAAAAAAAFN4/8nJzqAUJz9o/s640/%25E8%259E%25A2%25E5%25B9%2595%25E6%2593%25B7%25E5%258F%2596%25E7%2595%25AB%25E9%259D%25A2%2B%25282%2529.png)

我是唸生物的，<br>
![](http://2.bp.blogspot.com/-98v756CZj2M/VZYDXh9x3EI/AAAAAAAAFOU/YwUMkQo6Tk8/s640/%25E8%259E%25A2%25E5%25B9%2595%25E6%2593%25B7%25E5%258F%2596%25E7%2595%25AB%25E9%259D%25A2%2B%25284%2529.png)

因為PCR(polymerase chain reaction，聚合酶連鎖反應)是分子生物學最基本的實驗，但就算在中研院也不是每間生醫實驗室都買得起數位電泳照膠系統，目前正在發展中的開源硬體專案是迷你數位電泳照膠系統。<br>
![](http://2.bp.blogspot.com/-v-qsYtuVEQQ/VZYFBE_qmeI/AAAAAAAAFOg/3B8iW524tWI/s640/%25E8%259E%25A2%25E5%25B9%2595%25E6%2593%25B7%25E5%258F%2596%25E7%2595%25AB%25E9%259D%25A2%2B%25285%2529.png)

想學習OpenCV是因為PCR或蛋白質電泳分析都可以使用OpenCV:<br>
![](http://4.bp.blogspot.com/-KyM0qmIwSKs/VZYHGiQ_GuI/AAAAAAAAFOw/yYQqhi1wA8o/s640/%25E8%259E%25A2%25E5%25B9%2595%25E6%2593%25B7%25E5%258F%2596%25E7%2595%25AB%25E9%259D%25A2%2B%25287%2529.png)

第一個想拿來練習OpenCV-Python的專案是做個<a href="http://www.techbang.com/posts/16605-orientation-of-facial-recognition-marshmallow-blaster-you-want-to-buy" target="_blank">棉花糖大砲</a>送給小外甥:<br>
![](http://4.bp.blogspot.com/-u3ncNCPt1Ig/VZYJFaauhCI/AAAAAAAAFO8/SBAjajgf49s/s640/%25E6%2593%25B7%25E5%258F%2596_2015_07_03_12_00_28_798.png)

第一週練就了以OpenCV進行<a href="https://realpython.com/blog/python/face-recognition-with-python/" target="_blank">相片</a>和<a href="https://realpython.com/blog/python/face-detection-in-python-using-a-webcam/" target="_blank">即時攝影機</a>人臉辨識─ <br>
![](https://github.com/shantnu/FaceDetect/raw/master/abba_face_detected.jpg)

第二次聚會後跟 Cloud 借他做的步進馬達控制套組，想回家繼續研究棉花糖大砲的第二課：讓 webcam 跟著人臉移動！<br>
![](http://1.bp.blogspot.com/-Sjk6IkBVYYk/VahsC8IdD1I/AAAAAAAAFPo/gMwXZxWQa4E/s400/11403025_10203325463175942_3725439464351390920_n.jpg)

但是裝起來之後用 Arduino 的步進馬達範例程式測試，結果是不動如山... ← 這故事說明了用三用電表測線辨認迴路也是門需要好好修練的功課 ><~<br>
![](http://1.bp.blogspot.com/-zN0zb820f9U/VahuhN3hVHI/AAAAAAAAFP0/X4dSOeMIO4g/s640/stepper.png)

Cloud 介紹了另一種看起來更符合棉花糖大砲需求也更簡單的<a href="https://www.youtube.com/watch?v=SKEu29EbPZA" target="_blank">旋轉/平移台</a><br>
![](http://2.bp.blogspot.com/-AjxhVE6qwcY/VahxKRTzLhI/AAAAAAAAFQA/fFZVQTThnRM/s640/%25E8%259E%25A2%25E5%25B9%2595%25E6%2593%25B7%25E5%258F%2596%25E7%2595%25AB%25E9%259D%25A2%2B%252816%2529.png)

一點慧根都沒有的黑手指決定把硬體部份先放著 (就這樣了吧，呱~)
因為跟寫 OpenCV 作業一定要用的 <a href="https://www.kickstarter.com/projects/513736598/python-for-science-and-engineering" target="_blank">Numpy</a> 也還沒感情。。。<br>
![](http://4.bp.blogspot.com/--HYas712weI/Vah1ZLtFISI/AAAAAAAAFQU/6UYC4Sr5g1M/s640/Numpy.png)
![](http://1.bp.blogspot.com/-NeVAu4F21EU/Vah1SRHU2pI/AAAAAAAAFQM/obKMSn-XeXg/s640/python.png)

Numpy 翻完後再看看<a href="https://www.kickstarter.com/projects/513736598/python-for-science-and-engineering" target="_blank">一張圖到底可以怎麼分解它</a>─<br>
![](https://camo.githubusercontent.com/d140ee89e56d4400ee67a2ded13e6caaa09b32e8/687474703a2f2f7777772e7765686561727463762e636f6d2f77702d636f6e74656e742f75706c6f6164732f323031342f31322f686967686c6967687465642e6a7067)

可以抓出 pixcel 座標<br>
![](https://camo.githubusercontent.com/2e4a2097f7c2edde5287ee819cd267b2b425ec67/687474703a2f2f7777772e7765686561727463762e636f6d2f77702d636f6e74656e742f75706c6f6164732f323031342f31322f4247522e706e67)

可以單獨分出 RGB 或變成灰階<br>
![](https://camo.githubusercontent.com/ff25270925eaab7a69b214f92aad78fc8d70beb9/687474703a2f2f7777772e7765686561727463762e636f6d2f77702d636f6e74656e742f75706c6f6164732f323031342f31322f616c6c2e6a7067)

所以 pill challenge 目前的作業進度寫到 1) 抓出 18 顆藥丸中心座標和 BGR 值；2)顏色部份如果 BGR = (255,255,255) 就標定為 "W"，(0,255,255) 標定為 "Y"，其餘色碼先暫時顯示為 "?" <br>
![](http://3.bp.blogspot.com/-Gz_RDXrszQw/Vah8NMwykbI/AAAAAAAAFQk/5R04AuHZUEo/s640/%25E8%259E%25A2%25E5%25B9%2595%25E6%2593%25B7%25E5%258F%2596%25E7%2595%25AB%25E9%259D%25A2%2B%252819%2529.png)









