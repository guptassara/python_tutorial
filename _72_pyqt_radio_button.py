# GUI
import sys

from PyQt5.QtWidgets import QApplication, QButtonGroup, QMainWindow, QRadioButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first cool GUI")
        self.setGeometry(700, 300, 500, 700)
        self.radio1 = QRadioButton("Pyro", self)
        self.radio2 = QRadioButton("Cryo", self)
        self.radio3 = QRadioButton("Hydro", self)
        self.radio4 = QRadioButton("Electro", self)
        self.radio5 = QRadioButton("Dendro", self)
        self.radio6 = QRadioButton("Anemo", self)
        self.radio7 = QRadioButton("Geo", self)
        self.radiow1 = QRadioButton("Sword", self)
        self.radiow2 = QRadioButton("Claymore", self)
        self.radiow3 = QRadioButton("Bow", self)
        self.radiow4 = QRadioButton("Polearm", self)
        self.radiow5 = QRadioButton("Catalyst", self)

        self.button_group_element = QButtonGroup(self)
        self.button_group_weapon = QButtonGroup(self)
        self.initUI()

    def initUI(self):
        self.radio1.setGeometry(0, 0, 300, 50)
        self.radio2.setGeometry(0, 50, 300, 50)
        self.radio3.setGeometry(0, 100, 300, 50)
        self.radio4.setGeometry(0, 150, 300, 50)
        self.radio5.setGeometry(0, 200, 300, 50)
        self.radio6.setGeometry(0, 250, 300, 50)
        self.radio7.setGeometry(0, 300, 300, 50)
        self.radiow1.setGeometry(0, 350, 300, 50)
        self.radiow2.setGeometry(0, 400, 300, 50)
        self.radiow3.setGeometry(0, 450, 300, 50)
        self.radiow4.setGeometry(0, 500, 300, 50)
        self.radiow5.setGeometry(0, 550, 300, 50)

        self.setStyleSheet(
            "QRadioButton{font-size: 40px;font-family: Forte;padding: 10px;}"
        )

        self.button_group_element.addButton(self.radio1)
        self.button_group_element.addButton(self.radio2)
        self.button_group_element.addButton(self.radio3)
        self.button_group_element.addButton(self.radio4)
        self.button_group_element.addButton(self.radio5)
        self.button_group_element.addButton(self.radio6)
        self.button_group_element.addButton(self.radio7)
        self.button_group_weapon.addButton(self.radiow1)
        self.button_group_weapon.addButton(self.radiow2)
        self.button_group_weapon.addButton(self.radiow3)
        self.button_group_weapon.addButton(self.radiow4)
        self.button_group_weapon.addButton(self.radiow5)

        self.radio1.toggled.connect(self.radio_button_changed)
        self.radio2.toggled.connect(self.radio_button_changed)
        self.radio3.toggled.connect(self.radio_button_changed)
        self.radio4.toggled.connect(self.radio_button_changed)
        self.radio5.toggled.connect(self.radio_button_changed)
        self.radio6.toggled.connect(self.radio_button_changed)
        self.radio7.toggled.connect(self.radio_button_changed)
        self.radiow1.toggled.connect(self.radio_button_changed_other)
        self.radiow2.toggled.connect(self.radio_button_changed_other)
        self.radiow3.toggled.connect(self.radio_button_changed_other)
        self.radiow4.toggled.connect(self.radio_button_changed_other)
        self.radiow5.toggled.connect(self.radio_button_changed_other)

    def radio_button_changed(self):
        radio_button = self.sender()
        if radio_button.isChecked():
            print(f"{radio_button.text()} is selected")

    def radio_button_changed_other(self):
        radio_button_other = self.sender()
        if radio_button_other.isChecked():
            print(f"{radio_button_other.text()} is selected")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
