#coding:utf-8

from getImg import getImg
from process import imgTest
from KNN2 import imgToCode
from PIL import Image


def test():
    imgFile = getImg('http://page2.dfpan.com/verifyimg/getPcv.html','test')
    img=Image.open(imgFile)
    img.show()
    chlist = imgTest(imgFile)
    print chlist
    for ch in chlist:
        print imgToCode(ch)


if __name__=='__main__':
    test()
