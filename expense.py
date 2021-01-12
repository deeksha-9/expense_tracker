# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'expense.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import os.path
from os import path
from datetime import date
import matplotlib.pyplot as plt



class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(895, 812)
        Form.setStyleSheet("QToolButton{\n"
"background-color: rgb(114, 188,255);\n"
"border-radius: 50px;\n"
"}\n"
"\n"
"QFrame{\n"
"background-color: rbga(0,181, 255, 50);\n"
"\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QLabel{\n"
"background-color:none ;\n"
"color: white;\n"
"}\n"
"\n"
"QLineEdit{\n"
"color: white;\n"
"background: transparent;\n"
"border: none;\n"
"border-bottom: 1px solid gray;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"color: white;\n"
"border-bottom: 1px solid rgb(114, 188,255);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgba(10,10,10,100);\n"
"color: white;\n"
"border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(107, 151, 232);\n"
"color: white;\n"
"}\n"
"")
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/Deeksha Priya/Desktop/Expense_tracker/Resource/unnamed.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 911, 821))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:/Users/Deeksha Priya/Desktop/Expense_tracker/Resource/bg3.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 911, 821))
        self.tabWidget.setToolTip("")
        self.tabWidget.setStyleSheet("font: 12pt \"Comic Sans MS\";\n"
"QToolButton{\n"
"background-color: rgb(114, 188,255);\n"
"border-radius: 50px;\n"
"}\n"
"\n"
"QFrame{\n"
"background-color: rbga(0,181, 255, 50);\n"
"\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QLabel{\n"
"background-color:none ;\n"
"color: white;\n"
"}\n"
"\n"
"QLineEdit{\n"
"color: white;\n"
"background: transparent;\n"
"border: none;\n"
"border-bottom: 1px solid gray;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"color: white;\n"
"border-bottom: 1px solid rgb(114, 188,255);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgba(10,10,10,100);\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(107, 151, 232);\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setStyleSheet("QPushButton{\n"
"background-color: rgba(10,10,10,100);\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(107, 151, 232);\n"
"color: white;\n"
"border-radius: 15px;\n"
"}\n"
"")
        self.tab.setObjectName("tab")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(-10, 0, 911, 811))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("C:/Users/Deeksha Priya/Desktop/Expense_tracker/Resource/bg3.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(180, 90, 161, 31))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(180, 170, 161, 31))
        self.label_7.setObjectName("label_7")
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(390, 90, 201, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
          
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(390, 170, 201, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(400, 250, 161, 31))
        self.pushButton.setObjectName("pushButton")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.tab)
        self.verticalScrollBar.setGeometry(QtCore.QRect(790, 390, 20, 251))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(70, 390, 741, 251))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(80, 330, 261, 31))
        self.label_8.setObjectName("label_8")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab)
        self.pushButton_4.setGeometry(QtCore.QRect(710, 700, 131, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab)
        self.pushButton_5.setGeometry(QtCore.QRect(180, 250, 121, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab)
        self.pushButton_3.setGeometry(QtCore.QRect(340, 650, 131, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setStyleSheet("\n"
"")
        self.tab_2.setObjectName("tab_2")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(-10, -10, 921, 791))
        self.label_3.setStyleSheet("")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("C:/Users/Deeksha Priya/Desktop/Expense_tracker/Resource/bg3.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(130, 80, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("font: 16pt \"Comic Sans MS\";")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(510, 80, 251, 41))
        self.label_10.setStyleSheet("font: 16pt \"Comic Sans MS\";\n"
"font: 75 16pt \"Comic Sans MS\";")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(100, 140, 121, 21))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setGeometry(QtCore.QRect(100, 196, 121, 20))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setGeometry(QtCore.QRect(100, 240, 131, 31))
        self.label_13.setStyleSheet("QToolButton{\n"
"background-color: rgb(114, 188,255);\n"
"border-radius: 50px;\n"
"}\n"
"\n"
"QFrame{\n"
"background-color: rbga(0,181, 255, 50);\n"
"\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QLabel{\n"
"background-color:none ;\n"
"color: white;\n"
"}\n"
"\n"
"QLineEdit{\n"
"color: white;\n"
"background: transparent;\n"
"border: none;\n"
"border-bottom: 1px solid gray;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"color: white;\n"
"border-bottom: 1px solid rgb(114, 188,255);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgba(10,10,10,100);\n"
"color: white;\n"
"border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(107, 151, 232);\n"
"color: white;\n"
"}")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.tab_2)
        self.label_14.setGeometry(QtCore.QRect(480, 140, 181, 31))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.tab_2)
        self.label_15.setGeometry(QtCore.QRect(480, 190, 161, 31))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.tab_2)
        self.label_16.setGeometry(QtCore.QRect(490, 240, 131, 31))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.tab_2)
        self.label_17.setGeometry(QtCore.QRect(100, 280, 141, 21))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.tab_2)
        self.label_18.setGeometry(QtCore.QRect(490, 280, 141, 31))
        self.label_18.setObjectName("label_18")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(260, 140, 113, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(260, 190, 111, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(670, 140, 121, 22))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_7.setGeometry(QtCore.QRect(670, 190, 121, 22))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 380, 231, 28))
        self.pushButton_2.setStyleSheet("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_6.setGeometry(QtCore.QRect(530, 380, 231, 28))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_7.setGeometry(QtCore.QRect(130, 440, 231, 28))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_8.setGeometry(QtCore.QRect(530, 440, 231, 28))
        self.pushButton_8.setObjectName("pushButton_8")
        self.lcdNumber = QtWidgets.QLCDNumber(self.tab_2)
        self.lcdNumber.setGeometry(QtCore.QRect(260, 240, 111, 23))
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.tab_2)
        self.lcdNumber_2.setGeometry(QtCore.QRect(260, 290, 111, 23))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.tab_2)
        self.lcdNumber_3.setGeometry(QtCore.QRect(670, 240, 121, 23))
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.lcdNumber_4 = QtWidgets.QLCDNumber(self.tab_2)
        self.lcdNumber_4.setGeometry(QtCore.QRect(670, 290, 121, 23))
        self.lcdNumber_4.setObjectName("lcdNumber_4")
        self.pushButton_10 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_10.setGeometry(QtCore.QRect(260, 610, 391, 28))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_11.setGeometry(QtCore.QRect(260, 670, 391, 28))
        self.pushButton_11.setObjectName("pushButton_11")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setStyleSheet("font: 75 12pt \"Comic Sans MS\";\n"
"QToolButton{\n"
"background-color: rgb(114, 188,255);\n"
"border-radius: 50px;\n"
"}\n"
"\n"
"QFrame{\n"
"background-color: rbga(0,181, 255, 50);\n"
"\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QLabel{\n"
"background-color:none ;\n"
"color: white;\n"
"}\n"
"\n"
"QLineEdit{\n"
"color: white;\n"
"background: transparent;\n"
"border: none;\n"
"border-bottom: 1px solid gray;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"color: white;\n"
"border-bottom: 1px solid rgb(114, 188,255);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgba(10,10,10,100);\n"
"color: white;\n"
"border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(107, 151, 232);\n"
"color: white;\n"
"}\n"
"")
        self.tab_3.setObjectName("tab_3")
        self.label_4 = QtWidgets.QLabel(self.tab_3)
        self.label_4.setGeometry(QtCore.QRect(-20, 0, 921, 791))
        self.label_4.setStyleSheet("font:14pt \"Comic Sans MS\";\n"
"\n"
"")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("C:/Users/Deeksha Priya/Desktop/Expense_tracker/Resource/bg3.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_19 = QtWidgets.QLabel(self.tab_3)
        self.label_19.setGeometry(QtCore.QRect(90, 190, 201, 31))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.tab_3)
        self.label_20.setGeometry(QtCore.QRect(70, 350, 301, 31))
        self.label_20.setObjectName("label_20")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_4.setGeometry(QtCore.QRect(300, 190, 191, 22))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.checkBox = QtWidgets.QCheckBox(self.tab_3)
        self.checkBox.setGeometry(QtCore.QRect(430, 360, 171, 21))
        self.checkBox.setStyleSheet("color:rgb(255, 255, 255);")
        self.checkBox.setObjectName("checkBox")
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setGeometry(QtCore.QRect(90, 110, 151, 21))
        self.label_5.setObjectName("label_5")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_2.setGeometry(QtCore.QRect(300, 110, 191, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")

        
        self.pushButton_9 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_9.setGeometry(QtCore.QRect(310, 250, 141, 28))
        self.pushButton_9.setObjectName("pushButton_9")
        self.tabWidget.addTab(self.tab_3, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton.clicked.connect(self.enter_record)
        self.pushButton_3.clicked.connect(self.view)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Expense Tracker"))
        self.label_6.setText(_translate("Form", "Select Category"))
        self.comboBox.setItemText(0, _translate("Form", "Food"))
        self.comboBox.setItemText(1, _translate("Form", "Clothing"))
        self.comboBox.setItemText(2, _translate("Form", "Footwears"))
        self.comboBox.setItemText(3, _translate("Form", "Personal"))
        self.comboBox.setItemText(4, _translate("Form", "Travel"))
        self.comboBox.setItemText(5, _translate("Form", "Stationary"))
        self.comboBox.setItemText(6, _translate("Form", "Rations"))
        self.comboBox.setItemText(7, _translate("Form", "Gifts"))
        self.comboBox.setItemText(8, _translate("Form", "Party"))
        self.comboBox.setItemText(9, _translate("Form", "EMI"))
        
        self.label_7.setText(_translate("Form", "Enter Amount"))
        self.pushButton.setText(_translate("Form", "Add Record"))
        self.label_8.setText(_translate("Form", "TextLabel"))
        self.pushButton_4.setText(_translate("Form", "Close"))
        self.pushButton_5.setText(_translate("Form", "Reset"))
        self.pushButton_3.setText(_translate("Form", "View"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Expense"))
        self.label_9.setText(_translate("Form", "Current Analysis"))
        self.label_10.setText(_translate("Form", "Comparison Analysis"))
        self.label_11.setText(_translate("Form", "Current Month"))
        self.label_12.setText(_translate("Form", "Current Year"))
        self.label_13.setText(_translate("Form", "Total Budget"))
        self.label_14.setText(_translate("Form", "Compare to Month"))
        self.label_15.setText(_translate("Form", "Compare to Year"))
        self.label_16.setText(_translate("Form", "Total Budget"))
        self.label_17.setText(_translate("Form", "Total Expense"))
        self.label_18.setText(_translate("Form", "Total Expense"))
        self.pushButton_2.setText(_translate("Form", "Summary"))
        self.pushButton_6.setText(_translate("Form", "Summary"))
        self.pushButton_7.setText(_translate("Form", "Current Analysis"))
        self.pushButton_8.setText(_translate("Form", "Comparsion"))
        self.pushButton_10.setText(_translate("Form", " Year Wise Analysis"))
        self.pushButton_11.setText(_translate("Form", "Month wise Analysis"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Analysis"))
        self.label_19.setText(_translate("Form", "Enter Budget"))
        self.label_20.setText(_translate("Form", "Wants to receive Notification?"))
        self.checkBox.setText(_translate("Form", "Notification"))
        self.label_5.setText(_translate("Form", "Enter month"))
        self.comboBox_2.setItemText(0, _translate("Form", "January"))
        self.comboBox_2.setItemText(1, _translate("Form", "Febuary"))
        self.comboBox_2.setItemText(2, _translate("Form", "March"))
        self.comboBox_2.setItemText(3, _translate("Form", "April"))
        self.comboBox_2.setItemText(4, _translate("Form", "May"))
        self.comboBox_2.setItemText(5, _translate("Form", "June"))
        self.comboBox_2.setItemText(6, _translate("Form", "July"))
        self.comboBox_2.setItemText(7, _translate("Form", "August"))
        self.comboBox_2.setItemText(8, _translate("Form", "September"))
        self.comboBox_2.setItemText(9, _translate("Form", "October"))
        self.comboBox_2.setItemText(10, _translate("Form", "November"))
        self.comboBox_2.setItemText(11, _translate("Form", "December"))
        self.pushButton_9.setText(_translate("Form", "Add budget"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "Setting"))

    def enter_record(self,Form):
        date_df = str(date.today())
        amount_df = int(self.lineEdit.text())
        category_df = self.comboBox.currentText()
        month_df = []
        year_df = []
       # print(date_df,amount_df,category_df,month_df,year_df)
       # data=[date_df,amount_df,category_df,month_df,year_df]
        data = {"Date":date_df,"Amount":amount_df,"Category":category_df,"Month" :month_df,"Category":year_df}
        df=pd.DataFrame(data)
        df['Month'] = df['Date'].dt.month
        df['Year'] = df['Date'].dt.year
        if path.exists('C:/Users/Deeksha Priya/Desktop/Expense_tracker/expense.csv'):
            df.to_csv('expense.csv',mode='a',header=False,index=False)
        else:
            df.to_csv('expense.csv',mode='a',header=['Date','Amount','Category','Month','Year'],index=False)

    def view(self,Form):
        df = pd.read_csv('expense.csv')
        self.tableWidget.setColumnCount(len(df.columns))
        self.tableWidget.setRowCount(len(df.index))
        self.tableWidget.setHorizontalHeaderItem(0,QtWidgets.QTableWidgetItem("Date"))
        self.tableWidget.setHorizontalHeaderItem(1,QtWidgets.QTableWidgetItem("Amount"))
        self.tableWidget.setHorizontalHeaderItem(2,QtWidgets.QTableWidgetItem("Category"))
        self.tableWidget.setHorizontalHeaderItem(3,QtWidgets.QTableWidgetItem("Month"))
        self.tableWidget.setHorizontalHeaderItem(4,QtWidgets.QTableWidgetItem("Year"))
        for i in range(len(df.index)):
            for j in range(len(df.columns)):
                self.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(df.iloc[i, j])))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

