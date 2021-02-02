#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaomo
@license: (C) Copyright 2021-2030, Node Supply Chain Manager Corporation Limited.
@contact: 2572225959@qq.com
@software: QUST
@file: Qlablebuddy.py.py
@time: 2021/1/29 22:00
@desc:
'''

from  PyQt5.QtWidgets import *
import sys

class QlabelBuddy(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.setWindowTitle('Qlabel伙伴关系')

        nameLabel = QLabel('Name',self)
        nameLineEdit = QLineEdit()

        nameLabel.setBuddy(nameLineEdit)

        passwordLabel = QLabel('&Password', self)
        passwordLabelEdit = QLineEdit()

        passwordLabel.setBuddy(nameLineEdit)

        btnOK = QPushButton('&ok')
        btnCancel = QPushButton('&cancel')

        mainLayout = QGridLayout(self)
        mainLayout.addWidget(nameLabel,0,0)
        #后边的两个数字是标明占用的行和列
        mainLayout.addWidget(nameLineEdit,0,1,1,2)

        mainLayout.addWidget(passwordLabel,1,0)
        mainLayout.addWidget(passwordLabelEdit,1,1,1,2)

        mainLayout.addWidget(btnOK,2,1)
        mainLayout.addWidget(btnCancel,2,2)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QlabelBuddy()
    main.show()
    sys.exit(app.exec_())
