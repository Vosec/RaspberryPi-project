# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'projectUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_projectWindow(object):
    def setupUi(self, projectWindow):
        projectWindow.setObjectName("projectWindow")
        projectWindow.resize(1124, 742)
        self.centralwidget = QtWidgets.QWidget(projectWindow)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 30, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tmpLabel = QtWidgets.QLabel(self.centralwidget)
        self.tmpLabel.setGeometry(QtCore.QRect(80, 30, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tmpLabel.setFont(font)
        self.tmpLabel.setObjectName("tmpLabel")
        self.measureAllBtn = QtWidgets.QPushButton(self.centralwidget)
        self.measureAllBtn.setGeometry(QtCore.QRect(910, 20, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.measureAllBtn.setFont(font)
        self.measureAllBtn.setObjectName("measureAllBtn")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 300, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.humLabel = QtWidgets.QLabel(self.centralwidget)
        self.humLabel.setGeometry(QtCore.QRect(80, 300, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.humLabel.setFont(font)
        self.humLabel.setObjectName("humLabel")
        self.cntrlWinButton = QtWidgets.QPushButton(self.centralwidget)
        self.cntrlWinButton.setGeometry(QtCore.QRect(0, 560, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cntrlWinButton.setFont(font)
        self.cntrlWinButton.setObjectName("cntrlWinButton")
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(990, 560, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.exitButton.setFont(font)
        self.exitButton.setObjectName("exitButton")
        self.tmpRadioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.tmpRadioButton.setGeometry(QtCore.QRect(600, 490, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tmpRadioButton.setFont(font)
        self.tmpRadioButton.setChecked(True)
        self.tmpRadioButton.setObjectName("tmpRadioButton")
        self.humRadioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.humRadioButton.setGeometry(QtCore.QRect(600, 520, 95, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.humRadioButton.setFont(font)
        self.humRadioButton.setObjectName("humRadioButton")
        self.datePlotButton = QtWidgets.QPushButton(self.centralwidget)
        self.datePlotButton.setGeometry(QtCore.QRect(470, 560, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.datePlotButton.setFont(font)
        self.datePlotButton.setObjectName("datePlotButton")
        self.humLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.humLabel_2.setGeometry(QtCore.QRect(330, 490, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.humLabel_2.setFont(font)
        self.humLabel_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.humLabel_2.setObjectName("humLabel_2")
        self.humLabel_3 = QtWidgets.QLabel(self.centralwidget)
        self.humLabel_3.setGeometry(QtCore.QRect(330, 520, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.humLabel_3.setFont(font)
        self.humLabel_3.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.humLabel_3.setObjectName("humLabel_3")
        self.tmpLivePlotBtn = QtWidgets.QPushButton(self.centralwidget)
        self.tmpLivePlotBtn.setGeometry(QtCore.QRect(910, 100, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tmpLivePlotBtn.setFont(font)
        self.tmpLivePlotBtn.setObjectName("tmpLivePlotBtn")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(470, 30, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(470, 300, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.prutokLabel = QtWidgets.QLabel(self.centralwidget)
        self.prutokLabel.setGeometry(QtCore.QRect(630, 30, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.prutokLabel.setFont(font)
        self.prutokLabel.setObjectName("prutokLabel")
        self.spadLabel = QtWidgets.QLabel(self.centralwidget)
        self.spadLabel.setGeometry(QtCore.QRect(580, 300, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spadLabel.setFont(font)
        self.spadLabel.setObjectName("spadLabel")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(390, 490, 194, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dateTimeEdit.setFont(font)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit_2.setGeometry(QtCore.QRect(390, 520, 194, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dateTimeEdit_2.setFont(font)
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
        self.tmpMinLbl = QtWidgets.QLabel(self.centralwidget)
        self.tmpMinLbl.setGeometry(QtCore.QRect(10, 70, 321, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tmpMinLbl.setFont(font)
        self.tmpMinLbl.setObjectName("tmpMinLbl")
        self.tmpMaxLbl = QtWidgets.QLabel(self.centralwidget)
        self.tmpMaxLbl.setGeometry(QtCore.QRect(10, 110, 331, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tmpMaxLbl.setFont(font)
        self.tmpMaxLbl.setObjectName("tmpMaxLbl")
        self.humMinLbl = QtWidgets.QLabel(self.centralwidget)
        self.humMinLbl.setGeometry(QtCore.QRect(10, 340, 331, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.humMinLbl.setFont(font)
        self.humMinLbl.setObjectName("humMinLbl")
        self.humMaxLbl = QtWidgets.QLabel(self.centralwidget)
        self.humMaxLbl.setGeometry(QtCore.QRect(10, 380, 371, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.humMaxLbl.setFont(font)
        self.humMaxLbl.setObjectName("humMaxLbl")
        self.prutokMinLabel = QtWidgets.QLabel(self.centralwidget)
        self.prutokMinLabel.setGeometry(QtCore.QRect(470, 70, 361, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.prutokMinLabel.setFont(font)
        self.prutokMinLabel.setObjectName("prutokMinLabel")
        self.prutokMaxLabel = QtWidgets.QLabel(self.centralwidget)
        self.prutokMaxLabel.setGeometry(QtCore.QRect(470, 110, 351, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.prutokMaxLabel.setFont(font)
        self.prutokMaxLabel.setObjectName("prutokMaxLabel")
        self.tlakSpadMinLabel = QtWidgets.QLabel(self.centralwidget)
        self.tlakSpadMinLabel.setGeometry(QtCore.QRect(470, 340, 381, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tlakSpadMinLabel.setFont(font)
        self.tlakSpadMinLabel.setObjectName("tlakSpadMinLabel")
        self.tlakSpadMaxLabel = QtWidgets.QLabel(self.centralwidget)
        self.tlakSpadMaxLabel.setGeometry(QtCore.QRect(470, 380, 441, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tlakSpadMaxLabel.setFont(font)
        self.tlakSpadMaxLabel.setObjectName("tlakSpadMaxLabel")
        self.prutokRadioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.prutokRadioButton.setGeometry(QtCore.QRect(700, 490, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.prutokRadioButton.setFont(font)
        self.prutokRadioButton.setObjectName("prutokRadioButton")
        self.spadRadioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.spadRadioButton.setGeometry(QtCore.QRect(700, 520, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spadRadioButton.setFont(font)
        self.spadRadioButton.setObjectName("spadRadioButton")
        projectWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(projectWindow)
        self.statusbar.setObjectName("statusbar")
        projectWindow.setStatusBar(self.statusbar)

        self.retranslateUi(projectWindow)
        self.exitButton.clicked.connect(projectWindow.close)
        QtCore.QMetaObject.connectSlotsByName(projectWindow)

    def retranslateUi(self, projectWindow):
        _translate = QtCore.QCoreApplication.translate
        projectWindow.setWindowTitle(_translate("projectWindow", "Project"))
        self.label.setText(_translate("projectWindow", "Teplota:"))
        self.tmpLabel.setText(_translate("projectWindow", "? "))
        self.measureAllBtn.setText(_translate("projectWindow", "Změřit všechny veličiny"))
        self.label_3.setText(_translate("projectWindow", "Vlhkost:"))
        self.humLabel.setText(_translate("projectWindow", "? "))
        self.cntrlWinButton.setText(_translate("projectWindow", "Oknko s kontrolními prvky"))
        self.exitButton.setText(_translate("projectWindow", "Exit"))
        self.tmpRadioButton.setText(_translate("projectWindow", "Teplota"))
        self.humRadioButton.setText(_translate("projectWindow", "Vlhkost"))
        self.datePlotButton.setText(_translate("projectWindow", "Graf"))
        self.humLabel_2.setText(_translate("projectWindow", "Od"))
        self.humLabel_3.setText(_translate("projectWindow", "Do"))
        self.tmpLivePlotBtn.setText(_translate("projectWindow", "Graf aktuálních hodnot"))
        self.label_4.setText(_translate("projectWindow", "Proteklých litrů vody:"))
        self.label_5.setText(_translate("projectWindow", "Tlakový spád:"))
        self.prutokLabel.setText(_translate("projectWindow", "? "))
        self.spadLabel.setText(_translate("projectWindow", "? "))
        self.tmpMinLbl.setText(_translate("projectWindow", "Min"))
        self.tmpMaxLbl.setText(_translate("projectWindow", "Max"))
        self.humMinLbl.setText(_translate("projectWindow", "Min"))
        self.humMaxLbl.setText(_translate("projectWindow", "Max"))
        self.prutokMinLabel.setText(_translate("projectWindow", "Min"))
        self.prutokMaxLabel.setText(_translate("projectWindow", "Max"))
        self.tlakSpadMinLabel.setText(_translate("projectWindow", "Min"))
        self.tlakSpadMaxLabel.setText(_translate("projectWindow", "Max"))
        self.prutokRadioButton.setText(_translate("projectWindow", "Průtok"))
        self.spadRadioButton.setText(_translate("projectWindow", "Tlakový spád"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    projectWindow = QtWidgets.QMainWindow()
    ui = Ui_projectWindow()
    ui.setupUi(projectWindow)
    projectWindow.show()
    sys.exit(app.exec_())
