# GUI
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My second cool GUI")
        self.setGeometry(700, 300, 500, 500)

        label = QLabel("Hello", self)
        label.setFont(QFont("Algerian", 42))
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet(
            "color: #8c1c3c;background-color: #240b4a;"
            "font-weight: bold;"
            "font-style: italic;"
            "text-decoration: underline;"
        )

        # label.setAlignment(Qt.AlignBottom)  # vertically Bottom
        # label.setAlignment(Qt.AlignmentFlag.AlignTop)   # vertically top
        # label.setAlignment(Qt.AlignmentFlag.AlignHCenter)   # vertically center
        # label.setAlignment(Qt.AlignHCenter)  # horizontal center
        # label.setAlignment(Qt.AlignRight)   # horizontal right
        # label.setAlignment(Qt.AlignLeft)   # horizontal left
        label.setAlignment(Qt.AlignCenter)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
