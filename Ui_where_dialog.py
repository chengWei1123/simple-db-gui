# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/wei/Desktop/DBMS_project/where_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(405, 192)
        self.ok_btn = QtWidgets.QPushButton(Dialog)
        self.ok_btn.setGeometry(QtCore.QRect(110, 120, 101, 41))
        self.ok_btn.setObjectName("ok_btn")
        self.cancel_btn = QtWidgets.QPushButton(Dialog)
        self.cancel_btn.setGeometry(QtCore.QRect(270, 120, 101, 41))
        self.cancel_btn.setObjectName("cancel_btn")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 20, 67, 17))
        self.label.setObjectName("label")
        self.condition_edt = QtWidgets.QTextEdit(Dialog)
        self.condition_edt.setGeometry(QtCore.QRect(110, 50, 261, 31))
        self.condition_edt.setObjectName("condition_edt")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 81, 17))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.ok_btn.setText(_translate("Dialog", "ok"))
        self.cancel_btn.setText(_translate("Dialog", "cancel"))
        self.label.setText(_translate("Dialog", "where"))
        self.label_2.setText(_translate("Dialog", "condition :"))

