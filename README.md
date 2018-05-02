# Image Decryption using Linear Percetpron
>Machine Learning - Programming Asssignment1
## A. The way i prepare the training samples
>嘗試了opencv, PIL, matplotlib, scipy.misc, imageio，最後選擇imageio讀取圖片樣本
## B. All parameters i used for the training algorithm
* learning rate 學習率 = 0.00001
* MaxIterLimit 訓練次數上限 = 10
* epoch = 1
* weight 權重 = [,,] (用numpy.random隨機設定初始值)
## C. The derived weight vector w
* weight = [0.24914331 0.6613819 0.089239531]
## D. The printed image
![answer](https://github.com/LWC1024/ML2018_410421227/blob/master/Image_and_ImageData/answer.png)
## E. The problems i encountered
* opencv讀取圖片失敗
* matplotlib顯示圖片的參數設定
* 學習新的package和函式庫
* github desktop分支merge到master失敗
## F. I learned from this work
>一開始花了很多時間認識git和github，發現真是個非常方便的平台，很喜歡version的功能，以後會好好善用
>>
>試了各種讀取圖片的方法，如果使用PIL讀取的話需要從img轉換成array
>>
>卡在矩陣的型態很久，也找了很多matplotlib顯示圖片的參數要怎麼設定
>>
>雖然花了很多時間，但只要不要怕錯，打了就知道對不對了
>>
>最後也學到了readme.md的語法，對github也有了小小心得
>>
>當一切終於完成、答案揭曉後覺得很有成就感，收穫很多，是個很好的一次經驗
