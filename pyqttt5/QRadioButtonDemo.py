#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaomo
@license: (C) Copyright 2021-2030, Node Supply Chain Manager Corporation Limited.
@contact: 2572225959@qq.com
@software: QUST
@file: QRadioButtonDemo.py
@time: 2021/2/2 13:15
@desc:
'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class QRadioButtonDemo(QDialog):
    def __init__(self):
        super(QRadioButtonDemo, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('QRadioButton')
        layout = QHBoxLayout()
        self.button1 = QRadioButton('单选按钮1')
        self.button1.setChecked(True)
        self.button1.toggled.connect(self.buttonStatae)
        layout.addWidget(self.button1)

        self.button2 = QRadioButton('单选按钮2')
        self.button2.setChecked(True)
        self.button2.toggled.connect(self.buttonStatae)
        layout.addWidget(self.button2)
        self.setLayout(layout)


    def buttonStatae(self):
        radioButton = self.sender()

        if radioButton.isChecked()==True:
            print('<'+ radioButton.text()+'>被选中状态')
        else:
            print('<'+ radioButton.text()+'>被取消选中状态')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QRadioButtonDemo()
    main.show()
    sys.exit(app.exec_())