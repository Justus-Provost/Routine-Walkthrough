import sys

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

from routine_select_ui import Ui_RoutineSelect as urs
from routine_viewer_ui import Ui_RoutineViewer as urv
from routine_select_ui import startUp

if __name__ == "__main__":
    startUp()