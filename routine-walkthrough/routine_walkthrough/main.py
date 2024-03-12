import sys

#from routine_walkthrough import routines
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
# idea create a separate widget that the main window opens
morning = {"get dressed": "put on clothes to match the weather.","eat breakfast": "toast or an egg.","brush teeth": "red toothbrush and blue toothpaste."}

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        label = QLabel("Hello!")
        label = QLabel(self.testingJson())
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        #morning = {"get dressed": "put on clothes to match the weather.","eat breakfast": "toast or an egg.","brush teeth": "red toothbrush and blue toothpaste."}


        button_action = QAction(QIcon("bug.png"), "&Routine 1", self)
        button_action.setStatusTip("This is your first created routine")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        button_action.triggered.connect(self.checkDataFormat)
        toolbar.addAction(button_action)

        toolbar.addSeparator()

        button_action2 = QAction(QIcon("bug.png"), "Routine &2", self)
        button_action2.setStatusTip("This is your button2")
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        button_action2.setCheckable(True)
        button_action2.triggered.connect(self.testingJson)
        toolbar.addAction(button_action2)

        #toolbar.addWidget(QLabel("Hello"))
        #toolbar.addWidget(QCheckBox())

        self.setStatusBar(QStatusBar(self))

        menu = self.menuBar()

        file_menu = menu.addMenu("&File")
        file_menu.addAction(button_action)
        file_menu.addSeparator()

        file_submenu = file_menu.addMenu("Submenu")
        file_submenu.addAction(button_action2)

    def onMyToolBarButtonClick(self, s):
        print("click", s)

    def testingJson(self):
        #json.dumps("routines")
        x = open("routine_walkthrough/routines.json", "r")
        #y = json.loads(x)
        y = json.loads(x.read())
        print(y)
        z = y['routines']
        print(z)
        print(type(z))
        for i in z:
            print("new one")
            print(i)
            print(type(i))
            for e in i:
                print("new layer")
                print(e)
                print(type(e))
                print(i[e])
                print(type(i[e]))
                for b in i[e]:
                    print("yet another layer")
                    print(type(b))
                    print(b)
                    for t in b:
                        print("yet another layer")
                        print(type(t))
                        print(t)
                        u = t
        return u
    
    #def iDontKnow(self):
    #    button_action = QAction(QIcon("bug.png"), "&Routine 1", self)
    #    button_action.setStatusTip("This is your first created routine")
    #    button_action.triggered.connect(self.onMyToolBarButtonClick)
    #    button_action.setCheckable(True)
    #    button_action.triggered.connect(self.checkDataFormat)
    #    self.toolbar.addAction(button_action)
    #    x.close()
    
    #def furtherTestingJson(self, z):
    #    for i in z:
    #        print(i)
    #        for e in i:
    #            print(e)

    def checkDataFormat(self, data): #this is temporary
        #morning = {"get dressed": "put on clothes to match the weather.","eat breakfast": "toast or an egg.","brush teeth": "red toothbrush and blue toothpaste."}
        for i in morning:
            print(i)
            print(morning[i])
            print(type([i]))
            print(type(morning[i]))

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()

"""def testingJson(self):
        #json.dumps("routines")
        x = open("routine_walkthrough/routines.json", "r")
        #y = json.loads(x)
        y = json.loads(x.read())
        print(y)
        print(y['routines'])
        for i in y['routines']:
            print("new one")
            print(i)
            for e in i:
                print("new layer")
                print(i[e])
                for b in e:
                    print("yet another layer")
                    print([b])
        x.close()"""
