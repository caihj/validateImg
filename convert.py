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
        try:
            os.mkdir('ch/'+str(i))
        except Exception,e:
            pass


    for img in os.listdir('ch'):
        print 'rename',img
        if len(img)==1:
            continue
        num = img.split('.')[1]
        os.rename('ch/'+img,'ch/'+num+'/'+img)

def restore():
    for i in range(10):
        for file in os.listdir('ch/'+str(i)):
            os.rename('ch/'+str(i)+'/'+file,'ch/'+file)

def delBad():
    for img in os.listdir('ch'):
        if len(img.split('.'))<=2:
            os.remove('ch/'+img)

if __name__=="__main__":
    delBad()
    os._exit(0)
    imgs= os.listdir('ch')
    for img in imgs:
        convert(img)


