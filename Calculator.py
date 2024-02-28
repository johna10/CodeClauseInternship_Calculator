import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QLineEdit, QPushButton, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Calculator')
        self.setGeometry(100, 100, 400, 600)

        # Main layout
        main_layout = QVBoxLayout()

        # Create and configure the label for "Calculator"
        label = QLabel('Calculator')
        label.setAlignment(Qt.AlignCenter)  # Align the text to the center
        # Set a decorative font: family, point size, weight, and italic
        label.setFont(QFont('Verdana', 18, QFont.Bold))
        main_layout.addWidget(label)  # Add the label to the main layout at the top

        # Create and configure the display QLineEdit
        self.result_display = QLineEdit(self)
        self.result_display.setFixedHeight(100)
        self.result_display.setStyleSheet('font-size: 24px;')
        self.result_display.setAlignment(Qt.AlignRight)
        self.result_display.setReadOnly(True)
        main_layout.addWidget(self.result_display)  # Add the display below the label

        button_layout = QGridLayout()

        buttons = [
            'C', '7', '8', '9', '/',
            '=', '4', '5', '6', '*',
            '0', '1', '2', '3', '-',
            '.', '00', '000', '=', '+'
        ]

        row_val = 0
        col_val = 0

        for button_text in buttons:
            button = QPushButton(button_text, self)
            button.setFixedSize(80, 80)
            button.setStyleSheet('font-size: 18px; background-color: #fbc02d; border: 1px solid #e0e0e0;')
            button.clicked.connect(lambda state, text=button_text: self.on_button_click(text))
            button_layout.addWidget(button, row_val, col_val)
            col_val += 1
            if col_val == 5:  # Reset column to 0 when it reaches 5, move to next row
                col_val = 0
                row_val += 1

        main_layout.addLayout(button_layout)  # Add the buttons layout below the display

        self.setLayout(main_layout)

        self.show()

    def on_button_click(self, button_value):
        if button_value == '=':
            try:
                result = eval(self.result_display.text())
                self.result_display.setText(str(result))
            except Exception as e:
                self.result_display.setText("Error")
        elif button_value == 'C':
            self.result_display.clear()
        else:
            self.result_display.insert(button_value)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc_app = CalculatorApp()
    sys.exit(app.exec_())
