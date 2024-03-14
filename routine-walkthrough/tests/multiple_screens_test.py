import sys
from PyQt6.uic import load_ui
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog, QApplication

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        load_ui("screen.ui",self)
        self.button.clicked.connect(self.gotoScreen2)

    def gotoScreen2(self):
        screen2 = Screen2()
        widget.addWidget(screen2)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Screen2(QDialog):
    def __init__(self):
        super(Screen2, self).__init__()
        load_ui("screen2.ui",self)
        self.button.clicked.connect(self.gotoScreen1)

    def gotoScreen1(self):
        mainwindow = MainWindow()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)

app =QApplication(sys.argv)
widget=QtWidgets.QStackedWidget()
mainwindow = MainWindow()

widget.addWidget(mainwindow)
widget.add(Screen2)
widget.setFixedHeight(300)
widget.setFixedWidth(400)
widget.show()

try:
    sys.exit(app.exec())
except:
    print("Exiting")