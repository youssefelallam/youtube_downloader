# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 251)
        MainWindow.setStyleSheet("/*\n"
"Neon Style Sheet for QT Applications (QpushButton)\n"
"Author: Jaime A. Quiroga P.\n"
"Company: GTRONICK\n"
"Last updated: 24/10/2020, 15:42.\n"
"Available at: https://github.com/GTRONICK/QSS/blob/master/NeonButtons.qss\n"
"*/\n"
"QPushButton{\n"
"    border-style: solid;\n"
"    border-color: #050a0e;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: #d3dae3;\n"
"    padding: 2px;\n"
"    background-color: #100E19;\n"
"}\n"
"QPushButton::default{\n"
"    border-style: solid;\n"
"    border-color: #050a0e;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: #FFFFFF;\n"
"    padding: 2px;\n"
"    background-color: #151a1e;\n"
"}\n"
"QPushButton:hover{\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #C0DB50, stop:0.4 #C0DB50, stop:0.5 #100E19, stop:1 #100E19);\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #100E19, stop:0.5 #100E19, stop:0.6 #C0DB50, stop:1 #C0DB50);\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #C0DB50, stop:0.3 #C0DB50, stop:0.7 #100E19, stop:1 #100E19);\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #C0DB50, stop:0.3 #C0DB50, stop:0.7 #100E19, stop:1 #100E19);\n"
"    border-width: 2px;\n"
"    border-radius: 1px;\n"
"    color: #d3dae3;\n"
"    padding: 2px;\n"
"}\n"
"QPushButton:pressed{\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #d33af1, stop:0.4 #d33af1, stop:0.5 #100E19, stop:1 #100E19);\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #100E19, stop:0.5 #100E19, stop:0.6 #d33af1, stop:1 #d33af1);\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #d33af1, stop:0.3 #d33af1, stop:0.7 #100E19, stop:1 #100E19);\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #d33af1, stop:0.3 #d33af1, stop:0.7 #100E19, stop:1 #100E19);\n"
"    border-width: 2px;\n"
"    border-radius: 1px;\n"
"    color: #d3dae3;\n"
"    padding: 2px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(330, 180, 141, 31))
        self.pushButton_3.setStyleSheet("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(130, 20, 341, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 91, 20))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 70, 261, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 180, 141, 31))
        self.pushButton_2.setStyleSheet("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 64, 17))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(400, 70, 71, 25))
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 71, 21))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(130, 120, 341, 25))
        self.comboBox.setStyleSheet("background-color: rgb(101, 101, 101);")
        self.comboBox.setObjectName("comboBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_3.setText(_translate("MainWindow", "Download"))
        self.label_2.setText(_translate("MainWindow", "Save location"))
        self.pushButton_2.setText(_translate("MainWindow", "Search"))
        self.label_3.setText(_translate("MainWindow", "Qualiti"))
        self.pushButton.setText(_translate("MainWindow", "Browse"))
        self.label.setText(_translate("MainWindow", "Video URL"))
