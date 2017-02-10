#coding:utf-8

from PySide.QtCore import *
from PySide.QtGui import *
import os
import sys

class LableWidget(QWidget):
    def __init__(self,parent=None):
        QWidget.__init__(self,parent)
        self.label=QLabel()
        layout=QHBoxLayout()
        layout.addWidget(self.label)

        self.setLayout(layout)
        self.fileName=''

        self.imgIte=LableWidget.getImg()

        self.updateImg()

    @staticmethod
    def getImg():
        imgs = os.listdir('ch')
        for img in imgs:
            if len(img.split('.'))==3:
                continue
            yield img
        yield None

    def updateImg(self):
        self.fileName = self.imgIte.next()
        pix = QPixmap("ch/"+ self.fileName)
        self.label.setPixmap(pix)

    def keyPressEvent(self,e):
        print e.key()
        label=int(e.key())-48;
        os.rename('ch/'+self.fileName,'ch/'+self.fileName.replace('png','')+str(label)+".png")

        self.updateImg()

if __name__=='__main__':
    app=QApplication(sys.argv)

    l=LableWidget()
    l.show()
    app.exec_()