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
    #QDialog #experiment
)
from PyQt6 import QtCore, QtGui, QtWidgets

from main_window_template_ui import Ui_MainWindow as umw
from second_window_template_ui import Ui_SecondWindow as usw
# idea create a separate widget that the main window opens
morning = {"get dressed": "put on clothes to match the weather.","eat breakfast": "toast or an egg.","brush teeth": "red toothbrush and blue toothpaste."}

def startUp():
    #app = QApplication(sys.argv)
    """w = MainWindow()
    w.__init__()
    w.show()
    app.exec()"""
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        label = QLabel("Select a routine")
        #label = QLabel(self.testingJson())
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        #morning = {"get dressed": "put on clothes to match the weather.","eat breakfast": "toast or an egg.","brush teeth": "red toothbrush and blue toothpaste."}


        self.button_action = QAction(QIcon("bug.png"), "&Routine 1", self)
        self.button_action.setStatusTip("This is your first created routine")
        self.button_action.triggered.connect(self.onMyToolBarButtonClick)
        #self.button_action.triggered.connect(self.retranslateUi)
        self.button_action.setCheckable(True)
        self.button_action.triggered.connect(self.checkDataFormat)
        toolbar.addAction(self.button_action)

        toolbar.addSeparator()

        button_action2 = QAction(QIcon("bug.png"), "Routine &2", self)
        button_action2.setStatusTip("This is your button2")
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        button_action2.setCheckable(True)
        button_action2.triggered.connect(self.testingJson)
        toolbar.addAction(button_action2)

        toolbar.addSeparator()

        button_action3 = QAction(QIcon("bug.png"), "Routine &3", self)
        button_action3.setStatusTip("This is your button3")
        #button_action3.triggered.connect(self.onMyToolBarButtonClick)
        button_action3.setCheckable(True)
        button_action3.triggered.connect(self.testingJson)
        toolbar.addAction(button_action3)

        #toolbar.addWidget(QLabel("Hello"))
        #toolbar.addWidget(QCheckBox())

        self.setStatusBar(QStatusBar(self))

        menu = self.menuBar()

        file_menu = menu.addMenu("&File")
        file_menu.addAction(self.button_action)
        file_menu.addSeparator()

        file_submenu = file_menu.addMenu("Submenu")
        file_submenu.addAction(button_action2)

        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.button_action.setText(_translate("MainWindow", "Morning"))

        

    def onMyToolBarButtonClick(self, s):
        print("click", s)
        ##app = QApplication(sys.argv)
        #y = umw()
        #y.setupUi(self)
        #y.show()
        #app.exec()
        if s == True:
            """self.addDockWidget #experiment"""
            
            y = umw()
            y.setupUi(self)
            y.show()
            """
            self.y = umw()
            self.y.setupUi(self)
            self.y.show()
            """
            #app.exec()
        else:
            c = usw()
            c.setupUi(self)#, self.u)
            c.show()
            #self = MainWindow
            """self.__init__()
            self.show()
            umw.exit()"""
            #s = QApplication.instance().quit()
            #app = QApplication(sys.argv)
            #s = QApplication.instance().quit()
            #w = MainWindow()
            #umw.backToMain(self, MainWindow)
                ##umw.backToMain(self)
                ##startUp()
            #w.show()
            #app.exec()
            #QApplication.instance().quit()

    def testingJson(self):
        #json.dumps("routines")
        x = open("routine_walkthrough/routines.json", "r")
        #y = json.loads(x)
        y = json.loads(x.read())
        print(y)
        print(y['routines'][0]['morning'][0]['get dressed']) #This is how to properly read the .json file and organize it
        print(type(y['routines'][0]['morning'][0]['get dressed']))
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
                    self.routine_testing = b
                    usw.b = b
                    for t in b:
                        print("yet another layer")
                        print(type(t))
                        print(t)
                        u = t
        self.u = u
        usw.u = self.u
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

startUp()
#app = QApplication(sys.argv)
#w = MainWindow()
#w.show()
#app.exec()


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
