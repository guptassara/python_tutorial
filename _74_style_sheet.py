# GUI
import sys

from PyQt5.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QPushButton, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button1 = QPushButton("#1")
        self.button2 = QPushButton("#2")
        self.button3 = QPushButton("#3")
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        hbox = QHBoxLayout()

        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        central_widget.setLayout(hbox)

        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")

        self.setStyleSheet("""
            QPushButton {
                font-size: 40px;
                font-family: Forte;
                padding: 75px;
                margin: 25px;
                border: 3px solid;
                border-radius: 15px;
            }

            QPushButton#button1 {
                background-color: #FFB7D5;
            }
            QPushButton#button2 {
                background-color: #C7E9FF;
            }
            QPushButton#button3 {
                background-color: #F6E6FF;
            }

            QPushButton#button1:hover {
                background-color: #FF6FA3;
            }
            QPushButton#button2:hover {
                background-color: #7CC4F2;
            }
            QPushButton#button3:hover {
                background-color: #D3A6F7;
            }
        """)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
