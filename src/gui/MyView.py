# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MyView.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.amountLabel = QtWidgets.QLabel(self.centralwidget)
        self.amountLabel.setObjectName("amountLabel")
        self.horizontalLayout_3.addWidget(self.amountLabel)
        self.amount = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.amount.setSingleStep(0.1)
        self.amount.setObjectName("amount")
        self.horizontalLayout_3.addWidget(self.amount)
        self.currencyLabel = QtWidgets.QLabel(self.centralwidget)
        self.currencyLabel.setObjectName("currencyLabel")
        self.horizontalLayout_3.addWidget(self.currencyLabel)
        self.currency = QtWidgets.QLineEdit(self.centralwidget)
        self.currency.setObjectName("currency")
        self.horizontalLayout_3.addWidget(self.currency)
        self.targetCurrencyLabel = QtWidgets.QLabel(self.centralwidget)
        self.targetCurrencyLabel.setObjectName("targetCurrencyLabel")
        self.horizontalLayout_3.addWidget(self.targetCurrencyLabel)
        self.targetCurrency = QtWidgets.QLineEdit(self.centralwidget)
        self.targetCurrency.setObjectName("targetCurrency")
        self.horizontalLayout_3.addWidget(self.targetCurrency)
        self.calculate = QtWidgets.QPushButton(self.centralwidget)
        self.calculate.setObjectName("calculate")
        self.horizontalLayout_3.addWidget(self.calculate)
        self.liveData = QtWidgets.QCheckBox(self.centralwidget)
        self.liveData.setChecked(True)
        self.liveData.setObjectName("liveData")
        self.horizontalLayout_3.addWidget(self.liveData)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.output = QtWidgets.QTextBrowser(self.centralwidget)
        self.output.setObjectName("output")
        self.verticalLayout.addWidget(self.output)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setObjectName("exitButton")
        self.horizontalLayout.addWidget(self.exitButton)
        self.resetButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetButton.setObjectName("resetButton")
        self.horizontalLayout.addWidget(self.resetButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.resetButton.clicked.connect(self.currency.clear)
        self.resetButton.clicked.connect(self.targetCurrency.clear)
        self.exitButton.clicked.connect(MainWindow.close)
        self.resetButton.clicked.connect(self.amount.clear)
        self.resetButton.clicked.connect(self.output.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.amountLabel.setText(_translate("MainWindow", "Betrag:"))
        self.currencyLabel.setText(_translate("MainWindow", "Währung:"))
        self.targetCurrencyLabel.setText(_translate("MainWindow", "Zielwährung:"))
        self.calculate.setText(_translate("MainWindow", "Umrechnen"))
        self.liveData.setText(_translate("MainWindow", "Live-Daten"))
        self.exitButton.setText(_translate("MainWindow", "Exit"))
        self.resetButton.setText(_translate("MainWindow", "Zurücksetzen"))
