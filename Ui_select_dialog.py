# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/wei/Desktop/DBMS_project/select_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.field_edt = QtWidgets.QPlainTextEdit(Dialog)
        self.field_edt.setGeometry(QtCore.QRect(80, 60, 271, 31))
        self.field_edt.setObjectName("field_edt")
        self.ok_btn = QtWidgets.QPushButton(Dialog)
        self.ok_btn.setGeometry(QtCore.QRect(80, 220, 111, 41))
        self.ok_btn.setObjectName("ok_btn")
        self.cancel_btn = QtWidgets.QPushButton(Dialog)
        self.cancel_btn.setGeometry(QtCore.QRect(240, 220, 111, 41))
        self.cancel_btn.setObjectName("cancel_btn")
        self.table_edt = QtWidgets.QPlainTextEdit(Dialog)
        self.table_edt.setGeometry(QtCore.QRect(80, 140, 271, 31))
        self.table_edt.setObjectName("table_edt")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 30, 67, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 41, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 110, 71, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 150, 51, 17))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.ok_btn.setText(_translate("Dialog", "ok"))
        self.cancel_btn.setText(_translate("Dialog", "cancel"))
        self.label.setText(_translate("Dialog", "Select "))
        self.label_2.setText(_translate("Dialog", "field :"))
        self.label_3.setText(_translate("Dialog", "from "))
        self.label_4.setText(_translate("Dialog", "table :"))

