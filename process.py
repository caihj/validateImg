#coding:utf-8

from PIL import Image



'''
分隔图像并显示，使用扫描线算法

'''

def imgTest():
    #img=Image.open('img/3a41a1c0-e211-11e6-a579-448a5b698537.jpg')
    #img=Image.open('img/3a212170-e211-11e6-9313-448a5b698537.jpg')
    img=Image.open('img/3b867dcf-e211-11e6-96f9-448a5b698537.jpg')
    #img=Image.open('img/3b6190ae-e211-11e6-ae12-448a5b698537.jpg')
    #img.show()
    #转换为灰度图像
    gray=img.convert('L')
    gray.show()
    #延水平方向遍历,统计竖直方向

    thresold=80
    table=[]
    for i in range(0,256):
        if i <thresold:
            table.append(0)
        else:
            table.append(1)
    bimg=gray.point(table,"1")
    bimg.show()
    print 'get',bimg.getpixel((1,1))

    horiPixMap=[]

    for i in range(0,bimg.width):
        p=0
        for j in range(0,bimg.height):
            p=p+  (bimg.getpixel((i,j))==0 if 1 else 0)
        print 'horiz',i,p
        horiPixMap.append(p)


    horiImg=Image.new('1',gray.size)
    print gray.size
    for i in range(0,len(horiPixMap)):
        if horiPixMap[i]>0:
            print i,horiPixMap[i]-1
            horiImg.putpixel((i,horiPixMap[i]-1),1)

    horiImg.show()

    beginIdx=0
    charLocation=[]
    for i in range(len(horiPixMap)):
        if horiPixMap[i]>0:
                pass
        else:
            if beginIdx!=i:
                charLocation.append((beginIdx,i))
                beginIdx=i
            beginIdx=beginIdx+1


    print charLocation


    for loc in charLocation:
        chImg=bimg.crop((loc[0],0,loc[1],bimg.height))
        h1=0
        h2=chImg.height


        for i in range(chImg.height):
            end=False
            for j in range(chImg.width):
                if chImg.getpixel((j,i))==0:
                    end=True
                    break
            if end:
                h1=i
                break
            print ' up is ',h1

        for i in range(chImg.height-1,-1,-1):
            end=False
            for j in range(chImg.width):
                if chImg.getpixel((j,i))==0:
                    end=True
                    break
            if end:
                h2=i
                break
        chImg.show()
        print chImg.size
        print (0,h1,chImg.width,h2)
        chImg2=chImg.crop((0,h1,chImg.width,h2+1))
        chImg2.show()
        

if __name__=='__main__':
    imgTest()



