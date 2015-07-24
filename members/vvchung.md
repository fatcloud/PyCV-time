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

趕在第四週拍電視時間最終回聚會前把<a href="https://github.com/vvchung/PyCV-time/blob/master/challanges/pill-challenge/pill_reconition.py" target="_blank"> pill challenge </a>寫完：<br>
![](http://1.bp.blogspot.com/-hhjWTIYf6bY/VbHrMrmk09I/AAAAAAAAFQ8/FwdqDDNErUs/s1600/%25E8%259E%25A2%25E5%25B9%2595%25E6%2593%25B7%25E5%258F%2596%25E7%2595%25AB%25E9%259D%25A2%2B%252826%2529.png)

嘗試將「解決太陽眼鏡問題的神經網路模式辨識法」概念套用至 pill challenge (詳見<a href="http://book.tpml.edu.tw/webpac/bookDetail.do?id=628090" target="_blank">改變世界的九大演算法</a>第156-165頁) <br>
![](http://1.bp.blogspot.com/-eD52ZZB0o8k/VbHuZsAmaOI/AAAAAAAAFRI/kI_m8I75COE/s640/11760055_10203391002774391_8988689375344451608_n.jpg)

觀察一下 pill.png 這張圖裡頭 18 顆藥丸的特性，可以發現這 18 顆藥丸以中心點顏色和整體面積就大致上都可以成功區分，只有膠囊因為用中心點無法區分紅黑還是紅白膠囊，所以需要向左向右向上向下再取四點看顏色是黑是白來判定：<br>
![](http://4.bp.blogspot.com/-7sruBEZdZfM/VbHvft7MC4I/AAAAAAAAFRU/SnpGxUSd5Bs/s640/%25E8%259E%25A2%25E5%25B9%2595%25E6%2593%25B7%25E5%258F%2596%25E7%2595%25AB%25E9%259D%25A2%2B%252828%2529.png)

就這樣用偷吃步完成了 pill challenge。但是 Cloud 第一週交代要做的 shape challenge 還是沒有練習到如何以 OpenCV 進行圓形的判斷，所以再試著用 <a href="http://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_imgproc/py_houghcircles/py_houghcircles.html" target="_blank">HoughCircles 函數</a>做也長得圓圓的<a href="https://github.com/vvchung/PyCV-time/blob/master/challanges/shape-challenge/vivi/adipose_test.py" target="_blank">脂肪細胞自動辨識</a>：<br>
![](http://3.bp.blogspot.com/-yH2txfYyc0s/VbHzR6sCCOI/AAAAAAAAFRk/T43wopH4zhI/s320/11742668_10203418827910002_5771784882026363514_n.jpg)

![](http://4.bp.blogspot.com/-DHg-upKGTuU/VbH0OLdhBGI/AAAAAAAAFRo/thFydH4pQ8s/s640/11013407_10203418829110032_1950908097246470430_n.jpg)

想要練習做做看脂肪細胞自動辨識是因為 <a href="http://diamond.cs.cmu.edu/applications.html" target="_blank">CMU</a> 有跟 Merck 合作、用 OpenCV-Delphi 開發出一個 <a href="https://github.com/cmusatyalab/fatfind" target="_blank">FatFind</a>：<br>
![](http://3.bp.blogspot.com/-qn-fYd0-hZE/VbH5_EnKneI/AAAAAAAAFR4/qNPinCnRt6E/s320/11703164_10203391111057098_6520747805327944030_n.jpg)

我第一個參與的新藥開發計畫是抗肥胖藥物開發~ <br>
![](https://fbcdn-sphotos-a-a.akamaihd.net/hphotos-ak-xaf1/v/t1.0-9/188846_1011287021057_7970027_n.jpg?oh=f7aaa673a641a8e2e791c156030d2e49&oe=561A0127&__gda__=1447864846_951c65900bcf16698462d6ad5f57171c)

以上是這一個月來跟大家一起學習 OpenCV 的成果報告。順便記錄一下遇到過的最有名的 OpenCV-Python Tutroals 學習障礙: I get a <a href="http://stackoverflow.com/questions/22241474/i-get-a-error-when-using-houghcircles-with-python-opencv-that-a-module-is-missin" target="_blank">error</a> when using <a href="http://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_imgproc/py_houghcircles/py_houghcircles.html" target="_blank">HoughCircles</a> with Python OpenCV that a module is missing ─ <br>

![](http://1.bp.blogspot.com/-v-BG8GRbZvc/VbH_-RlCInI/AAAAAAAAFSI/A80ZPAI3-qU/s640/HOUGH_GRADIENT.png)

解決辦法是參照 PyImageSearch 的 <a href="http://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_imgproc/py_houghcircles/py_houghcircles.html" target="_blank">Detecting Circles in Images using OpenCV and Hough Circles</a>，把 OpenCV-Python Tutroals 範例程式碼裡頭的 cv2.HOUGH_GRADIENT 改成 **cv2.cv.CV_HOUGH_GRADIENT**： <br>
![](http://4.bp.blogspot.com/-oXfjzkuW4zY/VbICLppoSnI/AAAAAAAAFSU/aQW_zAfOaRg/s1600/HOUGH_GRADIENT_2.png)

這樣 HoughCircles 函數就能正常運作了。










