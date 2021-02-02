import sys
from PyQt5.QtWidgets import QDesktopWidget,QMainWindow,QApplication

from PyQt5.QtGui import QIcon

class FirstMainWin(QMainWindow):
    def __init__(self,parant = None):
        super(FirstMainWin, self).__init__(parant)
        self.setWindowTitle('first')
        self.resize(400,300)
    def center(self):
        screen = QDesktopWidget.screenGeometry()
        size = self.geometry()
        newLeft = (screen.width()-size.width())/2
        newTop = (screen.height()-size.height())/2
        self.move(newLeft,newTop)



if __name__=='__main__':
    app = QApplication(sys.argv)
    main = FirstMainWin()
    main.show()
    sys.exit(app.exec_())
