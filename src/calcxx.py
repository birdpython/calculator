# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calcxx.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(368, 362)
        self.btn_seven = QtGui.QPushButton(Form)
        self.btn_seven.setGeometry(QtCore.QRect(10, 90, 51, 51))
        self.btn_seven.setObjectName(_fromUtf8("btn_seven"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 351, 41))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.btn_eight = QtGui.QPushButton(Form)
        self.btn_eight.setGeometry(QtCore.QRect(110, 90, 51, 51))
        self.btn_eight.setObjectName(_fromUtf8("btn_eight"))
        self.btn_nine = QtGui.QPushButton(Form)
        self.btn_nine.setGeometry(QtCore.QRect(210, 90, 51, 51))
        self.btn_nine.setObjectName(_fromUtf8("btn_nine"))
        self.btn_multiply = QtGui.QPushButton(Form)
        self.btn_multiply.setGeometry(QtCore.QRect(310, 160, 51, 51))
        self.btn_multiply.setObjectName(_fromUtf8("btn_multiply"))
        self.btn_five = QtGui.QPushButton(Form)
        self.btn_five.setGeometry(QtCore.QRect(110, 160, 51, 51))
        self.btn_five.setObjectName(_fromUtf8("btn_five"))
        self.btn_four = QtGui.QPushButton(Form)
        self.btn_four.setGeometry(QtCore.QRect(10, 160, 51, 51))
        self.btn_four.setObjectName(_fromUtf8("btn_four"))
        self.btn_six = QtGui.QPushButton(Form)
        self.btn_six.setGeometry(QtCore.QRect(210, 160, 51, 51))
        self.btn_six.setObjectName(_fromUtf8("btn_six"))
        self.btn_three = QtGui.QPushButton(Form)
        self.btn_three.setGeometry(QtCore.QRect(210, 230, 51, 51))
        self.btn_three.setObjectName(_fromUtf8("btn_three"))
        self.btn_one = QtGui.QPushButton(Form)
        self.btn_one.setGeometry(QtCore.QRect(10, 230, 51, 51))
        self.btn_one.setObjectName(_fromUtf8("btn_one"))
        self.btn_minus = QtGui.QPushButton(Form)
        self.btn_minus.setGeometry(QtCore.QRect(310, 230, 51, 51))
        self.btn_minus.setObjectName(_fromUtf8("btn_minus"))
        self.btn_two = QtGui.QPushButton(Form)
        self.btn_two.setGeometry(QtCore.QRect(110, 230, 51, 51))
        self.btn_two.setObjectName(_fromUtf8("btn_two"))
        self.btn_point = QtGui.QPushButton(Form)
        self.btn_point.setGeometry(QtCore.QRect(110, 300, 51, 51))
        self.btn_point.setObjectName(_fromUtf8("btn_point"))
        self.btn_add = QtGui.QPushButton(Form)
        self.btn_add.setGeometry(QtCore.QRect(310, 300, 51, 51))
        self.btn_add.setObjectName(_fromUtf8("btn_add"))
        self.btn_equal = QtGui.QPushButton(Form)
        self.btn_equal.setGeometry(QtCore.QRect(210, 300, 51, 51))
        self.btn_equal.setObjectName(_fromUtf8("btn_equal"))
        self.btn_zero = QtGui.QPushButton(Form)
        self.btn_zero.setGeometry(QtCore.QRect(10, 300, 51, 51))
        self.btn_zero.setObjectName(_fromUtf8("btn_zero"))
        self.btn_divide = QtGui.QPushButton(Form)
        self.btn_divide.setGeometry(QtCore.QRect(310, 90, 51, 51))
        self.btn_divide.setObjectName(_fromUtf8("btn_divide"))
        self.btn_seven.raise_()
        self.lineEdit.raise_()
        self.btn_eight.raise_()
        self.btn_nine.raise_()
        self.btn_divide.raise_()
        self.btn_multiply.raise_()
        self.btn_five.raise_()
        self.btn_four.raise_()
        self.btn_six.raise_()
        self.btn_three.raise_()
        self.btn_one.raise_()
        self.btn_minus.raise_()
        self.btn_two.raise_()
        self.btn_point.raise_()
        self.btn_add.raise_()
        self.btn_equal.raise_()
        self.btn_zero.raise_()

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.btn_one, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.click_one)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "计算器", None))
        self.btn_seven.setText(_translate("Form", "7", None))
        self.btn_eight.setText(_translate("Form", "8", None))
        self.btn_nine.setText(_translate("Form", "9", None))
        self.btn_multiply.setText(_translate("Form", "*", None))
        self.btn_five.setText(_translate("Form", "5", None))
        self.btn_four.setText(_translate("Form", "4", None))
        self.btn_six.setText(_translate("Form", "6", None))
        self.btn_three.setText(_translate("Form", "3", None))
        self.btn_one.setText(_translate("Form", "1", None))
        self.btn_minus.setText(_translate("Form", "-", None))
        self.btn_two.setText(_translate("Form", "2", None))
        self.btn_point.setText(_translate("Form", ".", None))
        self.btn_add.setText(_translate("Form", "+", None))
        self.btn_equal.setText(_translate("Form", "=", None))
        self.btn_zero.setText(_translate("Form", "0", None))
        self.btn_divide.setText(_translate("Form", "/", None))

