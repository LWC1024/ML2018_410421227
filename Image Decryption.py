# -*- coding: utf-8 -*-
"""
Created on Tue May  1 22:23:48 2018

@author: LWC
"""
import numpy as np
import imageio as img
from matplotlib import pyplot as plt
figure = plt.figure(figsize=(4,3), dpi = 100)

PATH = 'E:/Google 雲端硬碟 (410421227@gms.ndhu.edu.tw)/課程/(三下) 機器學習/Assignment_1/ML2018_410421227/Image_and_ImageData/'
key1 = img.imread(PATH + 'key1.png')
key2 = img.imread(PATH + 'key2.png')
E = img.imread(PATH + 'E.png')
Ep = img.imread(PATH + 'Eprime.png')
I = img.imread(PATH + 'I.png')

lr = 0.00001
mil = 10
epoch = 1
weight = np.random.rand(3)

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

ans = (Ep - (weight[0]*key1) - (weight[1]*key2)) / weight[2]
plt.axis('off')
plt.imshow(ans, cmap = 'gray')
plt.show()
print (weight)