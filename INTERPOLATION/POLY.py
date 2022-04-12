import numpy as np

def produit(x,j):
    p=[1]
    a=x
    b=a.pop(a[j])
    for i in a:
       for i in len(p):
           p[i+1] = p[i-1]/(b-x[i])
           p[i] *= x[i]/(b-x[i]) 

def interpolation(x,y):
    l=[]
    for j in len(x):
        P=produit(x,j)
        L +=y[j]*P
    return L
