# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'advCalc.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(QtWidgets.QMainWindow):
    expression = ""
    isopr = False
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(668, 588)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(280, 130, 101, 81))
        self.pushButton_9.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color:white;\n"
"color:black;\n"
"font:bold;\n"
"border-width:3px;\n"
"border-color:silver;\n"
"border-style:outset;")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_20 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_20.setGeometry(QtCore.QRect(550, 130, 101, 81))
        self.pushButton_20.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(222, 222, 222);\n"
"color:black;\n"
"border-width:3px;\n"
"border-color: rgb(115, 115, 115);\n"
"border-style:outset;")
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(410, 240, 101, 81))
        self.pushButton_13.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(222, 222, 222);\n"
"color:black;\n"
"\n"
"border-width:3px;\n"
"border-color: rgb(115, 115, 115);\n"
"border-style:outset;")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_24 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_24.setGeometry(QtCore.QRect(280, 350, 101, 81))
        self.pushButton_24.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color:white;\n"
"color:black;\n"
"font:bold;\n"
"border-width:3px;\n"
"border-color:silver;\n"
"border-style:outset;")
        self.pushButton_24.setObjectName("pushButton_24")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(410, 460, 101, 81))
        self.pushButton_12.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(222, 222, 222);\n"
"color:black;\n"
"border-width:3px;\n"
"border-color: rgb(115, 115, 115);\n"
"border-style:outset;")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 460, 101, 81))
        self.pushButton_3.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color:white;\n"
"color:black;\n"
"font:bold;\n"
"border-width:3px;\n"
"border-color:silver;\n"
"border-style:outset;\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(280, 240, 101, 81))
        self.pushButton_6.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color:white;\n"
"color:black;\n"
"font:bold;\n"
"border-width:3px;\n"
"border-color:silver;\n"
"border-style:outset;")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_23 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_23.setGeometry(QtCore.QRect(150, 350, 101, 81))
        self.pushButton_23.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color:white;\n"
"color:black;\n"
"font:bold;\n"
"border-width:3px;\n"
"border-color:silver;\n"
"border-style:outset;")
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(410, 130, 101, 81))
        self.pushButton_10.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(222, 222, 222);\n"
"color:black;\n"
"\n"
"border-width:3px;\n"
"border-color: rgb(115, 115, 115);\n"
"border-style:outset;")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(150, 240, 101, 81))
        self.pushButton_5.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color:white;\n"
"color:black;\n"
"font:bold;\n"
"border-width:3px;\n"
"border-color:silver;\n"
"border-style:outset;")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(20, 130, 101, 81))
        self.pushButton_7.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color:white;\n"
"color:black;\n"
"font:bold;\n"
"border-width:3px;\n"
"border-color:silver;\n"
"border-style:outset;")

        self.pushButton_7.setObjectName("pushButton_7")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 30, 631, 81))
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight)
        self.lineEdit.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";text align:right;")



        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 460, 101, 81))
        self.pushButton_2.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color:white;\n"
"color:black;\n"
"font:bold;\n"
"border-width:3px;\n"
"border-color:silver;\n"
"border-style:outset;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(150, 130, 101, 81))
        self.pushButton_8.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color:white;\n"
"color:black;\n"
"font:bold;\n"
"border-width:3px;\n"
"border-color:silver;\n"
"border-style:outset;")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(280, 460, 101, 81))
        self.pushButton_15.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(222, 222, 222);\n"
"color:black;\n"
"\n"
"border-width:3px;\n"
"border-color: rgb(115, 115, 115);\n"
"border-style:outset;")
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 240, 101, 81))
        self.pushButton_4.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color:white;\n"
"color:black;\n"
"font:bold;\n"
"border-width:3px;\n"
"border-color:silver;\n"
"border-style:outset;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_22 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_22.setGeometry(QtCore.QRect(20, 350, 101, 81))
        self.pushButton_22.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color:white;\n"
"color:black;\n"
"font:bold;\n"
"border-width:3px;\n"
"border-color:silver;\n"
"border-style:outset;")
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_19 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_19.setGeometry(QtCore.QRect(550, 350, 101, 81))
        self.pushButton_19.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(222, 222, 222);\n"
"color:black;\n"
"\n"
"border-width:3px;\n"
"border-color: rgb(115, 115, 115);\n"
"border-style:outset;")
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_17 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_17.setGeometry(QtCore.QRect(410, 350, 101, 81))
        self.pushButton_17.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(222, 222, 222);\n"
"color:black;\n"
"border-width:3px;\n"
"border-color: rgb(115, 115, 115);\n"
"border-style:outset;")
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(550, 460, 101, 81))
        self.pushButton_11.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(222, 222, 222);\n"
"color:black;\n"
"border-width:3px;\n"
"border-color: rgb(115, 115, 115);\n"
"border-style:outset;")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(550, 240, 101, 81))
        self.pushButton_16.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(222, 222, 222);\n"
"color:black;\n"
"border-width:3px;\n"
"border-color: rgb(115, 115, 115);\n"
"border-style:outset;")
        self.pushButton_16.setObjectName("pushButton_16")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 668, 21))
        self.menubar.setObjectName("menubar")
        self.menuOption = QtWidgets.QMenu(self.menubar)
        self.menuOption.setObjectName("menuOption")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionStandard_Calculator = QtWidgets.QAction(MainWindow)
        self.actionStandard_Calculator.setObjectName("actionStandard_Calculator")
        self.actionScientific_Calculator = QtWidgets.QAction(MainWindow)
        self.actionScientific_Calculator.setObjectName("actionScientific_Calculator")
        self.menuOption.addAction(self.actionStandard_Calculator)
        self.menuOption.addAction(self.actionScientific_Calculator)
        self.menubar.addAction(self.menuOption.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_9.setText(_translate("MainWindow", "9"))
        self.pushButton_20.setText(_translate("MainWindow", "C"))
        self.pushButton_13.setText(_translate("MainWindow", "-"))
        self.pushButton_24.setText(_translate("MainWindow", "3"))
        self.pushButton_12.setText(_translate("MainWindow", "*"))
        self.pushButton_3.setText(_translate("MainWindow", "."))
        self.pushButton_6.setText(_translate("MainWindow", "6"))
        self.pushButton_23.setText(_translate("MainWindow", "2"))
        self.pushButton_10.setText(_translate("MainWindow", "+"))
        self.pushButton_5.setText(_translate("MainWindow", "5"))
        self.pushButton_7.setText(_translate("MainWindow", "7"))
        self.pushButton_2.setText(_translate("MainWindow", "0"))
        self.pushButton_8.setText(_translate("MainWindow", "8"))
        self.pushButton_15.setText(_translate("MainWindow", "%"))
        self.pushButton_4.setText(_translate("MainWindow", "4"))
        self.pushButton_22.setText(_translate("MainWindow", "1"))
        self.pushButton_19.setText(_translate("MainWindow", "1/X"))
        self.pushButton_17.setText(_translate("MainWindow", "÷"))
        self.pushButton_11.setText(_translate("MainWindow", "="))
        self.pushButton_16.setText(_translate("MainWindow", "√X"))
        self.menuOption.setTitle(_translate("MainWindow", "Option"))
        self.actionStandard_Calculator.setText(_translate("MainWindow", "Standard Calculator"))
        self.actionScientific_Calculator.setText(_translate("MainWindow", "Scientific Calculator"))
        self.initEvents()

    def initEvents(self):
         buttons = [self.pushButton_2,self.pushButton_22,self.pushButton_23,
         self.pushButton_24,self.pushButton_4,self.pushButton_5,
         self.pushButton_6,self.pushButton_7,self.pushButton_8,self.pushButton_9,self.pushButton_3]

         operator = [self.pushButton_10,self.pushButton_13,self.pushButton_17,
        self.pushButton_12,self.pushButton_15,self.pushButton_16,self.pushButton_19]

         for btn in buttons:
                 btn.clicked.connect(self.appendNum)

         for op_btn in operator:
                 op_btn.clicked.connect(self.appendOpr)
         self.pushButton_11.clicked.connect(self.evaluate)
         self.pushButton_20.clicked.connect(self.clear)
        
         

    def appendNum(self):
            btn = self.sender()

            num = btn.text()
            self.expression +=num
            self.lineEdit.setText(self.expression)
            self.isopr = False
            
    def evaluate(self):
        try:
            result = eval(self.expression)
            self.expression = str(result)
            self.lineEdit.setText(self.expression)
        except BaseException as ex:
                print(ex)
    

    def clear(self):
            self.expression =""
            self.lineEdit.setText(self.expression)


    def appendOpr(self):

            btn = self.sender()
            btn.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 0, 0);\n"
"color:black;\n"
"\n"
"border-width:3px;\n"
"border-color: rgb(255, 255, 255);\n"
"border-style:outset;")
            oper = [self.pushButton_10,self.pushButton_13,self.pushButton_17,
        self.pushButton_12,self.pushButton_15,self.pushButton_16,self.pushButton_19]
            for i in oper:
                if i != btn:
                    i.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(222, 222, 222);\n"
"color:black;\n"
"\n"
"border-width:3px;\n"
"border-color: rgb(115, 115, 115);\n"
"border-style:outset;")
            opr = btn.text()
            if self.isopr == False:
                self.expression = self.expression + opr
                self.lineEdit.setText(self.expression)
            else:
                self.expression = self.expression[0:len(self.expression)-1]+opr
                self.lineEdit.setText(self.expression)

            self.isopr = True
            

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
