import sys

from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtGui import QFont, QFontDatabase
from PyQt5.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class StopWatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0, 0, 0, 0)
        self.time_label = QLabel("00:00:00", self)
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Stopwatch")

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)

        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        hbox = QHBoxLayout()

        hbox.addWidget(self.start_button)
        hbox.addWidget(self.reset_button)
        hbox.addWidget(self.stop_button)

        vbox.addLayout(hbox)

        self.time_label.setObjectName("time_Label")
        self.start_button.setObjectName("start_button")
        self.reset_button.setObjectName("reset_button")
        self.stop_button.setObjectName("stop_button")

        font_id = QFontDatabase.addApplicationFont(
            "assets\\Space_Mono\\SpaceMono-Regular.ttf"
        )
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family, 150)
        self.time_label.setFont(my_font)

        self.setStyleSheet(
            """
            QWidget {
                background-color: #F8E9FF;
            }

            QLabel{
                color: #4B157A;
                font-size: 90px;
                letter-spacing: 2px;
            }

            QPushButton {
                font-family: my_font;
                font-size: 26px;
                color: #4B157A;
                padding: 18px 28px;
                border-radius: 22px;
                border: none;
            }

            QPushButton#start_button {
                background-color: #FFB7D5;
            }
            QPushButton#reset_button {
                background-color: #C7E9FF;
            }
            QPushButton#stop_button {
                background-color: #E9D1FF;
            }

            QPushButton#start_button:hover {
                background-color: #FF6FA3;
            }
            QPushButton#reset_button:hover {
                background-color: #7CC4F2;
            }
            QPushButton#stop_button:hover {
                background-color: #C18CFF;
            }
        """
        )

        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)

    def start(self):
        self.timer.start(10)

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText(self.format_time(self.time))

    def format_time(self, time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec() // 10
        return f"{hours:02}:{minutes:02}:{seconds:02}:{milliseconds:02}"

    def update_display(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    stopwatch = StopWatch()
    stopwatch.show()
    sys.exit(app.exec_())
