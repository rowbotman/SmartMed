# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NormalityWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class NormalityWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(480, 400, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 400, 113, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 80, 351, 51))
        self.label.setObjectName("label")
        self.radioButtonColm = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonColm.setGeometry(QtCore.QRect(110, 160, 241, 20))
        self.radioButtonColm.setObjectName("radioButtonColm")
        self.radioButtonShap = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonShap.setGeometry(QtCore.QRect(110, 210, 191, 20))
        self.radioButtonShap.setObjectName("radioButtonShap")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "вперед"))
        self.pushButton_2.setText(_translate("MainWindow", "назад"))
        self.label.setText(_translate("MainWindow", " Выберите, каким способом выполнется \n"
" проверка данных на нормальность:"))
        self.radioButtonColm.setText(_translate("MainWindow", "Критерий Колмогорова-Смирнова"))
        self.radioButtonShap.setText(_translate("MainWindow", "Критерий Шапиро-Уилка"))
