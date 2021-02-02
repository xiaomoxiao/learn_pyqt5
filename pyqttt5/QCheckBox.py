#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaomo
@license: (C) Copyright 2021-2030, Node Supply Chain Manager Corporation Limited.
@contact: 2572225959@qq.com
@software: QUST
@file: QCheckBox.py
@time: 2021/2/2 13:31
@desc:
'''
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class QCheckBoxDemo(QDialog):
    def __init__(self):
        super(QCheckBoxDemo, self).__init__()
        self.init_ui()
    def init_ui(self):
        self.setWindowTitle('复选框控件演示')

        layout = QHBoxLayout()

        self.checkbox1 = QCheckBox('复选框控件1')
        self.checkbox1.setChecked(True)
        self.checkbox1.stateChanged.connect(lambda :self.checkBoxState(self.checkbox1))
        layout.addWidget(self.checkbox1)

        self.checkbox2 = QCheckBox('复选框控件2')
        self.checkbox2.setChecked(True)
        self.checkbox2.stateChanged.connect(lambda :self.checkBoxState(self.checkbox2))
        layout.addWidget(self.checkbox2)

        self.checkbox3 = QCheckBox('半选中')
        self.checkbox3.setTristate(True)
        self.checkbox3.setCheckState(Qt.PartiallyChecked)
        self.checkbox3.stateChanged.connect(lambda :self.checkBoxState(self.checkbox3))
        layout.addWidget(self.checkbox3)

        self.setLayout(layout)

    def checkBoxState(self,cb):
        check1Status = self.checkbox1.text() + ', isChecked=' + str(self.checkbox1.isChecked()) + ',checkState=' + str(self.checkbox1.checkState()) + '\n'
        check2Status = self.checkbox2.text() + ', isChecked=' + str(self.checkbox2.isChecked()) + ',checkState=' + str(self.checkbox2.checkState()) + '\n'
        check3Status = self.checkbox3.text() + ', isChecked=' + str(self.checkbox3.isChecked()) + ',checkState=' + str(self.checkbox3.checkState()) + '\n'
        print(check1Status + check2Status + check3Status)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QCheckBoxDemo()
    main.show()
    sys.exit(app.exec_())