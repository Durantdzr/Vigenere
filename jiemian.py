# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jiemian.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Vigenere(object):
    def setupUi(self, Vigenere):
        Vigenere.setObjectName("Vigenere")
        Vigenere.resize(531, 402)
        self.Record = QtWidgets.QTextBrowser(Vigenere)
        self.Record.setGeometry(QtCore.QRect(110, 200, 361, 192))
        self.Record.setObjectName("Record")
        self.label_4 = QtWidgets.QLabel(Vigenere)
        self.label_4.setGeometry(QtCore.QRect(60, 200, 72, 15))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Vigenere)
        self.label_5.setGeometry(QtCore.QRect(150, 10, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.splitter_3 = QtWidgets.QSplitter(Vigenere)
        self.splitter_3.setGeometry(QtCore.QRect(60, 70, 71, 81))
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.label = QtWidgets.QLabel(self.splitter_3)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.splitter_3)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.splitter_3)
        self.label_3.setObjectName("label_3")
        self.splitter_2 = QtWidgets.QSplitter(Vigenere)
        self.splitter_2.setGeometry(QtCore.QRect(110, 60, 211, 101))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.MingWord = QtWidgets.QLineEdit(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.MingWord.setFont(font)
        self.MingWord.setObjectName("MingWord")
        self.Key = QtWidgets.QLineEdit(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Key.setFont(font)
        self.Key.setObjectName("Key")
        self.SecretWord = QtWidgets.QLineEdit(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.SecretWord.setFont(font)
        self.SecretWord.setObjectName("SecretWord")
        self.splitter = QtWidgets.QSplitter(Vigenere)
        self.splitter.setGeometry(QtCore.QRect(360, 60, 121, 71))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.JieMi = QtWidgets.QPushButton(self.splitter)
        self.JieMi.setObjectName("JieMi")
        self.JiaMi = QtWidgets.QPushButton(self.splitter)
        self.JiaMi.setObjectName("JiaMi")

        self.retranslateUi(Vigenere)
        self.JiaMi.clicked.connect(Vigenere.jiami)
        self.JieMi.clicked.connect(Vigenere.jiemi)
        QtCore.QMetaObject.connectSlotsByName(Vigenere)

    def retranslateUi(self, Vigenere):
        _translate = QtCore.QCoreApplication.translate
        Vigenere.setWindowTitle(_translate("Vigenere", "Dialog"))
        self.label_4.setText(_translate("Vigenere", "记录"))
        self.label_5.setText(_translate("Vigenere", "维吉尼亚密码"))
        self.label.setText(_translate("Vigenere", "明文"))
        self.label_2.setText(_translate("Vigenere", "Key"))
        self.label_3.setText(_translate("Vigenere", "密文"))
        self.JieMi.setText(_translate("Vigenere", "解密"))
        self.JiaMi.setText(_translate("Vigenere", "加密"))

