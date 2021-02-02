#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaomo
@license: (C) Copyright 2021-2030, Node Supply Chain Manager Corporation Limited.
@contact: 2572225959@qq.com
@software: QUST
@file: QlineEditValidator.py.py
@time: 2021/1/29 22:53
@desc:
'''
from PyQt5.QtCore import QRegExp
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtGui import QRegularExpressionValidator,QIntValidator,QDoubleValidator,QRegExpValidator

class QlineEditValidator(QWidget):
    def __init__(self):
        super(QlineEditValidator, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('教验器')

        #创建表单布局
        formLayout = QFormLayout(self)

        intLineEdit = QLineEdit()
        doubleLineEdit = QLineEdit()
        validatorLineEdit = QLineEdit()

        formLayout.addRow("整型",intLineEdit)
        formLayout.addRow("浮点型",doubleLineEdit)
        formLayout.addRow("数字和字母",validatorLineEdit)

        #int validator
        intValidator = QIntValidator(self)
        intValidator.setRange(1,99)

        #double validator
        doubleValidator=QDoubleValidator(self)
        doubleValidator.setRange(-360,360)
        doubleValidator.setNotation(QDoubleValidator.StandardNotation)
        doubleValidator.setDecimals(2)


        #validator
        reg = QRegExp('[a-zA-Z0-9]+$')
        validator=QRegExpValidator()
        validator.setRegExp(reg)

        #设置jiaoyanqi
        intLineEdit.setValidator(intValidator)
        doubleLineEdit.setValidator(doubleValidator)
        validatorLineEdit.setValidator(validator)
        self.setLayout(formLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QlineEditValidator()
    main.show()
    sys.exit(app.exec_())

