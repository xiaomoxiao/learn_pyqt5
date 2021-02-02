#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaomo
@license: (C) Copyright 2021-2030, Node Supply Chain Manager Corporation Limited.
@contact: 2572225959@qq.com
@software: QUST
@file: qSliderDemo.py
@time: 2021/2/2 14:30
@desc:
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class QSliderDemo(QWidget):
    def __init__(self):
        super(QSliderDemo, self).__init__()
        self.init_ui()
    def init_ui(self):
        self.setWindowTitle('滑块控件')
        self.resize(400,700)

        layout = QVBoxLayout()
        self.label = QLabel('你好 Pyqt5')
        self.label.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.label)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(12)
        self.slider.setMaximum(48)
        self.slider.setSingleStep(3)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(6)

        layout.addWidget(self.slider)
        self.slider.valueChanged.connect(self.valueChange)

        self.slider1 = QSlider(Qt.Vertical)
        self.slider1.setMinimum(10)
        self.slider1.setMaximum(60)
        self.slider1.setSingleStep(5)
        self.slider1.setTickPosition(QSlider.TicksBelow)
        self.slider1.setTickInterval(6)
        self.slider1.valueChanged.connect(self.valueChange)

        layout.addWidget(self.slider1)
        self.setLayout(layout)

    def valueChange(self):
        print('当前值是%s'%self.sender().value())
        size = self.sender().value()
        self.label.setFont(QFont('Arial',size))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QSliderDemo()
    main.show()
    sys.exit(app.exec_())
