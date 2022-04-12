# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 08:06:16 2021

@author: cleme
"""

import matplotlib.image as mpimg
from matplotlib import pyplot as plt
import imageio as iio
import numpy as np
import os as os
from PIL import Image
from tqdm import tqdm
##import usb1209 as usb1209

def convertbmp(x='I002557.bmp'): 
    im = iio.imread(x)
    iio.imsave(x+'B.jpg',im)
    return im

def convertjpgtomatrics(image0='imB.jpg'):
    img = iio.imread(image0)
##    plt.imshow(img, cmap='gray')
##    plt.show()
    return img

def file_convert():
    L = []
    path1 = '/home/clement/Documents/TIPE/PROPRE/JPG'
    listing = os.listdir(path1)
    for file in listing[:2]:
        im = Image.open(path1 + '/' + file)
        x= convertjpgtomatrics(path1 + '/' + file)
        L.append(x)
    return L

L = file_convert()

##def film_get(): 
##    l = usb1209()
##    L = convertbmp(l)
##    return L

def difference(img1, img2):
    mvm = img1-img2
    alpha = 1
    for i, e in np.ndenumerate(mvm):
        if e > alpha:
            e = 1
        else:
            e = 0
    mvm2 = mvm[0:2197,0:2197]
    plt.imshow(mvm2)
    plt.show()
    return mvm2

m = [difference(L[i],L[i+1]) for i in tqdm(range(len(L)-1))]
print(m[0][816][1912])
plt.show()
tcarre = 13 

def carre(img, i, j, tcarre=13):
    m = 0
    for c in range(tcarre):
        for l in range(tcarre):
            m = m+img[i+c][j+l]
    return m

def coordonnee(img):
    max_carre = 0
    a,b = 0,0
    for i in range(tcarre):
        for j in range(tcarre):
            v = carre(img,i,j)
            if v > max_carre:
                v = max_carre
                a,b = i,j
    return a,b

M = [coordonnee(m[i]) for i in tqdm(range(len(L)-1))]
print(M)
print('lol')
plt.plot(M[0],M[1])
plt.show()

def trace(film):
    L = film_get()
    n = len(L)
    x = np.zeros(len(L))
    y = np.zeros(len(L))
    for i, e in enumerate(L[:, n-2]):
        mvm = difference(L[i],L[i+1])
        a, b = coordonnee(mvm)
        x[i] = a 
        y[i] = b
    print(x,y)
    plt.plot(x,y)
    plt.show()
    return x,y

    
