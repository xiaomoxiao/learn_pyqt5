import sys

from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QMainWindow, QHBoxLayout, QPushButton
from PyQt5.QtGui import QFont


class TooltipForm(QMainWindow):
    def __init__(self,parant = None):
        super(TooltipForm, self).__init__(parant)
        self.init_ui()

    def init_ui(self):
        QToolTip.setFont(QFont('consolas', 12))
        self.setToolTip('今天是<b>星期五</b>')
        self.setGeometry(300, 300, 200, 300)
        self.setWindowTitle('设置控件提示消息')
        self.button1 = QPushButton('我的按钮')
        self.button1.setToolTip('这是一个按钮')

        layout = QHBoxLayout()
        layout.addWidget(self.button1)
        mainFrom = QWidget()
        mainFrom.setLayout(layout)
        self.setCentralWidget(mainFrom)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = TooltipForm()
    # main.resize(400,300)
    main.show()
    sys.exit(app.exec_())
