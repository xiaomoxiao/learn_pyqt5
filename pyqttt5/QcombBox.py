#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaomo
@license: (C) Copyright 2021-2030, Node Supply Chain Manager Corporation Limited.
@contact: 2572225959@qq.com
@software: QUST
@file: QcombBox.py
@time: 2021/2/2 14:09
@desc:
'''
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class QCombBoxDemo(QWidget):
    def __init__(self):
        super(QCombBoxDemo, self).__init__()
        self.init_ui()
    def init_ui(self):
        self.setWindowTitle('下拉控件')
        layout = QVBoxLayout()

        self.label = QLabel('选择编程语言')
        self.cb = QComboBox()
        self.cb.addItem('C++')
        self.cb.addItem('Python')
        self.cb.addItems(['Java','C#','Ruby'])

        self.cb.currentIndexChanged.connect(self.selectionChange)
        self.resize(300,200)
        layout.addWidget(self.label)
        layout.addWidget(self.cb)
        self.setLayout(layout)
    def selectionChange(self,i):
        self.label.setText(self.cb.currentText())
        self.label.adjustSize()

        for count in range(self.cb.count()):
            print('item' + str(count) + '=' + self.cb.itemText(count))
        print('current index', i, 'selection changed', self.cb.currentText())
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QCombBoxDemo()
    main.show()
    sys.exit(app.exec_())
