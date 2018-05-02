# -*- coding: utf-8 -*-
"""
Created on Tue May  1 22:23:48 2018

@author: LWC
"""
import numpy as np
import imageio as img
#import cv2
from matplotlib import pyplot as plt
figure = plt.figure(figsize=(4, 3), dpi = 100) #設定figure的大小和dpi

"""load the images"""
PATH = "E:/Google 雲端硬碟 (410421227@gms.ndhu.edu.tw)/課程/(三下) 機器學習/Assignment_1/ML2018_410421227/Image_and_ImageData/"
#設定路徑
"""
key1 = cv2.imread(PATH + "key1.png")
key2 = cv2.imread(PATH + "key2.png")
I = cv2.imread(PATH + "I.png")
E = cv2.imread(PATH + "E.png")
Ep = cv2.imread(PATH + "Eprime.png")
"""
key1 = img.imread(PATH + "key1.png") #讀取加密圖1
key2 = img.imread(PATH + "key2.png") #讀取加密圖2
I = img.imread(PATH + "I.png") #讀取加密前圖
E = img.imread(PATH + "E.png") #讀取加密後圖
Ep = img.imread(PATH + "Eprime.png") #讀取解鎖圖

"""setting parameters & randomiz weight"""
lr = 0.00001 #learning rate
mil = 10 #MaxIterLimit
epoch = 1
weight = np.random.rand(3) #隨機生成權重的初始值

"""training"""
while (epoch == 1 or epoch < mil):
    for w in range (0, 300):
        for h in range (0, 400):
            a = weight[0] * key1[w][h] + \
                weight[1] * key2[w][h] + \
                weight[2] * I[w][h]
            e = E[w][h] - a
            weight[0] += lr * e * key1[w][h]
            weight[1] += lr * e * key2[w][h]
            weight[2] += lr * e * I[w][h]
        epoch += 1
ans = (Ep - (weight[0] * key1) - (weight[1] * key2)) / weight[2]

"""draw and show"""
plt.axis("off") #隱藏坐標軸
plt.imshow(ans, cmap = "gray") #顯示為灰度圖
plt.show()
print ("The weight is ", weight)