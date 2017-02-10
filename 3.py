#coding:utf-8

import numpy as np
import os
from PIL import Image

def nonlin(x,deriv=False):
    if(deriv==True):
        return x*(1-x)
<<<<<<< HEAD
    return 1/(1+np.exp(-x))
=======
    return 1/(1+np.exp(-x))*9
>>>>>>> master


np.random.seed(1)

# randomly initialize our weights with mean 0
syn0 = 2*np.random.random((165,10))-1
syn1 = 2*np.random.random((10,1))-1

def train(X,y):
    global syn0
    global syn1

    # Feed forward through layers 0, 1, and 2
    l0 = X
    l1 = nonlin(np.dot(l0,syn0))
    l2 = nonlin(np.dot(l1,syn1))

    # how much did we miss the target value?
    l2_error = y - l2

    # in what direction is the target value?
    # were we really sure? if so, don't change too much.
    l2_delta = l2_error*nonlin(l2,deriv=True)

    # how much did each l1 value contribute to the l2 error (according to the weights)?
    l1_error = l2_delta.dot(syn1.T)

    # in what direction is the target l1?
    # were we really sure? if so, don't change too much.
    l1_delta = l1_error * nonlin(l1,deriv=True)

    syn1 += l1.T.dot(l2_delta)
    syn0 += l0.T.dot(l1_delta)

def match(d):
    global syn0
    global syn1
    l1=nonlin(np.dot(d,syn0))
    l2=nonlin(np.dot(l1,syn1))
    return l2

def main():
    images=os.listdir('ch')
    i=0
    for img in images:
        print (" img name",img)
        im = Image.open("ch/"+img)
        arr = np.asarray(im,dtype="uint32")  #将img数据转化为数组形式
        l = []
        for ar in arr:
            for a in ar:
                l.append(a)

        label=img.split('.')[1]
        train(np.asanyarray([l]),np.asanyarray([[float(label)/10]]))


if __name__=='__main__':
    main()


    im=Image.open("ch/61e8e191-ea89-11e6-9cc8-448a5b698537.1.png")

    arr = np.asarray(im,dtype="float32")  #将img数据转化为数组形式
    l = []
    for ar in arr:
        for a in ar:
            l.append(a)

    print(match(np.asanyarray(l)))
