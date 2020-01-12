import sys
import calcxx
from PyQt4 import QtCore, QtGui

class MyWidget(QtGui.QWidget):
    num1 = ""
    num2 = ""
    point1 = 0
    point2 = 0
    opera = 0
    opera_add = 0
    opera_minus = 0
    opera_mul = 0
    opera_div = 0

    def __init__(self):
        super(MyWidget, self).__init__()
        self.the_ui = calcxx.Ui_Form()
        self.the_ui.setupUi(self)
        self.connect(self.the_ui.btn_one, QtCore.SIGNAL('clicked()'), self.click_one)
        self.connect(self.the_ui.btn_two, QtCore.SIGNAL('clicked()'), self.click_two)
        self.connect(self.the_ui.btn_three, QtCore.SIGNAL('clicked()'), self.click_three)
        self.connect(self.the_ui.btn_four, QtCore.SIGNAL('clicked()'), self.click_four)
        self.connect(self.the_ui.btn_five, QtCore.SIGNAL('clicked()'), self.click_five)
        self.connect(self.the_ui.btn_six, QtCore.SIGNAL('clicked()'), self.click_six)
        self.connect(self.the_ui.btn_seven, QtCore.SIGNAL('clicked()'), self.click_seven)
        self.connect(self.the_ui.btn_eight, QtCore.SIGNAL('clicked()'), self.click_eight)
        self.connect(self.the_ui.btn_nine, QtCore.SIGNAL('clicked()'), self.click_nine)
        self.connect(self.the_ui.btn_zero, QtCore.SIGNAL('clicked()'), self.click_zero)
        self.connect(self.the_ui.btn_point, QtCore.SIGNAL('clicked()'), self.click_point)
        self.connect(self.the_ui.btn_add, QtCore.SIGNAL('clicked()'), self.click_add)
        self.connect(self.the_ui.btn_minus, QtCore.SIGNAL('clicked()'), self.click_minus)
        self.connect(self.the_ui.btn_multiply, QtCore.SIGNAL('clicked()'), self.click_multiply)
        self.connect(self.the_ui.btn_divide, QtCore.SIGNAL('clicked()'), self.click_divide)
        self.connect(self.the_ui.btn_equal, QtCore.SIGNAL('clicked()'),  self.click_equal)


    def click_one(self):
        if self.opera == 0:
            self.num1 += "1"
            self.the_ui.lineEdit.setText(self.num1)
        else:
            self.num2 += "1"
            self.the_ui.lineEdit.setText(self.num2)


    def click_two(self):
        if self.opera == 0:
            self.num1 += "2"
            self.the_ui.lineEdit.setText(self.num1)
        else:
            self.num2 += "2"
            self.the_ui.lineEdit.setText(self.num2)


    def click_three(self):
        if self.opera == 0:
            self.num1 += "3"
            self.the_ui.lineEdit.setText(self.num1)
        else:
            self.num2 += "3"
            self.the_ui.lineEdit.setText(self.num2)

    def click_four(self):
        if self.opera == 0:
            self.num1 += "4"
            self.the_ui.lineEdit.setText(self.num1)
        else:
            self.num2 += "4"
            self.the_ui.lineEdit.setText(self.num2)


    def click_five(self):
        if self.opera == 0:
            self.num1 += "5"
            self.the_ui.lineEdit.setText(self.num1)
        else:
            self.num2 += "5"
            self.the_ui.lineEdit.setText(self.num2)

    def click_six(self):
        if self.opera == 0:
            self.num1 += "6"
            self.the_ui.lineEdit.setText(self.num1)
        else:
            self.num2 += "6"
            self.the_ui.lineEdit.setText(self.num2)


    def click_seven(self):
        if self.opera == 0:
            self.num1 += "7"
            self.the_ui.lineEdit.setText(self.num1)
        else:
            self.num2 += "7"
            self.the_ui.lineEdit.setText(self.num2)


    def click_eight(self):
        if self.opera == 0:
            self.num1 += "8"
            self.the_ui.lineEdit.setText(self.num1)
        else:
            self.num2 += "8"
            self.the_ui.lineEdit.setText(self.num2)


    def click_nine(self):
        if self.opera == 0:
            self.num1 += "9"
            self.the_ui.lineEdit.setText(self.num1)
        else:
            self.num2 += "9"
            self.the_ui.lineEdit.setText(self.num2)


    def click_zero(self):
        if self.opera == 0:
            if len(self.num1) != 0:
                self.num1 += "0"
                self.the_ui.lineEdit.setText(self.num1)
        else:
            if len(self.num2) != 0:
                self.num2 += "0"
                self.the_ui.lineEdit.setText(self.num2)


    def click_point(self):
        if self.opera == 0:
            if len(self.num1) != 0:
                if self.point1 == 0:
                    self.num1 += "."
                    self.the_ui.lineEdit.setText(self.num1)
                    self.point1 = 1
        else:
            if len(self.num2) != 0:
                if self.point2 == 0:
                    self.num2 += "."
                    self.the_ui.lineEdit.setText(self.num2)
                    self.point2 = 1


    def click_add(self):
        self.opera = 1
        self.opera_add = 1
        self.opera_minus = 0
        self.opera_mul = 0
        self.opera_div = 0
        self.the_ui.lineEdit.setText("")


    def click_minus(self):
        self.opera = 1
        self.opera_add = 0
        self.opera_minus = 1
        self.opera_mul = 0
        self.opera_div = 0
        self.the_ui.lineEdit.setText("")


    def click_multiply(self):
        self.opera = 1
        self.opera_add = 0
        self.opera_minus = 0
        self.opera_mul = 1
        self.opera_div = 0
        self.the_ui.lineEdit.setText("")


    def click_divide(self):
        self.opera = 1
        self.opera_add = 0
        self.opera_minus = 0
        self.opera_mul = 0
        self.opera_div = 1
        self.the_ui.lineEdit.setText("")


    def click_equal(self):
        if self.opera_add == 1:
            self.the_ui.lineEdit.setText(str(float(self.num1) + float(self.num2)))
        if self.opera_minus == 1:
            self.the_ui.lineEdit.setText(str(float(self.num1) - float(self.num2)))
        if self.opera_mul == 1:
            self.the_ui.lineEdit.setText(str(float(self.num1) * float(self.num2)))
        if self.opera_div == 1:
            self.the_ui.lineEdit.setText(str(float(self.num1) / float(self.num2)))

        self.num1 = ""
        self.num2 = ""
        self.point1 = 0
        self.point2 = 0
        self.opera = 0
        self.opera_add = 0
        self.opera_minus = 0
        self.opera_mul = 0
        self.opera_div = 0


app = QtGui.QApplication(sys.argv)
wi = MyWidget()
wi.show()
app.exec_()