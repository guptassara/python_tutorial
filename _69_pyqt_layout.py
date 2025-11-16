# GUI
import sys

from PyQt5.QtWidgets import (
    QApplication,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool GUI")
        self.setGeometry(700, 300, 500, 500)
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        label1 = QLabel("#1", self)
        label2 = QLabel("2#", self)
        label3 = QLabel("#3", self)
        label4 = QLabel("#4", self)
        label5 = QLabel("#5", self)
        label6 = QLabel("#6", self)
        label7 = QLabel("#7", self)

        label1.setStyleSheet("background-color: red;")
        label2.setStyleSheet("background-color: orange;")
        label3.setStyleSheet("background-color: yellow;")
        label4.setStyleSheet("background-color: green;")
        label5.setStyleSheet("background-color: blue;")
        label6.setStyleSheet("background-color: indigo;")
        label7.setStyleSheet("background-color: violet;")

        # Vertical widgets

        # vbox = QVBoxLayout()

        # vbox.addWidget(label1)
        # vbox.addWidget(label2)
        # vbox.addWidget(label3)
        # vbox.addWidget(label4)
        # vbox.addWidget(label5)
        # vbox.addWidget(label6)
        # vbox.addWidget(label7)

        # central_widget.setLayout(vbox)

        # Horizontal widgets

        # hbox = QHBoxLayout()

        # hbox.addWidget(label1)
        # hbox.addWidget(label2)
        # hbox.addWidget(label3)
        # hbox.addWidget(label4)
        # hbox.addWidget(label5)
        # hbox.addWidget(label6)
        # hbox.addWidget(label7)

        # central_widget.setLayout(hbox)

        # Grid widgets

        grid = QGridLayout()

        grid.addWidget(label1, 0, 0)
        grid.addWidget(label2, 0, 1)
        grid.addWidget(label3, 0, 2)
        grid.addWidget(label4, 1, 0)
        grid.addWidget(label5, 1, 1)
        grid.addWidget(label6, 1, 2)
        grid.addWidget(label7, 2, 0)

        central_widget.setLayout(grid)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
