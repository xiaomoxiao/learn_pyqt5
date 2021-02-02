import sys
from PyQt5.QtWidgets import QPushButton,QHBoxLayout,QWidget,QMainWindow,QApplication

class QuitApp(QMainWindow):
    def __init__(self,parant = None):
        super(QuitApp, self).__init__(parant)
        self.setWindowTitle('first')
        self.resize(400,300)


        #添加button
        self.button1 = QPushButton('退出应用程序')
        self.button1.clicked.connect(self.onClick_button1)
        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        mainFrame = QWidget()

        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)

    def onClick_button1(self):
        sender = self.sender()
        print(sender.text()+"被按下")
        app = QApplication.instance()
        app.quit()

if __name__=='__main__':
    app = QApplication(sys.argv)
    print("1")
    main = QuitApp()
    print("2")
    #main.resize(400,300)
    main.show()
    sys.exit(app.exec_())
