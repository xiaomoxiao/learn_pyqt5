#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaomo
@license: (C) Copyright 2021-2030, Node Supply Chain Manager Corporation Limited.
@contact: 2572225959@qq.com
@software: QUST
@file: QlineEditMask.py.py
@time: 2021/1/29 23:34
@desc:
'''
from PyQt5.QtWidgets import *
import sys

class QlineEditMask(QWidget):
    def __init__(self):
        super(QlineEditMask,self).__init__()
        self.init_ui()
    def init_ui(self):
        self.setWindowTitle("用掩码显示QlineEdit控件的输入")
        formLayout =QFormLayout()
        ipLineEdit = QLineEdit()
        macLineEdit = QLineEdit()
        dataLineEdit = QLineEdit()
        licenseLineEdit = QLineEdit()

        ipLineEdit.setInputMask('000.000.000.000;_')
        macLineEdit.setInputMask('HH:HH:HH:HH:HH:HH;_')
        dataLineEdit.setInputMask('0000-00-00;_')
        licenseLineEdit.setInputMask('>AAAAA-AAAA-AAAA-AAAAA;#')

        formLayout.addRow('数字掩码',ipLineEdit)
        formLayout.addRow('mac掩码',macLineEdit)
        formLayout.addRow('日期掩码',dataLineEdit)
        formLayout.addRow('许可证掩码',licenseLineEdit)

        self.setLayout(formLayout)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    main = QlineEditMask()
    main.show()
    sys.exit(app.exec_())
