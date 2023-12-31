# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cal.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Calculator(object):
    def setupUi(self, Calculator):
        Calculator.setObjectName("Calculator")
        Calculator.resize(600, 800)
        Calculator.setMinimumSize(QtCore.QSize(600, 800))
        Calculator.setMaximumSize(QtCore.QSize(600, 800))
        Calculator.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 3px;\n"
"    border:1px solid #BBBBBB\n"
"}\n"
"\n"
"* {\n"
"    background-color: rgb(243, 243, 243);\n"
"    border:none;\n"
"}")
        self.vboxlayout = QtWidgets.QVBoxLayout(Calculator)
        self.vboxlayout.setObjectName("vboxlayout")
        self.frame = QtWidgets.QFrame(Calculator)
        self.frame.setMinimumSize(QtCore.QSize(0, 110))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 110))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.vboxlayout.addWidget(self.frame)
        self.side_display = QtWidgets.QLineEdit(Calculator)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.side_display.sizePolicy().hasHeightForWidth())
        self.side_display.setSizePolicy(sizePolicy)
        self.side_display.setMinimumSize(QtCore.QSize(0, 35))
        self.side_display.setMaximumSize(QtCore.QSize(16777215, 35))
        self.side_display.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(20)
        self.side_display.setFont(font)
        self.side_display.setStyleSheet("color:#9A9A9A")
        self.side_display.setText("")
        self.side_display.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.side_display.setReadOnly(True)
        self.side_display.setObjectName("side_display")
        self.vboxlayout.addWidget(self.side_display)
        self.display = QtWidgets.QLineEdit(Calculator)
        self.display.setMinimumSize(QtCore.QSize(0, 110))
        self.display.setMaximumSize(QtCore.QSize(16777215, 110))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(72)
        self.display.setFont(font)
        self.display.setStyleSheet("color:#101010")
        self.display.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.display.setReadOnly(True)
        self.display.setObjectName("display")
        self.vboxlayout.addWidget(self.display)
        self.line = QtWidgets.QFrame(Calculator)
        self.line.setStyleSheet("border:3px solid rgb(187, 187, 187)")
        self.line.setMidLineWidth(15)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.vboxlayout.addWidget(self.line)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 6, 19)
        self.gridLayout.setHorizontalSpacing(8)
        self.gridLayout.setVerticalSpacing(22)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_shift = QtWidgets.QPushButton(Calculator)
        self.btn_shift.setMinimumSize(QtCore.QSize(111, 67))
        self.btn_shift.setMaximumSize(QtCore.QSize(111, 67))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(18)
        self.btn_shift.setFont(font)
        self.btn_shift.setStyleSheet("QPushButton{\n"
"    background-color: rgb(249, 249, 249);    \n"
"    color: #591BB7;\n"
"}\n"
"\n"
"QPushButton:hover { \n"
"    background-color: rgb(246, 246, 246);\n"
"    color: #591BB7;\n"
" }\n"
"QPushButton:disabled {\n"
"    background-color:rgb(244 , 244 , 244);\n"
"    color: rgb(100,100,100);\n"
" }\n"
"\n"
"")
        self.btn_shift.setObjectName("btn_shift")
        self.gridLayout.addWidget(self.btn_shift, 1, 0, 1, 1)
        self.btn_num2 = QtWidgets.QPushButton(Calculator)
        self.btn_num2.setMinimumSize(QtCore.QSize(111, 67))
        self.btn_num2.setMaximumSize(QtCore.QSize(111, 67))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(18)
        self.btn_num2.setFont(font)
        self.btn_num2.setStyleSheet("QPushButton:pressed {\n"
"    background-color:rgb(247 , 247 , 247);\n"
"    color: rgb(120,120,120);\n"
"}\n"
"QPushButton:hover { \n"
"    background-color: rgb(249, 249, 249);\n"
" }\n"
"QPushButton:disabled {\n"
"    background-color:rgb(244 , 244 , 244);\n"
"    color: rgb(100,100,100);\n"
" }")
        self.btn_num2.setObjectName("btn_num2")
        self.gridLayout.addWidget(self.btn_num2, 6, 2, 1, 1)
        self.btn_fun_1x = QtWidgets.QPushButton(Calculator)
        self.btn_fun_1x.setMinimumSize(QtCore.QSize(111, 67))
        self.btn_fun_1x.setMaximumSize(QtCore.QSize(111, 67))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(18)
        self.btn_fun_1x.setFont(font)
        self.btn_fun_1x.setStyleSheet("QPushButton {\n"
"    background-color: rgb(249, 249, 249);}\n"
"\n"
"QPushButton:pressed \n"
"{\n"
"    background-color:rgb(244 , 244 , 244);\n"
"    color: rgb(100,100,100);\n"
"}\n"
"QPushButton:hover { \n"
"    background-color: rgb(246, 246, 246);\n"
" }\n"
"QPushButton:disabled {\n"
"    background-color:rgb(244 , 244 , 244);\n"
"    color: rgb(100,100,100);\n"
" }\n"
"")
        self.btn_fun_1x.setObjectName("btn_fun_1x")
        self.gridLayout.addWidget(self.btn_fun_1x, 2, 1, 1, 1)
        self.btn_C = QtWidgets.QPushButton(Calculator)
        self.btn_C.setMinimumSize(QtCore.QSize(111, 67))
        self.btn_C.setMaximumSize(QtCore.QSize(111, 67))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(18)
        self.btn_C.setFont(font)
        self.btn_C.setStyleSheet("QPushButton {\n"
"    background-color: rgb(249, 249, 249);}\n"
"\n"
"QPushButton:pressed \n"
"{\n"
"    background-color:rgb(244 , 244 , 244);\n"
"    color: rgb(100,100,100);\n"
"}\n"
"QPushButton:hover { \n"
"    background-color: rgb(246, 246, 246);\n"
" }\n"
"QPushButton:disabled {\n"
"    background-color:rgb(244 , 244 , 244);\n"
"    color: rgb(100,100,100);\n"
" }\n"
"")
        self.btn_C.setObjectName("btn_C")
        self.gridLayout.addWidget(self.btn_C, 1, 3, 1, 1)
        self.btn_num4 = QtWidgets.QPushButton(Calculator)
        self.btn_num4.setMinimumSize(QtCore.QSize(111, 67))
        self.btn_num4.setMaximumSize(QtCore.QSize(111, 67))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(18)
        self.btn_num4.setFont(font)
        self.btn_num4.setStyleSheet("QPushButton:pressed {\n"
"    background-color:rgb(247 , 247 , 247);\n"
"    color: rgb(120,120,120);\n"
"}\n"
"QPushButton:hover { \n"
"    background-color: rgb(249, 249, 249);\n"
" }\n"
"QPushButton:disabled {\n"
"    background-color:rgb(244 , 244 , 244);\n"
"    color: rgb(100,100,100);\n"
" }")
        self.btn_num4.setObjectName("btn_num4")
        self.gridLayout.addWidget(self.btn_num4, 5, 1, 1, 1)
        self.btn_cal_plus = QtWidgets.QPushButton(Calculator)
        self.btn_cal_plus.setMinimumSize(QtCore.QSize(111, 67))
        self.btn_cal_plus.setMaximumSize(QtCore.QSize(111, 67))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(24)
        self.btn_cal_plus.setFont(font)
        self.btn_cal_plus.setStyleSheet("QPushButton {\n"
"    background-color: rgb(249, 249, 249);}\n"
"\n"
"QPushButton:pressed \n"
"{\n"
"    background-color:rgb(244 , 244 , 244);\n"
"    color: rgb(100,100,100);\n"
"}\n"
"QPushButton:hover { \n"
"    background-color: rgb(246, 246, 246);\n"
" }\n"
"QPushButton:disabled {\n"
"    background-color:rgb(244 , 244 , 244);\n"
"    color: rgb(100,100,100);\n"
" }\n"
"")
        self.btn_cal_plus.setObjectName("btn_cal_plus")
        self.gridLayout.addWidget(self.btn_cal_plus, 6, 4, 1, 1)
        self.btn_cal_equal = QtWidgets.QPushButton(Calculator)
        self.btn_cal_equal.setMinimumSize(QtCore.QSize(111, 67))
        self.btn_cal_equal.setMaximumSize(QtCore.QSize(111, 67))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(48)
        self.btn_cal_equal.setFont(font)
        self.btn_cal_equal.setStyleSheet("\n"
"QPushButton{\n"
"    background-color: #591BB7;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"    background-color:rgb(70, 10, 160);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover { \n"
"    background-color: rgb(80, 20, 170);\n"
"    color: rgb(255, 255, 255);\n"
" }\n"
"QPushButton:disabled {\n"
"    background-color:rgb(244 , 244 , 244);\n"
"    color: rgb(100,100,100);\n"
" }")
        self.btn_cal_equal.setObjectName("btn_cal_equal")
        self.gridLayout.addWidget(self.btn_cal_equal, 7, 4, 1, 1)
        self.btn_fun_sqrt = QtWidgets.QPushButton(Calculator)
        self.btn_fun_sqrt.setMinimumSize(QtCore.QSize(111, 67))
        self.btn_fun_sqrt.setMaximumSize(QtCore.QSize(111, 67))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(18)
        self.btn_fun_sqrt.setFont(font)
        self.btn_fun_sqrt.setStyleSheet("QPushButton {\n"
"    background-color: rgb(249, 249, 249);}\n"
"\n"
"QPushButton:pressed \n"
"{\n"
"    background-color:rgb(244 , 244 , 244);\n"
"    color: rgb(100,100,100);\n"
"}\n"
"QPushButton:hover { \n"
"    background-color: rgb(246, 246, 246);\n"
" }\n"
"QPushButton:disabled {\n"
"    background-color:rgb(244 , 244 , 244);\n"
"    color: rgb(100,100,100);\n"
" }\n"
"")
        self.btn_fun_sqrt.setObjectName("btn_fun_sqrt")
        self.gridLayout.addWidget(self.btn_fun_sqrt, 3, 2, 1, 1)
        self.btn_num8 = QtWidgets.QPushButton(Calculator)
        self.btn_num8.setMinimumSize(QtCore.QSize(111, 67))
        self.btn_num8.setMaximumSize(QtCore.QSize(111, 67))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(18)
        self.btn_num8.setFont(font)
        self.btn_num8.setStyleSheet("QPushButton:pressed {\n"
"    background-color:rgb(247 , 247 , 247);\n"
"    color: rgb(120,120,120);\n"
"}\n"
"QPushButton:hover { \n"
"    background-color: rgb(249, 249, 249);\n"
" }\n"
"QPushButton:disabled {\n"
"    background-color:rgb(244 , 244 , 244);\n"
"    color: rgb(100,100,100);\n"
" }")
        self.btn_num8.setObjectName("btn_num8")
        self.gridLayout.addWidget(self.btn_num8, 4, 2, 1, 1)
        self.btn_num9 = QtWidgets.QPushButton(Calculator)
        self.btn_num9.setMinimumSize(QtCore.QSize(111, 67))
        self.btn_num9.setMaximumSize(QtCore.QSize(111, 67))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(18)
        self.btn_num9.setFont(font)
        self.btn_num9.setStyleSheet("QPushButton:pressed {\n"
"    background-color:rgb(247 , 247 , 247);\n"
"    color: rgb(120,120,120);\n"
"}\n"
"QPushButton:hover { \n"
"    background-color: rgb(249, 249, 249);\n"
" }\n"
"QPushButton:disabled {\n"
"    background-color:rgb(244 , 244 , 244);\n"
"    color: rgb(100,100,100);\n"
" }")
        self.btn_num9.setObjectName("btn_num9")
        self.gridLayout.addWidget(self.btn_num9, 4, 3, 1, 1)
        self.btn_cal_minus = QtWidgets.QPushButton(Calculator)
        self.btn_cal_minus.setMinimumSize(QtCore.QSize(111, 67))
        self.btn_cal_minus.setMaximumSize(QtCore.QSize(111, 67))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(24)
        self.btn_cal_minus.setFont(font)
        self.btn_cal_minus.setStyleSheet("QPushButton {\n"
"    background-color: rgb(249, 249, 249);}\n"
"\n"
"QPushButton:pressed \n"
"{\n"
"    background-color:rgb(244 , 244 , 244);\n"
"    color: rgb(100,100,100);\n"
"}\n"
"QPushButton:hover { \n"
"    background-color: rgb(246, 246, 246);\n"
" }\n"
"QPushButton:disabled {\n"
"    background-color:rgb(244 , 244 , 244);\n"
"    color: rgb(100,100,100);\n"
" }\n"
"")
        self.btn_cal_minus.setObjectName("btn_cal_minus")
        self.gridLayout.addWidget(self.btn_cal_minus, 5, 4, 1, 1)
        self.btn_fun_bs = QtWidgets.QPushButton(Calculator)
        self.btn_fun_bs.setMinimumSize(QtCore.QSize(111, 67))
        self.btn_fun_bs.setMaximumSize(QtCore.QSize(111, 67))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(18)
        self.btn_fun_bs.setFont(font)
        self.btn_fun_bs.setStyleSheet("QPushButton {\n"
"    background-color: rgb(249, 249, 249);}\n"
"\n"
"QPushButton:pressed \n"
"{\n"
"    background-color:rgb(244 , 244 , 244);\n"
"    color: rgb(100,100,100);\n"
"}\n"
"QPushButton:hover { \n"
"    background-color: rgb(246, 246, 246);\n"
" }\n"
"QPushButton:disabled {\n"
"    background-color:rgb(244 , 244 , 244);\n"
"    color: rgb(100,100,100);\n"
" }\n"
"")
        self.btn_fun_bs.setObjectName("btn_fun_bs")
        self.gridLayout.addWidget(self.btn_fun_bs, 1, 4, 1, 1)
        self.btn_fun_ln = QtWidgets.QPushButton(Calculator)
        self.btn_fun_ln.setMinimumSize(QtCore.QSize(111, 67))
        self.btn_fun_ln.setMaximumSize(QtCore.QSize(111, 67))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(18)
        self.btn_fun_ln.setFont(font)
        self.btn_fun_ln.setStyleSheet("QPushButton {\n"
"    background-color: rgb(249, 249, 249);}\n"
"\n"
"QPushButton:pressed \n"
"{\n"
"    background-color:rgb(244 , 244 , 244);\n"
"    color: rgb(100,100,100);\n"
"}\n"
"QPushButton:hover { \n"
"    background-color: rgb(246, 246, 246);\n"
" }\n"
"QPushButton:disabled {\n"
"    background-color:rgb(244 , 244 , 244);\n"
"    color: rgb(100,100,100);\n"
" }\n"
"")
        self.btn_fun_ln.setObjectName("btn_fun_ln")
        self.gridLayout.addWidget(self.btn_fun_ln, 7, 0, 1, 1)
        self.btn_num6 = QtWidgets.QPushButton(Calculator)
        self.btn_num6.setMinimumSize(QtCore.QSize(111, 67))
        self.btn_num6.setMaximumSize(QtCore.QSize(111, 67))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(18)
        self.btn_num6.setFont(font)
        self.btn_num6.setStyleSheet("QPushButton:pressed {\n"
"    background-color:rgb(247 , 247 , 247);\n"
"    color: rgb(120,120,120);\n"
"}\n"
"QPushButton:hover { \n"
"    background-color: rgb(249, 249, 249);\n"
" }\n"
"QPushButton:disabled {\n"
"    background-color:rgb(244 , 244 , 244);\n"
"    color: rgb(100,100,100);\n"
" }")
        self.btn_num6.setObjectName("btn_num6")
        self.gridLayout.addWidget(self.btn_num6, 5, 3, 1, 1)
        self.btn_fun_x3 = QtWidgets.QPushButton(Calculator)
        self.btn_fun_x3.setMinimumSize(QtCore.QSize(111, 67))
        self.btn_fun_x3.setMaximumSize(QtCore.QSize(111, 67))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(18)
        self.btn_fun_x3.setFont(font)
        self.btn_fun_x3.setStyleSheet("QPushButton {\n"
"    background-color: rgb(249, 249, 249);}\n"
"\n"
"QPushButton:pressed \n"
"{\n"
"    background-color:rgb(244 , 244 , 244);\n"
"    color: rgb(100,100,100);\n"
"}\n"
"QPushButton:hover { \n"
"    background-color: rgb(246, 246, 246);\n"
" }\n"
"QPushButton:disabled {\n"
"    background-color:rgb(244 , 244 , 244);\n"
"    color: rgb(100,100,100);\n"
" }\n"
"")
        self.btn_fun_x3.setObjectName("btn_fun_x3")
        self.gridLayout.addWidget(self.btn_fun_x3, 3, 0, 1, 1)
        self.btn_neg = QtWidgets.QPushButton(Calculator)
        self.btn_neg.setMinimumSize(QtCore.QSize(111, 67))
        self.btn_neg.setMaximumSize(QtCore.QSize(111, 67))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(18)
        self.btn_neg.setFont(font)
        self.btn_neg.setStyleSheet("QPushButton:pressed {\n"
"    background-color:rgb(247 , 247 , 247);\n"
"    color: rgb(120,120,120);\n"
"}\n"
"QPushButton:hover { \n"
"    background-color: rgb(249, 249, 249);\n"
" }\n"
"QPushButton:disabled {\n"
"    background-color:rgb(244 , 244 , 244);\n"
"    color: rgb(100,100,100);\n"
" }")
        self.btn_neg.setObjectName("btn_neg")
        self.gridLayout.addWidget(self.btn_neg, 7, 1, 1, 1)
        self.btn_num5 = QtWidgets.QPushButton(Calculator)
        self.btn_num5.setMinimumSize(QtCore.QSize(111, 67))
        self.btn_num5.setMaximumSize(QtCore.QSize(111, 67))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(18)
        self.btn_num5.setFont(font)
        self.btn_num5.setStyleSheet("QPushButton:pressed {\n"
"    background-color:rgb(247 , 247 , 247);\n"
"    color: rgb(120,120,120);\n"
"}\n"
"QPushButton:hover { \n"
"    background-color: rgb(249, 249, 249);\n"
" }\n"
"QPushButton:disabled {\n"
"    background-color:rgb(244 , 244 , 244);\n"
"    color: rgb(100,100,100);\n"
" }")
        self.btn_num5.setObjectName("btn_num5")
        self.gridLayout.addWidget(self.btn_num5, 5, 2, 1, 1)
        self.btn_fun_x2 = QtWidgets.QPushButton(Calculator)
        self.btn_fun_x2.setMinimumSize(QtCore.QSize(111, 67))
        self.btn_fun_x2.setMaximumSize(QtCore.QSize(111, 67))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(18)
        self.btn_fun_x2.setFont(font)
        self.btn_fun_x2.setStyleSheet("QPushButton {\n"
"    background-color: rgb(249, 249, 249);}\n"
"\n"
"QPushButton:pressed \n"
"{\n"
"    background-color:rgb(244 , 244 , 244);\n"
"    color: rgb(100,100,100);\n"
"}\n"
"QPushButton:hover { \n"
"    background-color: rgb(246, 246, 246);\n"
" }\n"
"QPushButton:disabled {\n"
"    background-color:rgb(244 , 244 , 244);\n"
"    color: rgb(100,100,100);\n"
" }\n"
"")
        self.btn_fun_x2.setObjectName("btn_fun_x2")
        self.gridLayout.addWidget(self.btn_fun_x2, 2, 0, 1, 1)
        self.btn_num1 = QtWidgets.QPushButton(Calculator)
        self.btn_num1.setMinimumSize(QtCore.QSize(111, 67))
        self.btn_num1.setMaximumSize(QtCore.QSize(111, 67))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(18)
        self.btn_num1.setFont(font)
        self.btn_num1.setStyleSheet("QPushButton:pressed {\n"
"    background-color:rgb(247 , 247 , 247);\n"
"    color: rgb(120,120,120);\n"
"}\n"
"QPushButton:hover { \n"
"    background-color: rgb(249, 249, 249);\n"
" }\n"
"QPushButton:disabled {\n"
"    background-color:rgb(244 , 244 , 244);\n"
"    color: rgb(100,100,100);\n"
" }")
        self.btn_num1.setObjectName("btn_num1")
        self.gridLayout.addWidget(self.btn_num1, 6, 1, 1, 1)
        self.btn_fun_xfact = QtWidgets.QPushButton(Calculator)
        self.btn_fun_xfact.setMinimumSize(QtCore.QSize(111, 67))
        self.btn_fun_xfact.setMaximumSize(QtCore.QSize(111, 67))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(18)
        self.btn_fun_xfact.setFont(font)
        self.btn_fun_xfact.setStyleSheet("QPushButton {\n"
"    background-color: rgb(249, 249, 249);}\n"
"\n"
"QPushButton:pressed \n"
"{\n"
"    background-color:rgb(244 , 244 , 244);\n"
"    color: rgb(100,100,100);\n"
"}\n"
"QPushButton:hover { \n"
"    background-color: rgb(246, 246, 246);\n"
" }\n"
"QPushButton:disabled {\n"
"    background-color:rgb(244 , 244 , 244);\n"
"    color: rgb(100,100,100);\n"
" }\n"
"")
        self.btn_fun_xfact.setObjectName("btn_fun_xfact")
        self.gridLayout.addWidget(self.btn_fun_xfact, 3, 3, 1, 1)
        self.btn_fun_10x = QtWidgets.QPushButton(Calculator)
        self.btn_fun_10x.setMinimumSize(QtCore.QSize(111, 67))
        self.btn_fun_10x.setMaximumSize(QtCore.QSize(111, 67))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(18)
        self.btn_fun_10x.setFont(font)
        self.btn_fun_10x.setStyleSheet("QPushButton {\n"
"    background-color: rgb(249, 249, 249);}\n"
"\n"
"QPushButton:pressed \n"
"{\n"
"    background-color:rgb(244 , 244 , 244);\n"
"    color: rgb(100,100,100);\n"
"}\n"
"QPushButton:hover { \n"
"    background-color: rgb(246, 246, 246);\n"
" }\n"
"QPushButton:disabled {\n"
"    background-color:rgb(244 , 244 , 244);\n"
"    color: rgb(100,100,100);\n"
" }\n"
"")
        self.btn_fun_10x.setObjectName("btn_fun_10x")
        self.gridLayout.addWidget(self.btn_fun_10x, 5, 0, 1, 1)
        self.btn_fun_log = QtWidgets.QPushButton(Calculator)
        self.btn_fun_log.setMinimumSize(QtCore.QSize(111, 67))
        self.btn_fun_log.setMaximumSize(QtCore.QSize(111, 67))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(18)
        self.btn_fun_log.setFont(font)
        self.btn_fun_log.setStyleSheet("QPushButton {\n"
"    background-color: rgb(249, 249, 249);}\n"
"\n"
"QPushButton:pressed \n"
"{\n"
"    background-color:rgb(244 , 244 , 244);\n"
"    color: rgb(100,100,100);\n"
"}\n"
"QPushButton:hover { \n"
"    background-color: rgb(246, 246, 246);\n"
" }\n"
"QPushButton:disabled {\n"
"    background-color:rgb(244 , 244 , 244);\n"
"    color: rgb(100,100,100);\n"
" }\n"
"")
        self.btn_fun_log.setObjectName("btn_fun_log")
        self.gridLayout.addWidget(self.btn_fun_log, 6, 0, 1, 1)
        self.btn_cal_div = QtWidgets.QPushButton(Calculator)
        self.btn_cal_div.setMinimumSize(QtCore.QSize(111, 67))
        self.btn_cal_div.setMaximumSize(QtCore.QSize(111, 67))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(24)
        self.btn_cal_div.setFont(font)
        self.btn_cal_div.setStyleSheet("QPushButton {\n"
"    background-color: rgb(249, 249, 249);}\n"
"\n"
"QPushButton:pressed \n"
"{\n"
"    background-color:rgb(244 , 244 , 244);\n"
"    color: rgb(100,100,100);\n"
"}\n"
"QPushButton:hover { \n"
"    background-color: rgb(246, 246, 246);\n"
" }\n"
"QPushButton:disabled {\n"
"    background-color:rgb(244 , 244 , 244);\n"
"    color: rgb(100,100,100);\n"
" }\n"
"")
        self.btn_cal_div.setObjectName("btn_cal_div")
        self.gridLayout.addWidget(self.btn_cal_div, 3, 4, 1, 1)
        self.btn_dot = QtWidgets.QPushButton(Calculator)
        self.btn_dot.setMinimumSize(QtCore.QSize(111, 67))
        self.btn_dot.setMaximumSize(QtCore.QSize(111, 67))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(18)
        self.btn_dot.setFont(font)
        self.btn_dot.setStyleSheet("QPushButton:pressed {\n"
"    background-color:rgb(247 , 247 , 247);\n"
"    color: rgb(120,120,120);\n"
"}\n"
"QPushButton:hover { \n"
"    background-color: rgb(249, 249, 249);\n"
" }\n"
"QPushButton:disabled {\n"
"    background-color:rgb(244 , 244 , 244);\n"
"    color: rgb(100,100,100);\n"
" }")
        self.btn_dot.setObjectName("btn_dot")
        self.gridLayout.addWidget(self.btn_dot, 7, 3, 1, 1)
        self.btn_fun_abs = QtWidgets.QPushButton(Calculator)
        self.btn_fun_abs.setMinimumSize(QtCore.QSize(111, 67))
        self.btn_fun_abs.setMaximumSize(QtCore.QSize(111, 67))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(18)
        self.btn_fun_abs.setFont(font)
        self.btn_fun_abs.setStyleSheet("QPushButton {\n"
"    background-color: rgb(249, 249, 249);}\n"
"\n"
"QPushButton:pressed \n"
"{\n"
"    background-color:rgb(244 , 244 , 244);\n"
"    color: rgb(100,100,100);\n"
"}\n"
"QPushButton:hover { \n"
"    background-color: rgb(246, 246, 246);\n"
" }\n"
"QPushButton:disabled {\n"
"    background-color:rgb(244 , 244 , 244);\n"
"    color: rgb(100,100,100);\n"
" }\n"
"")
        self.btn_fun_abs.setObjectName("btn_fun_abs")
        self.gridLayout.addWidget(self.btn_fun_abs, 2, 2, 1, 1)
        self.btn_num7 = QtWidgets.QPushButton(Calculator)
        self.btn_num7.setMinimumSize(QtCore.QSize(111, 67))
        self.btn_num7.setMaximumSize(QtCore.QSize(111, 67))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(18)
        self.btn_num7.setFont(font)
        self.btn_num7.setStyleSheet("QPushButton:pressed {\n"
"    background-color:rgb(247 , 247 , 247);\n"
"    color: rgb(120,120,120);\n"
"}\n"
"QPushButton:hover { \n"
"    background-color: rgb(249, 249, 249);\n"
" }\n"
"QPushButton:disabled {\n"
"    background-color:rgb(244 , 244 , 244);\n"
"    color: rgb(100,100,100);\n"
" }")
        self.btn_num7.setObjectName("btn_num7")
        self.gridLayout.addWidget(self.btn_num7, 4, 1, 1, 1)
        self.btn_fun_exp = QtWidgets.QPushButton(Calculator)
        self.btn_fun_exp.setMinimumSize(QtCore.QSize(111, 67))
        self.btn_fun_exp.setMaximumSize(QtCore.QSize(111, 67))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(18)
        self.btn_fun_exp.setFont(font)
        self.btn_fun_exp.setStyleSheet("QPushButton {\n"
"    background-color: rgb(249, 249, 249);}\n"
"\n"
"QPushButton:pressed \n"
"{\n"
"    background-color:rgb(244 , 244 , 244);\n"
"    color: rgb(100,100,100);\n"
"}\n"
"QPushButton:hover { \n"
"    background-color: rgb(246, 246, 246);\n"
" }\n"
"QPushButton:disabled {\n"
"    background-color:rgb(244 , 244 , 244);\n"
"    color: rgb(100,100,100);\n"
" }\n"
"")
        self.btn_fun_exp.setObjectName("btn_fun_exp")
        self.gridLayout.addWidget(self.btn_fun_exp, 2, 3, 1, 1)
        self.btn_fun_rand = QtWidgets.QPushButton(Calculator)
        self.btn_fun_rand.setMinimumSize(QtCore.QSize(111, 67))
        self.btn_fun_rand.setMaximumSize(QtCore.QSize(111, 67))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(18)
        self.btn_fun_rand.setFont(font)
        self.btn_fun_rand.setStyleSheet("QPushButton {\n"
"    background-color: rgb(249, 249, 249);}\n"
"\n"
"QPushButton:pressed \n"
"{\n"
"    background-color:rgb(244 , 244 , 244);\n"
"    color: rgb(100,100,100);\n"
"}\n"
"QPushButton:hover { \n"
"    background-color: rgb(246, 246, 246);\n"
" }\n"
"QPushButton:disabled {\n"
"    background-color:rgb(244 , 244 , 244);\n"
"    color: rgb(100,100,100);\n"
" }\n"
"")
        self.btn_fun_rand.setObjectName("btn_fun_rand")
        self.gridLayout.addWidget(self.btn_fun_rand, 3, 1, 1, 1)
        self.btn_num0 = QtWidgets.QPushButton(Calculator)
        self.btn_num0.setMinimumSize(QtCore.QSize(111, 67))
        self.btn_num0.setMaximumSize(QtCore.QSize(111, 67))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(18)
        self.btn_num0.setFont(font)
        self.btn_num0.setStyleSheet("QPushButton:pressed {\n"
"    background-color:rgb(247 , 247 , 247);\n"
"    color: rgb(120,120,120);\n"
"}\n"
"QPushButton:hover { \n"
"    background-color: rgb(249, 249, 249);\n"
" }\n"
"QPushButton:disabled {\n"
"    background-color:rgb(244 , 244 , 244);\n"
"    color: rgb(100,100,100);\n"
" }")
        self.btn_num0.setObjectName("btn_num0")
        self.gridLayout.addWidget(self.btn_num0, 7, 2, 1, 1)
        self.btn_fun_e = QtWidgets.QPushButton(Calculator)
        self.btn_fun_e.setMinimumSize(QtCore.QSize(111, 67))
        self.btn_fun_e.setMaximumSize(QtCore.QSize(111, 67))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(18)
        self.btn_fun_e.setFont(font)
        self.btn_fun_e.setStyleSheet("QPushButton {\n"
"    background-color: rgb(249, 249, 249);}\n"
"\n"
"QPushButton:pressed \n"
"{\n"
"    background-color:rgb(244 , 244 , 244);\n"
"    color: rgb(100,100,100);\n"
"}\n"
"QPushButton:hover { \n"
"    background-color: rgb(246, 246, 246);\n"
" }\n"
"QPushButton:disabled {\n"
"    background-color:rgb(244 , 244 , 244);\n"
"    color: rgb(100,100,100);\n"
" }\n"
"")
        self.btn_fun_e.setObjectName("btn_fun_e")
        self.gridLayout.addWidget(self.btn_fun_e, 1, 2, 1, 1)
        self.btn_fun_pi = QtWidgets.QPushButton(Calculator)
        self.btn_fun_pi.setMinimumSize(QtCore.QSize(111, 67))
        self.btn_fun_pi.setMaximumSize(QtCore.QSize(111, 67))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(18)
        self.btn_fun_pi.setFont(font)
        self.btn_fun_pi.setStyleSheet("QPushButton {\n"
"    background-color: rgb(249, 249, 249);}\n"
"\n"
"QPushButton:pressed \n"
"{\n"
"    background-color:rgb(244 , 244 , 244);\n"
"    color: rgb(100,100,100);\n"
"}\n"
"QPushButton:hover { \n"
"    background-color: rgb(246, 246, 246);\n"
" }\n"
"QPushButton:disabled {\n"
"    background-color:rgb(244 , 244 , 244);\n"
"    color: rgb(100,100,100);\n"
" }\n"
"")
        self.btn_fun_pi.setObjectName("btn_fun_pi")
        self.gridLayout.addWidget(self.btn_fun_pi, 1, 1, 1, 1)
        self.btn_fun_xy = QtWidgets.QPushButton(Calculator)
        self.btn_fun_xy.setMinimumSize(QtCore.QSize(111, 67))
        self.btn_fun_xy.setMaximumSize(QtCore.QSize(111, 67))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(18)
        self.btn_fun_xy.setFont(font)
        self.btn_fun_xy.setStyleSheet("QPushButton {\n"
"    background-color: rgb(249, 249, 249);}\n"
"\n"
"QPushButton:pressed \n"
"{\n"
"    background-color:rgb(244 , 244 , 244);\n"
"    color: rgb(100,100,100);\n"
"}\n"
"QPushButton:hover { \n"
"    background-color: rgb(246, 246, 246);\n"
" }\n"
"QPushButton:disabled {\n"
"    background-color:rgb(244 , 244 , 244);\n"
"    color: rgb(100,100,100);\n"
" }\n"
"")
        self.btn_fun_xy.setObjectName("btn_fun_xy")
        self.gridLayout.addWidget(self.btn_fun_xy, 4, 0, 1, 1)
        self.btn_cal_mul = QtWidgets.QPushButton(Calculator)
        self.btn_cal_mul.setMinimumSize(QtCore.QSize(111, 67))
        self.btn_cal_mul.setMaximumSize(QtCore.QSize(111, 67))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(24)
        self.btn_cal_mul.setFont(font)
        self.btn_cal_mul.setStyleSheet("QPushButton {\n"
"    background-color: rgb(249, 249, 249);}\n"
"\n"
"QPushButton:pressed \n"
"{\n"
"    background-color:rgb(244 , 244 , 244);\n"
"    color: rgb(100,100,100);\n"
"}\n"
"QPushButton:hover { \n"
"    background-color: rgb(246, 246, 246);\n"
" }\n"
"QPushButton:disabled {\n"
"    background-color:rgb(244 , 244 , 244);\n"
"    color: rgb(100,100,100);\n"
" }\n"
"")
        self.btn_cal_mul.setObjectName("btn_cal_mul")
        self.gridLayout.addWidget(self.btn_cal_mul, 4, 4, 1, 1)
        self.btn_fun_mod = QtWidgets.QPushButton(Calculator)
        self.btn_fun_mod.setMinimumSize(QtCore.QSize(111, 67))
        self.btn_fun_mod.setMaximumSize(QtCore.QSize(111, 67))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(18)
        self.btn_fun_mod.setFont(font)
        self.btn_fun_mod.setStyleSheet("QPushButton {\n"
"    background-color: rgb(249, 249, 249);}\n"
"\n"
"QPushButton:pressed \n"
"{\n"
"    background-color:rgb(244 , 244 , 244);\n"
"    color: rgb(100,100,100);\n"
"}\n"
"QPushButton:hover { \n"
"    background-color: rgb(246, 246, 246);\n"
" }\n"
"QPushButton:disabled {\n"
"    background-color:rgb(244 , 244 , 244);\n"
"    color: rgb(100,100,100);\n"
" }\n"
"")
        self.btn_fun_mod.setObjectName("btn_fun_mod")
        self.gridLayout.addWidget(self.btn_fun_mod, 2, 4, 1, 1)
        self.btn_num3 = QtWidgets.QPushButton(Calculator)
        self.btn_num3.setMinimumSize(QtCore.QSize(111, 67))
        self.btn_num3.setMaximumSize(QtCore.QSize(111, 67))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(18)
        self.btn_num3.setFont(font)
        self.btn_num3.setStyleSheet("QPushButton:pressed {\n"
"    background-color:rgb(247 , 247 , 247);\n"
"    color: rgb(120,120,120);\n"
"}\n"
"QPushButton:hover { \n"
"    background-color: rgb(249, 249, 249);\n"
" }\n"
"QPushButton:disabled {\n"
"    background-color:rgb(244 , 244 , 244);\n"
"    color: rgb(100,100,100);\n"
" }")
        self.btn_num3.setObjectName("btn_num3")
        self.gridLayout.addWidget(self.btn_num3, 6, 3, 1, 1)
        self.vboxlayout.addLayout(self.gridLayout)

        self.retranslateUi(Calculator)
        QtCore.QMetaObject.connectSlotsByName(Calculator)

    def retranslateUi(self, Calculator):
        _translate = QtCore.QCoreApplication.translate
        Calculator.setWindowTitle(_translate("Calculator", "Calculator"))
        self.display.setText(_translate("Calculator", "0"))
        self.btn_shift.setText(_translate("Calculator", "shift"))
        self.btn_num2.setText(_translate("Calculator", "2"))
        self.btn_fun_1x.setText(_translate("Calculator", "1/x"))
        self.btn_C.setText(_translate("Calculator", "C"))
        self.btn_num4.setText(_translate("Calculator", "4"))
        self.btn_cal_plus.setText(_translate("Calculator", "+"))
        self.btn_cal_equal.setText(_translate("Calculator", "="))
        self.btn_fun_sqrt.setText(_translate("Calculator", "sqrt"))
        self.btn_num8.setText(_translate("Calculator", "8"))
        self.btn_num9.setText(_translate("Calculator", "9"))
        self.btn_cal_minus.setText(_translate("Calculator", "-"))
        self.btn_fun_bs.setText(_translate("Calculator", "DEL"))
        self.btn_fun_ln.setText(_translate("Calculator", "ln"))
        self.btn_num6.setText(_translate("Calculator", "6"))
        self.btn_fun_x3.setText(_translate("Calculator", "x^3"))
        self.btn_neg.setText(_translate("Calculator", "+/-"))
        self.btn_num5.setText(_translate("Calculator", "5"))
        self.btn_fun_x2.setText(_translate("Calculator", "x^2"))
        self.btn_num1.setText(_translate("Calculator", "1"))
        self.btn_fun_xfact.setText(_translate("Calculator", "x!"))
        self.btn_fun_10x.setText(_translate("Calculator", "10^x"))
        self.btn_fun_log.setText(_translate("Calculator", "log"))
        self.btn_cal_div.setText(_translate("Calculator", "/"))
        self.btn_dot.setText(_translate("Calculator", "."))
        self.btn_fun_abs.setText(_translate("Calculator", "abs"))
        self.btn_num7.setText(_translate("Calculator", "7"))
        self.btn_fun_exp.setText(_translate("Calculator", "exp"))
        self.btn_fun_rand.setText(_translate("Calculator", "rand"))
        self.btn_num0.setText(_translate("Calculator", "0"))
        self.btn_fun_e.setText(_translate("Calculator", "e"))
        self.btn_fun_pi.setText(_translate("Calculator", "π"))
        self.btn_fun_xy.setText(_translate("Calculator", "x^y"))
        self.btn_cal_mul.setText(_translate("Calculator", "*"))
        self.btn_fun_mod.setText(_translate("Calculator", "mod"))
        self.btn_num3.setText(_translate("Calculator", "3"))
