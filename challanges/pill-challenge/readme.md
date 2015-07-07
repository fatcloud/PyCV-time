![image](https://cloud.githubusercontent.com/assets/7896433/8547656/e15c3412-24f2-11e5-8d88-b1f9cc5a2f52.png)

(感謝 [曲新天](https://github.com/fatcloud/PyCV-time/blob/master/members/Sky%20introduction.pdf) 提供主題)

### 情境敘述

湯姆先生是一個退休的老人，生活非常的無聊。最近他為了尋找生命中的第二春，跑去參加相親認識了一個妹子叫安妮。安妮是一個護理師，她最近才因為送錯藥而險些被醫院開除。湯姆先生聽了安妮的遭遇，為了愛他決定用自己龐大的退休金中的九牛一毛發包寫個程式，自動化地辨認藥丸有沒有送錯，你能不能接下這個案子滿足他的需求呢？


### 藥丸挑戰

以下共有十種藥丸擺在綠色的背景上：

1. 淺藍色圓形小藥丸
2. 粉紅偏紫色長方形大藥丸
3. 紅黑膠囊
4. 紅白膠囊
5. 黃色橢圓藥丸
6. 皮膚色橢圓藥丸
7. 白熱橢圓形藥丸
8. 方形白色藥丸
9. 圓形白色小藥丸
10. 圓形白色大藥丸

試著寫一個程式，自動辨認影像中看到的藥丸，並且即時顯示編號。
（歡迎自行修改規則，再自行解決之！）
![pill](https://cloud.githubusercontent.com/assets/7896433/8550364/b3d8f6e6-2502-11e5-9f23-b1c0f60a4b00.png)


### 程式範例

讀圖片、抓藥丸邊緣路徑以及顯示文字的程式碼已經寫好在 [PyCV-time/challenges/pill_reconition.py](https://github.com/fatcloud/PyCV-time/blob/master/challanges/pill-challenge/pill_reconition.py)，
想參加挑戰只需尋找 TODO 部分插入自己的演算法即可。

    # ================== TODO ===================
    
    # Every pill is surrounded by a contour in variable "contours" now
    
    # ============================================

繳交挑戰內容請做成一個獨立的資料夾 push 到 [PyCV-time/challanges/pill-challenge](https://github.com/fatcloud/PyCV-time/tree/master/challanges/pill-challenge) 底下
