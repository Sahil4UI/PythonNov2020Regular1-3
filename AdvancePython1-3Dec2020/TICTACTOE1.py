# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TICTACTOE.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(591, 484)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 0, 201, 61))
        self.label.setStyleSheet("font: 75 26pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 100, 361, 31))
        self.label_2.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(240, 140, 82, 31))
        self.radioButton.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(330, 140, 82, 31))
        self.radioButton_2.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.radioButton_2.setObjectName("radioButton_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 210, 211, 23))
        self.pushButton.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 0);")
        self.pushButton.setObjectName("pushButton")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 70, 581, 391))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 441, 371))
        self.label_3.setStyleSheet("font: 75 26pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../../Downloads/tictactoe.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 30, 111, 86))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"font: 20pt \"MS Shell Dlg 2\";")
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setDefault(False)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 140, 111, 86))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"font: 20pt \"MS Shell Dlg 2\";")
        self.pushButton_3.setAutoDefault(False)
        self.pushButton_3.setDefault(False)
        self.pushButton_3.setFlat(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setEnabled(True)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 260, 111, 86))
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"font: 20pt \"MS Shell Dlg 2\";")
        self.pushButton_4.setAutoDefault(False)
        self.pushButton_4.setDefault(False)
        self.pushButton_4.setFlat(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setEnabled(True)
        self.pushButton_5.setGeometry(QtCore.QRect(166, 260, 111, 86))
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"font: 20pt \"MS Shell Dlg 2\";")
        self.pushButton_5.setAutoDefault(False)
        self.pushButton_5.setDefault(False)
        self.pushButton_5.setFlat(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setEnabled(True)
        self.pushButton_6.setGeometry(QtCore.QRect(166, 140, 111, 86))
        self.pushButton_6.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"font: 20pt \"MS Shell Dlg 2\";")
        self.pushButton_6.setAutoDefault(False)
        self.pushButton_6.setDefault(False)
        self.pushButton_6.setFlat(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setEnabled(True)
        self.pushButton_7.setGeometry(QtCore.QRect(166, 30, 111, 86))
        self.pushButton_7.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"font: 20pt \"MS Shell Dlg 2\";")
        self.pushButton_7.setAutoDefault(False)
        self.pushButton_7.setDefault(False)
        self.pushButton_7.setFlat(False)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setEnabled(True)
        self.pushButton_8.setGeometry(QtCore.QRect(301, 260, 111, 86))
        self.pushButton_8.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"font: 20pt \"MS Shell Dlg 2\";")
        self.pushButton_8.setAutoDefault(False)
        self.pushButton_8.setDefault(False)
        self.pushButton_8.setFlat(False)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setEnabled(True)
        self.pushButton_9.setGeometry(QtCore.QRect(301, 30, 111, 86))
        self.pushButton_9.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"font: 20pt \"MS Shell Dlg 2\";")
        self.pushButton_9.setAutoDefault(False)
        self.pushButton_9.setDefault(False)
        self.pushButton_9.setFlat(False)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame)
        self.pushButton_10.setEnabled(True)
        self.pushButton_10.setGeometry(QtCore.QRect(301, 140, 111, 86))
        self.pushButton_10.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"font: 20pt \"MS Shell Dlg 2\";")
        self.pushButton_10.setAutoDefault(False)
        self.pushButton_10.setDefault(False)
        self.pushButton_10.setFlat(False)
        self.pushButton_10.setObjectName("pushButton_10")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(450, 140, 121, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(450, 110, 121, 21))
        self.label_4.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"font: 75 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 591, 21))
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
        self.label.setText(_translate("MainWindow", "TIC TAC TOE"))
        self.label_2.setText(_translate("MainWindow", "CHOOSE YOUR CHARACTER  (X OR 0)"))
        self.radioButton.setText(_translate("MainWindow", "0"))
        self.radioButton_2.setText(_translate("MainWindow", "X"))
        self.pushButton.setText(_translate("MainWindow", "Start Game"))
        self.pushButton_2.setText(_translate("MainWindow", "1"))
        self.pushButton_3.setText(_translate("MainWindow", "4"))
        self.pushButton_4.setText(_translate("MainWindow", "7"))
        self.pushButton_5.setText(_translate("MainWindow", "8"))
        self.pushButton_6.setText(_translate("MainWindow", "5"))
        self.pushButton_7.setText(_translate("MainWindow", "2"))
        self.pushButton_8.setText(_translate("MainWindow", "9"))
        self.pushButton_9.setText(_translate("MainWindow", "3"))
        self.pushButton_10.setText(_translate("MainWindow", "6"))
        self.label_4.setText(_translate("MainWindow", "WINNER"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
