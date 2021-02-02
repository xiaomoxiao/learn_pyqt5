#!/usr/bin/env python
# encoding: utf-8
'''
@author: Xiaomo
@license: (C) Copyright 2021-2030, Node Supply Chain Manager Corporation Limited.
@contact: 2572225959@qq.com
@software: QUST
@file: QTextEditdemo.py.py
@time: 2021/2/1 22:33
@desc:
'''


from PyQt5.QtWidgets import *
import sys


class QtextEditDemo(QWidget):
    def __init__(self):
        super(QtextEditDemo, self).__init__()
        self.init_ui()
    def init_ui(self):
        self.setWindowTitle('Qlabel伙伴关系')
        self.resize(300,320)

        self.textEdit = QTextEdit()
        self.buttonText = QPushButton("显示文本")
        self.buttonHTML = QPushButton("显示HTML")

        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.buttonText)
        layout.addWidget(self.buttonHTML)
        self.setLayout(layout)
        self.buttonText.clicked.connect(self.onClick_ButtonText)
        self.buttonHTML.clicked.connect(self.onClick_ButtonHTML)

    def onClick_ButtonText(self):
        self.textEdit.setPlainText('hello world')
    def onClick_ButtonHTML(self):
        self.textEdit.setHtml('<font color = "blue" size = "5">hello world</font>')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QtextEditDemo()
    main.show()
    sys.exit(app.exec_())