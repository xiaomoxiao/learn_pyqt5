import sys

from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow,QHBoxLayout,QPushButton

def on_Clicked():
    print("clicked")

app = QApplication(sys.argv)
widgt=QWidget()
btn = QPushButton(widgt)
btn.setText("按钮")
btn.move(24,52)
btn.clicked.connect(on_Clicked)
widgt.resize(300,240)
widgt.move(250,200)
widgt.setWindowTitle("屏幕居中")
widgt.show()
sys.exit(app.exec_())

