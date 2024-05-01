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
from routine_select_ui import startUp
from json_back_end import back_end_setup as bes
"""
def startUp():
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()
"""
"""
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        routine = ["place_holder", "another_place_holder"]

        y = urs()
        y.setupUi(self, routine)
        y.show()
        #y = None

        #self.x = urv()
        #self.x.setupUi(self)
        #self.x.show()

        #y.open_viewer()
#flip routine_control and back_end_setup's position
"""
"""
class routine_control():# create different objects for each routine than save them as different objects if this
    def __init__(self):
        super().__init__()

        self.routines = self.get_routines()

    def breakdown_into_list(self):
        pass

    def update_routine(self):
        pass

    def rebuild_routine(self):
        pass
class back_end_setup():
    def __init__(self):
        super().__init__()
        self.routines = self.get_routines()

    def get_routines(self):
        self.routines = 0#insert the json here
        return 0

    def separate_routine(self):
        pass
    
    def rebuild_all_routines(self):
        pass

    def save_routines(self):
        pass"""

#verifying it works\/
#c = bes()
#c.rebuild_all_routines(c.get_keyholder(c.temp))
startUp()
