# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\budaa\Desktop\dev\printEXE\ui\mark_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(355, 188)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(355, 188))
        Dialog.setMaximumSize(QtCore.QSize(355, 188))
        self.label_form = QtWidgets.QLabel(Dialog)
        self.label_form.setGeometry(QtCore.QRect(0, 0, 371, 201))
        self.label_form.setText("")
        self.label_form.setPixmap(QtGui.QPixmap(":/resources/img/make_opened_form.png"))
        self.label_form.setObjectName("label_form")
        self.label_name = QtWidgets.QLabel(Dialog)
        self.label_name.setGeometry(QtCore.QRect(100, 40, 221, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_name.sizePolicy().hasHeightForWidth())
        self.label_name.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_name.setFont(font)
        self.label_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_name.setWordWrap(True)
        self.label_name.setObjectName("label_name")
        self.label_temp = QtWidgets.QLabel(Dialog)
        self.label_temp.setGeometry(QtCore.QRect(160, 80, 161, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_temp.sizePolicy().hasHeightForWidth())
        self.label_temp.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_temp.setFont(font)
        self.label_temp.setAlignment(QtCore.Qt.AlignCenter)
        self.label_temp.setObjectName("label_temp")
        self.label_current = QtWidgets.QLabel(Dialog)
        self.label_current.setGeometry(QtCore.QRect(160, 120, 161, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_current.sizePolicy().hasHeightForWidth())
        self.label_current.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_current.setFont(font)
        self.label_current.setAlignment(QtCore.Qt.AlignCenter)
        self.label_current.setObjectName("label_current")
        self.label_exp = QtWidgets.QLabel(Dialog)
        self.label_exp.setGeometry(QtCore.QRect(160, 150, 161, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_exp.sizePolicy().hasHeightForWidth())
        self.label_exp.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_exp.setFont(font)
        self.label_exp.setAlignment(QtCore.Qt.AlignCenter)
        self.label_exp.setObjectName("label_exp")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_name.setText(_translate("Dialog", "TextLabel"))
        self.label_temp.setText(_translate("Dialog", "TextLabel"))
        self.label_current.setText(_translate("Dialog", "TextLabel"))
        self.label_exp.setText(_translate("Dialog", "TextLabel"))
from py_form import resources_rc
