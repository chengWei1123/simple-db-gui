# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/wei/Desktop/DBMS_project/update_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 349)
        self.cancel_btn = QtWidgets.QPushButton(Dialog)
        self.cancel_btn.setGeometry(QtCore.QRect(250, 270, 101, 41))
        self.cancel_btn.setObjectName("cancel_btn")
        self.ok_btn = QtWidgets.QPushButton(Dialog)
        self.ok_btn.setGeometry(QtCore.QRect(50, 270, 101, 41))
        self.ok_btn.setObjectName("ok_btn")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 101, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 61, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 220, 81, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 190, 67, 17))
        self.label_4.setObjectName("label_4")
        self.table_edt = QtWidgets.QTextEdit(Dialog)
        self.table_edt.setGeometry(QtCore.QRect(100, 60, 271, 31))
        self.table_edt.setObjectName("table_edt")
        self.condition_edt = QtWidgets.QTextEdit(Dialog)
        self.condition_edt.setGeometry(QtCore.QRect(100, 210, 271, 31))
        self.condition_edt.setObjectName("condition_edt")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 110, 67, 17))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 150, 81, 17))
        self.label_6.setObjectName("label_6")
        self.field_edt = QtWidgets.QTextEdit(Dialog)
        self.field_edt.setGeometry(QtCore.QRect(100, 100, 271, 31))
        self.field_edt.setObjectName("field_edt")
        self.value_edt = QtWidgets.QTextEdit(Dialog)
        self.value_edt.setGeometry(QtCore.QRect(100, 140, 271, 31))
        self.value_edt.setObjectName("value_edt")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.cancel_btn.setText(_translate("Dialog", "cancel"))
        self.ok_btn.setText(_translate("Dialog", "ok"))
        self.label.setText(_translate("Dialog", "update"))
        self.label_2.setText(_translate("Dialog", "table :"))
        self.label_3.setText(_translate("Dialog", "condition : "))
        self.label_4.setText(_translate("Dialog", "where"))
        self.label_5.setText(_translate("Dialog", "field :"))
        self.label_6.setText(_translate("Dialog", "new value :"))

