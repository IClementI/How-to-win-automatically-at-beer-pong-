import turtle as tr
import numpy as np
from tk import *
from PIL import Image

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
    for i in range(n):
        x,y = generate_pos()
        trace(x,y)
        s = tr.getscreen()
        L.append('random' + str(x) + str(y) + '.eps')
        tr.getcanvas().postscript(file='random' + str(x) + str(y) + '.eps')
    return L

def parabole(x, a=-0.01, b=0, c=0):
    return a * x**2 + b * x + c

def gen_x(n):
    x=np.linspace(-200,200,n)
    return x

def gen_y(x):
    return parabole(x)


def trace_para(x,y):
    tr.tracer(0, 0)
    tr.ht()
    cercle(x,y)
    bruit()
    tr.update()

def register_para(n=10):
    L=[]
    x = gen_x(n)
    y = gen_y(x)
    for i in range(n):
        trace_para(x[i],y[i]+100)
        s = tr.getscreen()
        L.append('parabole' + str(x) + str(y) + '.eps')
        tr.getcanvas().postscript(file='parabole' + str(x) + str(y) + '.eps')
        print(s)
    return L


def converteps_png(x):
    image_eps = x
    im = Image.open(image_eps)
    fig = im.convert('RGBA')
    image_png= str(x[:,-4]) + '.png'
    fig.save(image_png, lossless = True)
    return image_png


def MAGIE(n=1):
    L_eps = register_random(n)
    L_png = converteps_png(L_eps)
    return L_png

MAGIE()

