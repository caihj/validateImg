#coding:utf-8

import wget
import uuid

def getImg(url,savePath):
    print('get',url)
    saveName=savePath+'/'+str(uuid.uuid1())+'.jpg'
    print('save as',saveName)
    wget.download(url,saveName)
    return saveName


if __name__=='__main__':
    count=1000
    for i in range(0,count):
        print('get ',i)
        getImg('http://page2.dfpan.com/verifyimg/getPcv.html','C:/python_workspace/tools/validateImg/img')
