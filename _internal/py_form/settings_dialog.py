# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\budaa\Desktop\dev\printEXE\ui\settings_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(357, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(350, 400))
        Dialog.setMaximumSize(QtCore.QSize(357, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resources/img/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.lineEdit_org = QtWidgets.QLineEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_org.sizePolicy().hasHeightForWidth())
        self.lineEdit_org.setSizePolicy(sizePolicy)
        self.lineEdit_org.setMaximumSize(QtCore.QSize(200, 30))
        self.lineEdit_org.setObjectName("lineEdit_org")
        self.gridLayout.addWidget(self.lineEdit_org, 2, 2, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy)
        self.spinBox.setMinimumSize(QtCore.QSize(50, 30))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.spinBox.setFont(font)
        self.spinBox.setStyleSheet("QSpinBox::up-button   { width: 25px; height:25px; }\n"
"QSpinBox::down-button { width: 25px; height: 25px; }")
        self.spinBox.setWrapping(False)
        self.spinBox.setFrame(True)
        self.spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox.setReadOnly(False)
        self.spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.spinBox.setAccelerated(False)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(5)
        self.spinBox.setProperty("value", 3)
        self.spinBox.setDisplayIntegerBase(10)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 3, 2, 2, 1)
        self.label = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 2)
        self.check_box_exp = QtWidgets.QCheckBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_box_exp.sizePolicy().hasHeightForWidth())
        self.check_box_exp.setSizePolicy(sizePolicy)
        self.check_box_exp.setMinimumSize(QtCore.QSize(100, 20))
        self.check_box_exp.setMaximumSize(QtCore.QSize(10000000, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.check_box_exp.setFont(font)
        self.check_box_exp.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.check_box_exp.setStyleSheet("QCheckBox {\n"
"    spacing: 131px; \n"
"}")
        self.check_box_exp.setCheckable(False)
        self.check_box_exp.setChecked(False)
        self.check_box_exp.setObjectName("check_box_exp")
        self.gridLayout.addWidget(self.check_box_exp, 5, 0, 1, 3)
        self.pushButton_save = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_save.sizePolicy().hasHeightForWidth())
        self.pushButton_save.setSizePolicy(sizePolicy)
        self.pushButton_save.setMinimumSize(QtCore.QSize(165, 50))
        self.pushButton_save.setMaximumSize(QtCore.QSize(0, 0))
        self.pushButton_save.setObjectName("pushButton_save")
        self.gridLayout.addWidget(self.pushButton_save, 7, 0, 1, 1)
        self.pushButton_cancel = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_cancel.sizePolicy().hasHeightForWidth())
        self.pushButton_cancel.setSizePolicy(sizePolicy)
        self.pushButton_cancel.setMinimumSize(QtCore.QSize(140, 50))
        self.pushButton_cancel.setMaximumSize(QtCore.QSize(0, 0))
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.gridLayout.addWidget(self.pushButton_cancel, 7, 2, 1, 1)
        self.button_for_printer = QtWidgets.QPushButton(Dialog)
        self.button_for_printer.setObjectName("button_for_printer")
        self.gridLayout.addWidget(self.button_for_printer, 6, 1, 1, 2)
        self.label_printer = QtWidgets.QLabel(Dialog)
        self.label_printer.setObjectName("label_printer")
        self.gridLayout.addWidget(self.label_printer, 6, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Настройки"))
        self.label_4.setText(_translate("Dialog", "Юр.Лицо"))
        self.label.setText(_translate("Dialog", "Количество кнопок в строке:"))
        self.check_box_exp.setText(_translate("Dialog", "Отправка срока годности в бота"))
        self.pushButton_save.setText(_translate("Dialog", "Сохранить"))
        self.pushButton_cancel.setText(_translate("Dialog", "Назад"))
        self.button_for_printer.setText(_translate("Dialog", "Выбор принтера для печати"))
        self.label_printer.setText(_translate("Dialog", "TextLabel"))
from py_form import resources_rc