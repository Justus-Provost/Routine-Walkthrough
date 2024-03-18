#this runs the rest of the program
import sys

import json
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QLabel,
    QMainWindow,
    QStatusBar,
    QToolBar,
    #QDialog #experiment
)
from PyQt6 import QtCore, QtGui, QtWidgets

from routine_select_ui import Ui_RoutineSelect as urs
from routine_viewer_ui import Ui_RoutineViewer as urv

def startUp():
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        y = urs()
        y.setupUi(self)
        y.show()

        
startUp()
