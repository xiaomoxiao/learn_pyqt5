import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPalette
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel


class QLableDemo(QWidget):
    def __init__(self):
        super(QLableDemo, self).__init__()
        self.init_ui()

    def init_ui(self):
        lable1 = QLabel(self)
        lable2 = QLabel(self)
        lable3 = QLabel(self)
        lable4 = QLabel(self)

        lable1.setText('<font color = yellow>这是一个文本标签.</font>')
        lable1.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window, Qt.blue)
        lable1.setPalette(palette)
        lable1.setAlignment(Qt.AlignCenter)

        lable2.setText("<a href='#'>欢迎使pythonGUI</a>")

        lable3.setAlignment(Qt.AlignCenter)
        lable3.setToolTip("这是一个图片标签")
        lable3.setPixmap(QPixmap("python.jpg"))
        lable4.setOpenExternalLinks(True)
        lable4.setText("<a href ='https://item.jd.com/12417265.html'>感谢关注《Python"
                       "从菜鸟到高手》</a>")
        lable4.setAlignment(Qt.AlignRight)
        lable4.setToolTip("这是一个超级链接")

        vbox = QVBoxLayout()
        vbox.addWidget(lable1)
        vbox.addWidget(lable2)
        vbox.addWidget(lable3)
        vbox.addWidget(lable4)

        lable2.linkHovered.connect(self.linkHovered)
        lable4.linkActivated.connect(self.linkClicked)
        self.setLayout(vbox)
        self.setWindowTitle("QLable 控件演示")

    def linkHovered(self):
        print("当鼠标划过label2")

    def linkClicked(self):
        print("当鼠标点击label4时")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLableDemo()
    # main.resize(400,300)
    main.show()
    sys.exit(app.exec_())







