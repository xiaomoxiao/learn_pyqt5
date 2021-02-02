#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaomo
@license: (C) Copyright 2021-2030, Node Supply Chain Manager Corporation Limited.
@contact: 2572225959@qq.com
@software: QUST
@file: QlineEditEchoMode.py.py
@time: 2021/1/29 22:29
@desc:
'''
from PyQt5.QtWidgets import *
import sys

class QlineEditMode(QWidget):
    def __init__(self):
        super(QlineEditMode,self).__init__()
        self.init_ui()
    def init_ui(self):
        self.setWindowTitle("文本输入框回显模式")

        formLayout = QFormLayout(self)

        normalLineEdit = QLineEdit()
        noEchoLineEdit = QLineEdit()
        passwordLineEdit = QLineEdit()
        passwordEchoOnEditLineEdit = QLineEdit()

        formLayout.addRow("Normal",normalLineEdit)
        formLayout.addRow("NoEcho",noEchoLineEdit)
        formLayout.addRow("password",passwordLineEdit)
        formLayout.addRow("EchoPassword",passwordEchoOnEditLineEdit)

        #placeholdertext
        normalLineEdit.setPlaceholderText("Normal")
        noEchoLineEdit.setPlaceholderText("NoEcho")
        passwordLineEdit.setPlaceholderText("password")
        passwordEchoOnEditLineEdit.setPlaceholderText("Echopassword")

        normalLineEdit.setEchoMode(QLineEdit.Normal)
        noEchoLineEdit.setEchoMode(QLineEdit.NoEcho)
        passwordLineEdit.setEchoMode(QLineEdit.Password)
        passwordEchoOnEditLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)



if __name__ == '__main__':

    app = QApplication(sys.argv)
    main = QlineEditMode()
    main.show()
    sys.exit(app.exec_())
