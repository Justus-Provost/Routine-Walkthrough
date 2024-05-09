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
)
from PyQt6 import QtCore, QtGui, QtWidgets

from routine_select_ui import Ui_RoutineSelect as urs
from routine_viewer_ui import Ui_RoutineViewer as urv
from routine_select_ui import startUp
from json_back_end import back_end_setup as bes

startUp()
