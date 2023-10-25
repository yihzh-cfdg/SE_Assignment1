import math
import random
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QPushButton
from ui_cal import Ui_Calculator

sym_name = ['+', '-', '*', '/', 'x^y', 'mod']


class Calculator(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.old_exp = ""
        self.new_exp = ""
        self.currentVal = 0  # Currently displayed number
        self.lastVal = 0  # Number before operation
        self.bChangeop = False  # Flag for changing operation
        self.bInv = False  # Inverse on/off flag
        self.bNoprev = True  # Flag for previous equals
        self.bDot = False  # Flag for has a dot
        self.holdVal = ''  # holding the second operand in repetitive calculations
        self.shift_change = False
        self.bError = False
        self.ui = Ui_Calculator()
        self.ui.setupUi(self)
        self.ui.btn_shift.clicked.connect(self.on_shift_clicked)

    def on_button_clicked(self):
        clicked_button = self.sender()
        button_text = clicked_button.text()
        # change new_exp
        if str.isdigit(button_text):
            if self.bNoprev == False:
                self.remake()
            if button_text == '0' and self.isEmpty():
                return
            else:
                self.new_exp += button_text
                try:
                    self.currentVal = eval(self.new_exp)
                except Exception as e:
                    self.ErrorHandler(e)
                    return
                if self.bChangeop:
                    self.bChangeop = False
            self.disp(0, None, 1, self.new_exp)
        elif button_text in sym_name:
            # change old_exp += new_exp
            if button_text == 'x^y':
                button_text = '**'
            if button_text == 'mod':
                button_text = '%'
            if self.bDot and len(self.new_exp) > 0 and self.new_exp[-1] == '.':
                self.new_exp = '0'
            if self.bChangeop:
                self.old_exp = self.old_exp[:-1]
                self.old_exp += button_text
            elif not self.bNoprev:
                # after "=" , use currentVal as old_exp
                self.bNoprev = True
                self.new_exp = ''
                self.old_exp = str(self.currentVal) + button_text
                self.bChangeop = True
            else:
                if self.isEmpty():
                    self.old_exp = '0'
                else:
                    self.old_exp += self.new_exp
                self.new_exp = ''
                try:
                    self.lastVal = self.currentVal
                    self.currentVal = eval(self.old_exp)
                except Exception as e:
                    self.ErrorHandler(e)
                    return
                self.old_exp += button_text
                self.bChangeop = True
            self.disp(1, self.old_exp, 1, str(self.currentVal))
        elif button_text == '=':
            # 输入等号
            if not self.bNoprev:
                self.old_exp = str(self.currentVal)
                self.old_exp += self.holdVal
                try:
                    self.currentVal = eval(self.old_exp)
                except Exception as e:
                    self.ErrorHandler(e)
                    return
                self.old_exp += '='
            elif self.bChangeop:
                self.bChangeop = False
                self.bNoprev = False
                self.holdVal += self.old_exp[-1]
                self.old_exp += str(self.currentVal)
                try:
                    self.currentVal = eval(self.old_exp)
                except Exception as e:
                    self.ErrorHandler(e)
                    return
                self.holdVal += str(self.currentVal)
                self.old_exp += '='
            else:
                self.bNoprev = False
                if self.old_exp != '':
                    self.holdVal = self.old_exp[-1] + self.new_exp
                    self.old_exp += self.new_exp
                else:
                    self.holdVal = ''
                    self.old_exp = self.new_exp
                    if self.isEmpty():
                        self.old_exp = '0'
                try:
                    self.currentVal = eval(self.old_exp)
                except Exception as e:
                    self.ErrorHandler(e)
                    return
                self.old_exp += '='
            self.disp(1, self.old_exp, 1, str(self.currentVal))
        elif button_text == "DEL":
            if not self.bNoprev:
                return
            if not self.isEmpty():
                if self.new_exp[-1] == '.':
                    self.bDot = False
                self.new_exp = self.new_exp[:-1]
            if self.new_exp == '':
                self.currentVal = 0
            else:
                try:
                    self.currentVal = eval(self.new_exp)
                except Exception as e:
                    self.ErrorHandler(e)
                    return
            self.disp(0, None, 1, self.new_exp)
        elif button_text == '+/-':
            if self.currentVal != 0:
                self.currentVal = -self.currentVal
                if self.bInv == False:
                    self.new_exp = '-' + self.new_exp
                    self.bInv = True
                else:
                    self.new_exp = self.new_exp[1:]
                    self.bInv = False
            self.disp(0, None, 1, str(self.currentVal))
        elif button_text == '.':
            if not self.bDot:
                self.bDot = True
                self.new_exp += '.'
            self.disp(0, None, 1, self.new_exp)
        elif button_text == 'x^2':
            self.currentVal = self.currentVal * self.currentVal
            self.new_exp = str(self.currentVal)
            self.bInv = False
            self.disp(0, None, 1, self.new_exp)
        elif button_text == 'x^3':
            self.currentVal = self.currentVal * self.currentVal * self.currentVal
            self.new_exp = str(self.currentVal)
            self.disp(0, None, 1, self.new_exp)
        elif button_text == '10^x':
            self.currentVal = 10 ** self.currentVal
            self.new_exp = str(self.currentVal)
            self.disp(0, None, 1, self.new_exp)
        elif button_text == 'log':
            try:
                self.currentVal = math.log10(self.currentVal)
            except Exception as e:
                self.ErrorHandler(e)
                return
            self.new_exp = str(self.currentVal)
            self.disp(0, None, 1, self.new_exp)
        elif button_text == 'ln':
            try:
                self.currentVal = math.log(self.currentVal)
            except Exception as e:
                self.ErrorHandler(e)
                return
            self.new_exp = str(self.currentVal)
            self.disp(0, None, 1, self.new_exp)
        elif button_text == 'π':
            self.currentVal = math.pi
            self.new_exp = str(self.currentVal)
            if self.bChangeop:
                self.bChangeop = False
            self.disp(0, None, 1, self.new_exp)
        elif button_text == 'e':
            self.currentVal = math.e
            self.new_exp = str(self.currentVal)
            if self.bChangeop:
                self.bChangeop = False
            self.disp(0, None, 1, self.new_exp)
        elif button_text == '1/x':
            self.currentVal = 1 / self.currentVal
            self.new_exp = str(self.currentVal)
            self.disp(0, None, 1, self.new_exp)
        elif button_text == 'rand':
            self.currentVal = random.random()
            self.new_exp = str(self.currentVal)
            self.disp(0, None, 1, self.new_exp)
        elif button_text == 'abs':
            self.currentVal = abs(self.currentVal)
            self.bInv = False
            self.new_exp = str(self.currentVal)
            self.disp(0, None, 1, self.new_exp)
        elif button_text == 'sqrt':
            try:
                self.currentVal = math.sqrt(self.currentVal)
            except Exception as e:
                self.ErrorHandler(e)
                return
            self.new_exp = str(self.currentVal)
            self.disp(0, None, 1, self.new_exp)
        elif button_text == 'exp':
            self.currentVal = math.exp(self.currentVal)
            self.new_exp = str(self.currentVal)
            self.disp(0, None, 1, self.new_exp)
        elif button_text == 'x!':
            try:
                self.currentVal = math.factorial(int(self.currentVal))
            except Exception as e:
                self.ErrorHandler(e)
                return
            self.new_exp = str(self.currentVal)
            self.disp(0, None, 1, self.new_exp)
        elif button_text == 'sin':
            self.currentVal = round(math.sin(math.radians(self.currentVal)), 10)
            self.new_exp = str(self.currentVal)
            self.disp(0, None, 1, self.new_exp)
        elif button_text == 'cos':
            self.currentVal = round(math.cos(math.radians(self.currentVal)), 10)
            self.new_exp = str(self.currentVal)
            self.disp(0, None, 1, self.new_exp)
        elif button_text == 'tan':
            try:
                self.currentVal = round(math.tan(math.radians(self.currentVal)), 10)
                if self.currentVal > 1e16:
                    raise OverflowError
            except Exception as e:
                self.ErrorHandler(e)
                return
            self.new_exp = str(self.currentVal)
            self.disp(0, None, 1, self.new_exp)
        elif button_text == 'arcsin':
            try:
                self.currentVal = round(math.asin(self.currentVal), 10)
            except Exception as e:
                self.ErrorHandler(e)
                return
            self.new_exp = str(self.currentVal)
            self.disp(0, None, 1, self.new_exp)
        elif button_text == 'arccos':
            try:
                self.currentVal = round(math.acos(self.currentVal), 10)
            except Exception as e:
                self.ErrorHandler(e)
                return
            self.new_exp = str(self.currentVal)
            self.disp(0, None, 1, self.new_exp)
        elif button_text == 'arctan':
            try:
                self.currentVal = round(math.atan(self.currentVal), 10)
            except Exception as e:
                self.ErrorHandler(e)
                return
            self.new_exp = str(self.currentVal)
            self.disp(0, None, 1, self.new_exp)
        elif button_text == 'C':
            if self.bError:
                self.bError = False
                buttons = self.findChildren(QPushButton)
                for button in buttons:
                    button.setDisabled(False)
            self.remake()

    def add_onclick_functions(self):
        buttons = self.findChildren(QPushButton)
        for button in buttons:
            button.clicked.connect(self.on_button_clicked)

    def ErrorHandler(self, e: Exception):
        self.bError = True
        exc_type, exc_obj, exc_tb = sys.exc_info()
        buttons = self.findChildren(QPushButton)
        for button in buttons:
            button.setDisabled(True)
        self.ui.btn_C.setDisabled(False)
        self.ui.side_display.setText("")
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(36)
        self.ui.display.setFont(font)
        self.ui.display.setText(f"Error: {exc_type.__name__}")

    def remake(self):
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(72)
        self.ui.display.setFont(font)
        self.old_exp = ""
        self.new_exp = ""
        self.currentVal = 0
        self.lastVal = 0
        self.bChangeop = False
        self.bInv = False
        self.bNoprev = True
        self.holdVal = ''
        self.disp(1, '', 1, '0')

    def isEmpty(self):
        if self.currentVal == 0 and self.new_exp == '':
            return True
        else:
            return False

    def disp(self, isChangeupper: bool, ut: str, isChangedown: bool, dt: str):
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        if isChangeupper:
            if len(ut) >= 60:
                font.setPointSize(10)
            elif len(ut) >= 30:
                font.setPointSize(15)
            else:
                font.setPointSize(20)
            self.ui.side_display.setFont(font)
            self.ui.side_display.setText(ut)
        if isChangedown:
            if self.isEmpty():
                self.ui.display.setText("0")
                return
            if len(dt) >= 20:
                font.setPointSize(18)
            elif len(dt) >= 10:
                font.setPointSize(36)
            else:
                font.setPointSize(72)
            self.ui.display.setFont(font)
            self.ui.display.setText(dt)

    def on_shift_clicked(self):
        if self.shift_change == False:  # 从白色到紫色
            self.ui.btn_shift.setStyleSheet("background-color: rgb(89, 27, 183);\n"
                                            "color: rgb(255,255,255);")
            self.ui.btn_fun_x2.setText("sin")
            self.ui.btn_fun_x3.setText("cos")
            self.ui.btn_fun_xy.setText("tan")
            self.ui.btn_fun_10x.setText("arcsin")
            self.ui.btn_fun_log.setText("arccos")
            self.ui.btn_fun_ln.setText("arctan")
            self.shift_change = True
        else:
            self.ui.btn_shift.setStyleSheet("background-color: rgb(249, 249, 249);\n"
                                            "color: #591BB7;")
            self.ui.btn_fun_x2.setText("x^2")
            self.ui.btn_fun_x3.setText("sqrt")
            self.ui.btn_fun_xy.setText("x^y")
            self.ui.btn_fun_10x.setText("10^x")
            self.ui.btn_fun_log.setText("log")
            self.ui.btn_fun_ln.setText("ln")
            self.shift_change = False


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    calculator.add_onclick_functions()
    sys.exit(app.exec_())
