import sys
import math
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QGridLayout
from ui_cal import Ui_Calculator


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Calculator()
        self.ui.setupUi(self)

    def on_button_clicked(self):
        clicked_button = self.sender()
        button_text = clicked_button.text()

        if button_text == '=':
            try:
                result = eval(self.expression)
                self.display.setText(str(result))
                self.expression = str(result)
            except:
                self.display.setText("Error")
                self.expression = ""
        elif button_text == 'sqrt':
            if len(self.expression) > 0:
                result = math.sqrt(eval(self.expression))
                self.display.setText(str(result))
                self.expression = str(result)
        elif button_text == 'sin':
            if len(self.expression) > 0:
                result = math.sin(math.radians(eval(self.expression)))
                self.display.setText(str(result))
                self.expression = str(result)
        elif button_text == 'cos':
            if len(self.expression) > 0:
                result = math.cos(math.radians(eval(self.expression)))
                self.display.setText(str(result))
                self.expression = str(result)
        elif button_text == 'tan':
            if len(self.expression) > 0:
                result = math.tan(math.radians(eval(self.expression)))
                self.display.setText(str(result))
                self.expression = str(result)
        else:
            self.expression += button_text
            self.display.setText(self.expression)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())
