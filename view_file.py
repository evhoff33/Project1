# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view_file.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 900)
        MainWindow.setMinimumSize(QtCore.QSize(640, 900))
        MainWindow.setMaximumSize(QtCore.QSize(640, 900))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(110, 20, 431, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet("color: rgb(170, 85, 255);")
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName("title_label")
        self.assign_header = QtWidgets.QLabel(self.centralwidget)
        self.assign_header.setGeometry(QtCore.QRect(10, 120, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.assign_header.setFont(font)
        self.assign_header.setStyleSheet("color: rgb(255, 85, 0);")
        self.assign_header.setAlignment(QtCore.Qt.AlignCenter)
        self.assign_header.setObjectName("assign_header")
        self.grade_header = QtWidgets.QLabel(self.centralwidget)
        self.grade_header.setGeometry(QtCore.QRect(280, 120, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.grade_header.setFont(font)
        self.grade_header.setStyleSheet("color: rgb(255, 85, 0);")
        self.grade_header.setAlignment(QtCore.Qt.AlignCenter)
        self.grade_header.setObjectName("grade_header")
        self.weight_header = QtWidgets.QLabel(self.centralwidget)
        self.weight_header.setGeometry(QtCore.QRect(450, 120, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.weight_header.setFont(font)
        self.weight_header.setStyleSheet("color: rgb(255, 85, 0);")
        self.weight_header.setAlignment(QtCore.Qt.AlignCenter)
        self.weight_header.setObjectName("weight_header")
        self.assign_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.assign_1.setGeometry(QtCore.QRect(10, 190, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.assign_1.setFont(font)
        self.assign_1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.assign_1.setAlignment(QtCore.Qt.AlignCenter)
        self.assign_1.setObjectName("assign_1")
        self.assign_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.assign_2.setGeometry(QtCore.QRect(10, 250, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.assign_2.setFont(font)
        self.assign_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.assign_2.setAlignment(QtCore.Qt.AlignCenter)
        self.assign_2.setObjectName("assign_2")
        self.assign_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.assign_3.setGeometry(QtCore.QRect(10, 310, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.assign_3.setFont(font)
        self.assign_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.assign_3.setAlignment(QtCore.Qt.AlignCenter)
        self.assign_3.setObjectName("assign_3")
        self.assign_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.assign_4.setGeometry(QtCore.QRect(10, 370, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.assign_4.setFont(font)
        self.assign_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.assign_4.setAlignment(QtCore.Qt.AlignCenter)
        self.assign_4.setObjectName("assign_4")
        self.assign_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.assign_5.setGeometry(QtCore.QRect(10, 430, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.assign_5.setFont(font)
        self.assign_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.assign_5.setAlignment(QtCore.Qt.AlignCenter)
        self.assign_5.setObjectName("assign_5")
        self.assign_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.assign_6.setGeometry(QtCore.QRect(10, 490, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.assign_6.setFont(font)
        self.assign_6.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.assign_6.setAlignment(QtCore.Qt.AlignCenter)
        self.assign_6.setObjectName("assign_6")
        self.grade_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.grade_1.setGeometry(QtCore.QRect(310, 190, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.grade_1.setFont(font)
        self.grade_1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.grade_1.setAlignment(QtCore.Qt.AlignCenter)
        self.grade_1.setObjectName("grade_1")
        self.grade_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.grade_2.setGeometry(QtCore.QRect(310, 250, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.grade_2.setFont(font)
        self.grade_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.grade_2.setAlignment(QtCore.Qt.AlignCenter)
        self.grade_2.setObjectName("grade_2")
        self.grade_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.grade_3.setGeometry(QtCore.QRect(310, 310, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.grade_3.setFont(font)
        self.grade_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.grade_3.setAlignment(QtCore.Qt.AlignCenter)
        self.grade_3.setPlaceholderText("")
        self.grade_3.setObjectName("grade_3")
        self.grade_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.grade_4.setGeometry(QtCore.QRect(310, 370, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.grade_4.setFont(font)
        self.grade_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.grade_4.setAlignment(QtCore.Qt.AlignCenter)
        self.grade_4.setObjectName("grade_4")
        self.grade_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.grade_5.setGeometry(QtCore.QRect(310, 430, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.grade_5.setFont(font)
        self.grade_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.grade_5.setAlignment(QtCore.Qt.AlignCenter)
        self.grade_5.setObjectName("grade_5")
        self.grade_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.grade_6.setGeometry(QtCore.QRect(310, 490, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.grade_6.setFont(font)
        self.grade_6.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.grade_6.setAlignment(QtCore.Qt.AlignCenter)
        self.grade_6.setObjectName("grade_6")
        self.weight_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.weight_1.setGeometry(QtCore.QRect(480, 190, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.weight_1.setFont(font)
        self.weight_1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.weight_1.setAlignment(QtCore.Qt.AlignCenter)
        self.weight_1.setObjectName("weight_1")
        self.weight_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.weight_2.setGeometry(QtCore.QRect(480, 250, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.weight_2.setFont(font)
        self.weight_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.weight_2.setAlignment(QtCore.Qt.AlignCenter)
        self.weight_2.setObjectName("weight_2")
        self.weight_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.weight_3.setGeometry(QtCore.QRect(480, 310, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.weight_3.setFont(font)
        self.weight_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.weight_3.setAlignment(QtCore.Qt.AlignCenter)
        self.weight_3.setObjectName("weight_3")
        self.weight_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.weight_6.setGeometry(QtCore.QRect(480, 490, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.weight_6.setFont(font)
        self.weight_6.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.weight_6.setAlignment(QtCore.Qt.AlignCenter)
        self.weight_6.setObjectName("weight_6")
        self.weight_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.weight_5.setGeometry(QtCore.QRect(480, 430, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.weight_5.setFont(font)
        self.weight_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.weight_5.setAlignment(QtCore.Qt.AlignCenter)
        self.weight_5.setObjectName("weight_5")
        self.weight_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.weight_4.setGeometry(QtCore.QRect(480, 370, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.weight_4.setFont(font)
        self.weight_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.weight_4.setAlignment(QtCore.Qt.AlignCenter)
        self.weight_4.setObjectName("weight_4")
        self.percent_button = QtWidgets.QRadioButton(self.centralwidget)
        self.percent_button.setGeometry(QtCore.QRect(280, 560, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.percent_button.setFont(font)
        self.percent_button.setStyleSheet("color: rgb(140, 0, 0);")
        self.percent_button.setChecked(True)
        self.percent_button.setObjectName("percent_button")
        self.display_label = QtWidgets.QLabel(self.centralwidget)
        self.display_label.setGeometry(QtCore.QRect(50, 540, 171, 91))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.display_label.setFont(font)
        self.display_label.setStyleSheet("color: rgb(140, 0, 0);")
        self.display_label.setObjectName("display_label")
        self.letter_button = QtWidgets.QRadioButton(self.centralwidget)
        self.letter_button.setGeometry(QtCore.QRect(470, 560, 95, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.letter_button.setFont(font)
        self.letter_button.setStyleSheet("color: rgb(140, 0, 0);")
        self.letter_button.setObjectName("letter_button")
        self.clear_button = QtWidgets.QPushButton(self.centralwidget)
        self.clear_button.setGeometry(QtCore.QRect(370, 640, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.clear_button.setFont(font)
        self.clear_button.setStyleSheet("background-color: rgb(170, 170, 127);\n"
"color: rgb(0, 0, 0);")
        self.clear_button.setObjectName("clear_button")
        self.output_box = QtWidgets.QLabel(self.centralwidget)
        self.output_box.setGeometry(QtCore.QRect(20, 720, 591, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.output_box.setFont(font)
        self.output_box.setStyleSheet("color: rgb(255, 85, 0);\n"
"background-color: rgb(0, 0, 0);")
        self.output_box.setText("")
        self.output_box.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.output_box.setObjectName("output_box")
        self.submit_button = QtWidgets.QPushButton(self.centralwidget)
        self.submit_button.setGeometry(QtCore.QRect(120, 640, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.submit_button.setFont(font)
        self.submit_button.setStyleSheet("background-color: rgb(170, 170, 127);\n"
"color: rgb(0, 0, 0);")
        self.submit_button.setObjectName("submit_button")
        self.check_1 = QtWidgets.QCheckBox(self.centralwidget)
        self.check_1.setGeometry(QtCore.QRect(600, 200, 81, 20))
        self.check_1.setObjectName("check_1")
        self.check_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.check_2.setGeometry(QtCore.QRect(600, 260, 81, 20))
        self.check_2.setObjectName("check_2")
        self.check_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.check_3.setGeometry(QtCore.QRect(600, 320, 81, 20))
        self.check_3.setObjectName("check_3")
        self.check_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.check_4.setGeometry(QtCore.QRect(600, 380, 81, 20))
        self.check_4.setObjectName("check_4")
        self.check_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.check_5.setGeometry(QtCore.QRect(600, 440, 81, 20))
        self.check_5.setObjectName("check_5")
        self.check_6 = QtWidgets.QCheckBox(self.centralwidget)
        self.check_6.setGeometry(QtCore.QRect(600, 500, 81, 20))
        self.check_6.setObjectName("check_6")
        self.check_message = QtWidgets.QLabel(self.centralwidget)
        self.check_message.setGeometry(QtCore.QRect(220, 160, 251, 20))
        self.check_message.setStyleSheet("color: rgb(255, 85, 0);")
        self.check_message.setAlignment(QtCore.Qt.AlignCenter)
        self.check_message.setObjectName("check_message")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Project 1"))
        self.title_label.setText(_translate("MainWindow", "Weighted Grade Calculator"))
        self.assign_header.setText(_translate("MainWindow", "Assignment category"))
        self.grade_header.setText(_translate("MainWindow", "Grade (%)"))
        self.weight_header.setText(_translate("MainWindow", "Weight (%)"))
        self.percent_button.setText(_translate("MainWindow", "Percentage"))
        self.display_label.setText(_translate("MainWindow", "Grade Display:"))
        self.letter_button.setText(_translate("MainWindow", "Letter"))
        self.clear_button.setText(_translate("MainWindow", "Clear Form"))
        self.submit_button.setText(_translate("MainWindow", "Submit"))
        self.check_1.setText(_translate("MainWindow", "CheckBox"))
        self.check_2.setText(_translate("MainWindow", "CheckBox"))
        self.check_3.setText(_translate("MainWindow", "CheckBox"))
        self.check_4.setText(_translate("MainWindow", "CheckBox"))
        self.check_5.setText(_translate("MainWindow", "CheckBox"))
        self.check_6.setText(_translate("MainWindow", "CheckBox"))
        self.check_message.setText(_translate("MainWindow", "(Check box if you enter data in the row.)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
