# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1200, 550)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 550))
        MainWindow.setMaximumSize(QtCore.QSize(1200, 550))
        MainWindow.setStyleSheet("background-color: rgb(222, 221, 218);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-3, -6, 1211, 181))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(192, 97, 203);")
        self.label.setIndent(100)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(9, 180, 381, 241))
        self.frame.setStyleSheet("background-color: rgb(246, 245, 244);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 131, 51))
        self.label_2.setStyleSheet("color: rgb(152, 106, 68);\n"
"font-size: 25px;")
        self.label_2.setObjectName("label_2")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(0, 220, 391, 20))
        self.label_7.setStyleSheet("background-color: rgb(53, 132, 228);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_infectados = QtWidgets.QLabel(self.frame)
        self.label_infectados.setGeometry(QtCore.QRect(14, 70, 361, 51))
        self.label_infectados.setStyleSheet("font-size:32px;")
        self.label_infectados.setAlignment(QtCore.Qt.AlignCenter)
        self.label_infectados.setObjectName("label_infectados")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(10, 180, 361, 20))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_data = QtWidgets.QLabel(self.frame)
        self.label_data.setGeometry(QtCore.QRect(27, 150, 341, 20))
        self.label_data.setStyleSheet("font-size:15px;")
        self.label_data.setAlignment(QtCore.Qt.AlignCenter)
        self.label_data.setObjectName("label_data")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(400, 180, 391, 241))
        self.frame_2.setStyleSheet("background-color: rgb(246, 245, 244);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 151, 41))
        self.label_3.setStyleSheet("color: rgb(152, 106, 68);\n"
"font-size: 25px;")
        self.label_3.setObjectName("label_3")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(0, 220, 391, 20))
        self.label_8.setStyleSheet("background-color: rgb(51, 209, 122);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_recuperados = QtWidgets.QLabel(self.frame_2)
        self.label_recuperados.setGeometry(QtCore.QRect(10, 70, 371, 51))
        self.label_recuperados.setStyleSheet("font-size:32px;")
        self.label_recuperados.setAlignment(QtCore.Qt.AlignCenter)
        self.label_recuperados.setObjectName("label_recuperados")
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        self.label_11.setGeometry(QtCore.QRect(10, 180, 371, 20))
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_data_2 = QtWidgets.QLabel(self.frame_2)
        self.label_data_2.setGeometry(QtCore.QRect(20, 150, 341, 20))
        self.label_data_2.setStyleSheet("font-size:15px;")
        self.label_data_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_data_2.setObjectName("label_data_2")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(800, 180, 391, 241))
        self.frame_3.setStyleSheet("background-color: rgb(246, 245, 244);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setGeometry(QtCore.QRect(20, 10, 91, 41))
        self.label_4.setStyleSheet("color: rgb(152, 106, 68);\n"
"font-size: 25px;")
        self.label_4.setObjectName("label_4")
        self.label_9 = QtWidgets.QLabel(self.frame_3)
        self.label_9.setGeometry(QtCore.QRect(0, 220, 391, 20))
        self.label_9.setStyleSheet("background-color: rgb(224, 27, 36);")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_obitos = QtWidgets.QLabel(self.frame_3)
        self.label_obitos.setGeometry(QtCore.QRect(10, 70, 371, 51))
        self.label_obitos.setStyleSheet("font-size:32px;")
        self.label_obitos.setAlignment(QtCore.Qt.AlignCenter)
        self.label_obitos.setObjectName("label_obitos")
        self.label_12 = QtWidgets.QLabel(self.frame_3)
        self.label_12.setGeometry(QtCore.QRect(10, 180, 371, 20))
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_data_3 = QtWidgets.QLabel(self.frame_3)
        self.label_data_3.setGeometry(QtCore.QRect(30, 150, 341, 20))
        self.label_data_3.setStyleSheet("font-size:15px;")
        self.label_data_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_data_3.setObjectName("label_data_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(392, 471, 151, 31))
        self.label_5.setStyleSheet("color: rgb(0, 0, 0);\n"
"font-size: 17px;")
        self.label_5.setObjectName("label_5")
        self.combo = QtWidgets.QComboBox(self.centralwidget)
        self.combo.setGeometry(QtCore.QRect(552, 471, 211, 31))
        self.combo.setObjectName("combo")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(457, -6, 731, 181))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setItalic(True)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(192, 97, 203);")
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("../a1a09896/virus.png"))
        self.label_6.setIndent(100)
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Covid-19"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#f6f5f4;\">COVID-19</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Infectados"))
        self.label_infectados.setText(_translate("MainWindow", "99 999 999 999"))
        self.label_10.setText(_translate("MainWindow", "Total confirmados"))
        self.label_data.setText(_translate("MainWindow", "data"))
        self.label_3.setText(_translate("MainWindow", "Suspeitos"))
        self.label_recuperados.setText(_translate("MainWindow", "99 999 999 999"))
        self.label_11.setText(_translate("MainWindow", "Total curados"))
        self.label_data_2.setText(_translate("MainWindow", "data"))
        self.label_4.setText(_translate("MainWindow", "Óbitos"))
        self.label_obitos.setText(_translate("MainWindow", "99 999 999 999"))
        self.label_12.setText(_translate("MainWindow", "Total óbitos"))
        self.label_data_3.setText(_translate("MainWindow", "data"))
        self.label_5.setText(_translate("MainWindow", "Selecione o Estado"))
