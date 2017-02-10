#coding:utf-8

import os
from PIL import Image
import numpy as np

def convert(fileName):

   img=Image.open('ch/'+fileName)
   fp=open('bn/'+fileName+".bn",'w')

   for i in range(img.width):
       for j in range(img.height):
           #print(img.getpixel((i,j)))
           fp.write(chr(img.getpixel((i,j))))
   fp.close()

def classfier():
    for i in range(10):
        os.mkdir('ch/'+i)


    for img in os.listdir('ch'):
        num = img.split('.')[1]
        os.rename('ch/'+img,'ch/'+num+'/'+img)




if __name__=="__main__":
    imgs= os.listdir('ch')
    for img in imgs:
        convert(img)


