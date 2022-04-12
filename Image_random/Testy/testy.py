import turtle as tr
import numpy as np
from tk import *
from PIL import Image
import os as os
import imageio as iio
from matplotlib import pyplot as plt

tr.speed(0)
tr.color('black')

def bruit(x=0, y=0, r=10):
    l = [(1,1),(1,-1),(-1,1),(-1,-1)]
    for e in l:
        for i in range(100):
            tr.up()
            tr.goto(e[0] * np.random.randint(400), e[1] * np.random.randint(400))
            tr.down()
            tr.begin_fill()
            tr.circle(1)
            tr.end_fill()
        tr.up()
        tr.goto(0,0)
        tr.down()
    tr.ht()

def cercle(x=0, y=0, r=100):
    tr.reset()
    tr.up()
    tr.goto(x,y)
    tr.down()
    tr.begin_fill()
    tr.circle(10)
    tr.end_fill()

def generate_pos():
    x = np.random.randint(400, size=(1))[0] 
    y = np.random.randint(400, size=(1))[0]
    return x,y

def trace(x,y):
    tr.tracer(0, 0)
    tr.ht()
    cercle(x-200,y-200)
    bruit()
    tr.update()

def register_random(n=1):
    L=[]
    L3 = np.array([])
    for i in range(n):
        x,y = generate_pos()
        trace(x,y)
        s = tr.getscreen()
        L.append('random' + str(x) + str(y) + '.eps')
        tr.getcanvas().postscript(file='random' + str(x) + str(y) + '.eps')
        np.append(L3, [x,y])
    print(L3)
    return L3

def converteps_png(x):
    image_eps = x
    im = Image.open(image_eps)
    fig = im.convert('RGBA')
    image_png= str(x[:-4]) + '.png'
    fig.save(image_png, lossless = True)
    return image_png

def MAGIE(n=1):
    if n == 0:
        return 0
    Position = register_random(n)
##    L_png = converteps_png(L_eps)
    return Position

Position = MAGIE(1)
##fichier = open('pos.txt',w)
##               
##
def file_convert():
    L = []
    path1 = '/home/clement/Documents/TIPE/Image_random/Testy'
    listing = os.listdir(path1)
    for file in listing[:]:
        if file == 'testy.py':
            continue
        im = Image.open(path1 + '/' + file)
        x = converteps_png(path1 + '/' + file)
        L.append(x)
    return L

L = file_convert()

def convertjpgtomatrics(image0='imB.jpg'):
    img = iio.imread(image0)
##    plt.imshow(img, cmap='gray')
##    plt.show()
    return img

def allconvert():
    L = []
    L2 = []
    path1 = '/home/clement/Documents/TIPE/Image_random/Testy'
    listing = os.listdir(path1)
    for file in listing[:]:
        if file == 'testy.py':
            continue
        if file[-1] == 's':
            continue
        IMG = convertjpgtomatrics(file)
        L2.append(IMG)
    return L2 
        
L2 = allconvert()
print(L2)
