# Form implementation generated from reading ui file 'c:\Users\provj709\Documents\ResearchandDevelopment\Routine-Walkthrough\routine-walkthrough\tests\screen.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.filename = QtWidgets.QLineEdit(parent=Dialog)
        self.filename.setGeometry(QtCore.QRect(20, 130, 211, 22))
        self.filename.setObjectName("filename")
        self.browse = QtWidgets.QPushButton(parent=Dialog)
        self.browse.setGeometry(QtCore.QRect(260, 130, 93, 28))
        self.browse.setObjectName("browse")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.browse.setText(_translate("Dialog", "Browse"))
