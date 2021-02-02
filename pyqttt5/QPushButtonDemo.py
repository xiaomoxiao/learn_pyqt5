#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaomo
@license: (C) Copyright 2021-2030, Node Supply Chain Manager Corporation Limited.
@contact: 2572225959@qq.com
@software: QUST
@file: QPushButtonDemo.py.py
@time: 2021/2/1 23:17
@desc:
'''
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class QPushButtonDemo(QDialog):
    def __init__(self):
        super(QPushButtonDemo, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('QPushButton Demo')
        layout = QVBoxLayout()

        self.button1 = QPushButton('第一个')
        self.button1.setCheckable(True)
        self.button1.toggle()

        self.button2 = QPushButton('图像按钮')
        self.button2.setIcon(QIcon(QPixmap('./images/python.jpg')))
        self.button2.clicked.connect(lambda:self.whichButton(self.button2))

        self.button3 = QPushButton("bukeyong")
        self.button3.setEnabled(False)

        self.button4 = QPushButton('&Mybutton')
        self.button4.setDefault(True)
        self.button4.clicked.connect(lambda: self.whichButton(self.button4))
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)


        self.setLayout(layout)
        self.resize(400,300)
        self.button1.clicked.connect(lambda:self.whichButton(self.button1))
        self.button1.clicked.connect(self.buttonState)
    def whichButton(self,btn):
        print('被单击的按钮是<'+btn.text()+'>')
    def buttonState(self):
        if self.button1.isChecked():
            print('1选中')
        else:
            print('未选中')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QPushButtonDemo()
    main.show()
    sys.exit(app.exec_())
