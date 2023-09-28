import random
import sys
import unittest
import math
from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
from calculator import Calculator

buttons = {
    'shift': 'btn_shift',
    'x^2': 'btn_fun_x2',
    'x^3': 'btn_fun_x3',
    'x^y': 'btn_fun_xy',
    '10^x': 'btn_fun_10x',
    'log': 'btn_fun_log',
    'ln': 'btn_fun_ln',
    'pi': 'btn_fun_pi',
    'e': 'btn_fun_e',
    'C': 'btn_C',
    'DEL': 'btn_fun_bs',
    '1/x': 'btn_fun_1x',
    'abs': 'btn_fun_abs',
    'exp': 'btn_fun_exp',
    'mod': 'btn_fun_mod',
    'rand': 'btn_fun_rand',
    'sqrt': 'btn_fun_sqrt',
    'x!': 'btn_fun_xfact',
    '1': 'btn_num1',
    '2': 'btn_num2',
    '3': 'btn_num3',
    '4': 'btn_num4',
    '5': 'btn_num5',
    '6': 'btn_num6',
    '7': 'btn_num7',
    '8': 'btn_num8',
    '9': 'btn_num9',
    '0': 'btn_num0',
    '+/-': 'btn_neg',
    '.': 'btn_dot',
    '+': 'btn_cal_plus',
    '-': 'btn_cal_minus',
    '*': 'btn_cal_mul',
    '/': 'btn_cal_div',
    '=': 'btn_cal_equal'
}


def create_random_int(op: str, aub=1000000, bub=1000000):
    random.seed()
    a = random.randint(1, aub)
    b = random.randint(1, bub)
    return [a, b, eval('a' + op + 'b')]


class TestCalculator(unittest.TestCase):

    def click_button(self, button_name: str):
        button = self.calculator.findChild(QPushButton, buttons[button_name])
        QTest.mouseClick(button, Qt.LeftButton)

    def exec_exp(self, a, op, b, num=2):
        a = str(a)
        b = str(b)
        aInv = False
        bInv = False
        if a[0] == '-':
            aInv = True
            a = a[1:]
        if b[0] == '-':
            bInv = True
            b = b[1:]
        if num == 2:
            # input a
            for digit in a:
                self.click_button(digit)
            if aInv:
                self.click_button('+/-')
            self.click_button(op)
            for digit in b:
                self.click_button(digit)
            if bInv:
                self.click_button('+/-')
            self.click_button('=')
            return self.calculator.currentVal
        else:
            for digit in a:
                self.click_button(digit)
            if aInv:
                self.click_button('+/-')
            self.click_button(op)
            return self.calculator.currentVal

    def setUp(self):
        self.app = QApplication([])
        self.calculator = Calculator()
        self.calculator.add_onclick_functions()

    def tearDown(self):
        self.calculator.close()

    def test_add(self):
        [a, b, expect_value] = create_random_int('+')
        res = self.exec_exp(a, '+', b)
        self.assertEqual(res, expect_value)

    def test_sub(self):
        [a, b, expect_value] = create_random_int('-')
        res = self.exec_exp(a, '-', b)
        self.assertEqual(res, expect_value)

    def test_mul(self):
        [a, b, expect_value] = create_random_int('*')
        res = self.exec_exp(a, '*', b)
        self.assertEqual(res, expect_value)

    def test_div(self):
        [a, b, expect_value] = create_random_int('/')
        res = self.exec_exp(a, '/', b)
        self.assertEqual(res, expect_value)

    def test_equ_times(self):
        [a, b, expect_value] = create_random_int('+', 10, 10)
        res = self.exec_exp(a, '+', b)
        self.click_button("=")
        self.click_button("=")
        self.click_button("=")
        self.assertEqual(self.calculator.currentVal, expect_value + b + b + b)

    def test_change_sym(self):
        self.click_button("2")
        self.click_button("+")
        self.click_button("8")
        self.click_button("*")
        self.click_button("/")
        self.assertEqual(self.calculator.currentVal, 10)

    def test_equal_next(self):
        [a, b, expect_value] = create_random_int('+')
        res = self.exec_exp(a, '+', b)
        self.click_button("*")
        self.click_button("6")
        self.click_button("=")
        self.assertEqual(self.calculator.currentVal, res * 6)

    def test_x2(self):
        a = random.randint(-1000, 1000)
        res = self.exec_exp(a, 'x^2', None, 1)
        self.assertEqual(res, a ** 2)

    def test_x3(self):
        a = random.randint(-100, 100)
        res = self.exec_exp(a, 'x^3', None, 1)
        self.assertEqual(res, a ** 3)

    def test_xy(self):
        [a, b, expect_value] = create_random_int('**', 10, 10)
        res = self.exec_exp(a, 'x^y', b, 2)
        self.assertEqual(res, expect_value)

    def test_10x(self):
        a = random.randint(0, 10)
        res = self.exec_exp(a, '10^x', None, 1)
        self.assertEqual(res, 10 ** a)

    def test_log(self):
        a = random.randint(1, 1000000)
        res = self.exec_exp(a, 'log', None, 1)
        self.assertEqual(res, math.log10(a))

    def test_ln(self):
        a = random.randint(1, 1000000)
        res = self.exec_exp(a, 'ln', None, 1)
        self.assertEqual(res, math.log(a))

    def test_sin(self):
        self.shift_change = False
        a = random.randint(0, 180)
        self.click_button("shift")
        res = self.exec_exp(a, 'x^2', None, 1)
        self.assertEqual(res, round(math.sin(math.radians(a)), 10))

    def test_cos(self):
        self.shift_change = False
        a = random.randint(0, 180)
        self.click_button("shift")
        res = self.exec_exp(a, 'x^3', None, 1)
        self.assertEqual(res, round(math.cos(math.radians(a)), 10))

    def test_tan(self):
        a = 90
        while a == 90:
            a = random.randint(1, 179)
        self.click_button("shift")
        res = self.exec_exp(a, 'x^y', None, 1)
        self.assertEqual(res, round(math.tan(math.radians(a)), 10))

    def test_asin(self):
        a = random.uniform(-1, 1)
        self.click_button("shift")
        res = self.exec_exp(a, '10^x', 0, 1)
        self.assertEqual(res, round(math.asin(a), 10))

    def test_acos(self):
        a = random.uniform(-1, 1)
        self.click_button("shift")
        res = self.exec_exp(a, 'log', 0, 1)
        self.assertEqual(res, round(math.acos(a), 10))

    def test_atan(self):
        a = random.uniform(-1000, 1000)
        self.click_button("shift")
        self.click_button("shift")
        self.click_button("shift")
        res = self.exec_exp(a, 'ln', 0, 1)
        self.assertEqual(res, round(math.atan(a), 10))

    def test_pi(self):
        a = math.pi
        self.click_button('pi')
        self.assertEqual(a, self.calculator.currentVal)

    def test_e(self):
        a = math.e
        self.click_button('e')
        self.assertEqual(a, self.calculator.currentVal)

    def test_C(self):
        self.click_button('C')
        self.assertEqual(0, self.calculator.currentVal)

    def test_del(self):
        a = str(random.randint(100, 1000000))
        b = random.randint(1, len(a) - 1)
        for digits in str(a):
            self.click_button(digits)
        for i in range(b):
            self.click_button('DEL')
        self.assertEqual(self.calculator.currentVal, eval(a[:-b]))

    def test_abs(self):
        a = random.randint(-10000, 0)
        res = self.exec_exp(a, 'abs', 0, 1)
        self.assertEqual(res, abs(a))

    def test_1x(self):
        a = random.uniform(-10000, 10000)
        res = self.exec_exp(a, '1/x', None, 1)
        self.assertEqual(res, 1 / a)

    def test_exp(self):
        a = random.uniform(-10, 10)
        res = self.exec_exp(a, 'exp', 0, 1)
        self.assertEqual(res, math.exp(a))

    def test_mod(self):
        [a, b, expect_value] = create_random_int('%')
        res = self.exec_exp(a, 'mod', b, 2)
        self.assertEqual(res, expect_value)

    def test_sqrt(self):
        a = random.randint(0, 100000)
        res = self.exec_exp(a, 'sqrt', None, 1)
        self.assertEqual(res, math.sqrt(a))

    def test_fact(self):
        a = random.randint(0, 10)
        res = self.exec_exp(a, 'x!', None, 1)
        self.assertEqual(res, math.factorial(a))

    def test_equal_change_op(self):
        self.click_button('1')
        self.click_button('4')
        self.click_button('*')
        self.click_button('=')
        self.assertEqual(self.calculator.currentVal, 196)

    def test_error(self):
        self.click_button('8')
        self.click_button('/')
        self.click_button('0')
        self.click_button('=')
        self.assertEqual(self.calculator.ui.display.text(), "Error: ZeroDivisionError")


if __name__ == '__main__':
    unittest.main()
