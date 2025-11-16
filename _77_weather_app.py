import sys

import requests
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QFontDatabase, QIcon
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter city name: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get weather", self)
        self.temparature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)

        self.initUI()

    def initUI(self):
        self.setWindowIcon(QIcon("weather_app_assets\\images\\icon.jpeg"))
        self.setWindowTitle("Weather App")

        font_id = QFontDatabase.addApplicationFont(
            "assets\\fonts\\Reem_Kufi_Fun\\ReemKufiFun-Regular.ttf"
        )
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family)
        self.setFont(my_font)

        vbox = QVBoxLayout()

        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temparature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.city_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.temparature_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.description_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temparature_label.setObjectName("temparature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        self.setStyleSheet("""
            QWidget{
                background-color: #FDEBFF;
                color: #4A0B78;
            }
            QLabel#city_label{
                font-size: 40px;
                font-weight: 500;
            }
            QLineEdit#city_input{
                font-size: 30px;
                background-color: #E8F3FF;
                border: 2px solid #B983FF;
                border-radius: 12px;
                padding: 10px 14px;
            }
            QLabel#temparature_label{
                font-size: 50px;
            }
            QPushButton{
                background-color: #FFC1E3;
                color: #4A0B78;
                font-size: 22px;
                padding: 12px 20px;
                border-radius: 18px;
            }
            QPushButton:hover {
                background-color: #FF8FC8;
            }
            QPushButton:pressed {
                background-color: #E95FA9;
            }
            QLabel#emoji_label{
                font-size: 100px;
            }
            QLabel#description_label {
                font-size: 50px;
            }
            """)

        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):
        api_key = "ebac25739a743d8899a543b4cedf730d"
        city = self.city_input.text()
        url = (
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        )
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data["cod"] == 200:
                self.display_weather(data)

        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.display_error("Bad request:\nPlease check your input")
                case 401:
                    self.display_error("Unauthorized:\nInvalid API key")
                case 403:
                    self.display_error("Forbidden:\nAccess Denied")
                case 404:
                    self.display_error("Not found:\ncity not Found")
                case 500:
                    self.display_error("Internal server error:\nPlease try again later")
                case 502:
                    self.display_error("Bad gateway:\nInvalid response from the server")
                case 503:
                    self.display_error("Service unavailable:\nServer is down")
                case 504:
                    self.display_error("Gateway Timeout:\nNo response from the server")
                case _:
                    self.display_error(f"HTTP error occured:\n{http_error}")

        except requests.exceptions.Timeout:
            self.display_error("Connection error:\nthe request timed out")

        except requests.exceptions.ConnectionError:
            self.display_error("Connetion error:\ncheck your internet connection")

        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many redirects:\nCheck the URL")

        except requests.exceptions.RequestException as http_error:
            self.display_error(f"Rquest Error:\n{http_error}")

    def display_error(self, message):
        self.temparature_label.setStyleSheet("font-size: 30px")
        self.temparature_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()

    def display_weather(self, data):
        self.temparature_label.setStyleSheet("font-size: 50px")
        temparature_k = data["main"]["temp"]
        temparature_c = temparature_k - 273.15
        temparature_f = (temparature_k * 9 / 5) - 459.67
        weather_description = data["weather"][0]["description"]
        weather_id = data["weather"][0]["id"]
        # print(data)

        self.temparature_label.setText(
            f"{temparature_c:.0f} °C\n{temparature_f:.0f} °f"
        )
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.description_label.setText(weather_description)

    @staticmethod
    def get_weather_emoji(weather_id):
        if 200 <= weather_id <= 232:
            return "⛈️"
        elif 300 <= weather_id <= 321:
            return "🌥️"
        elif 500 <= weather_id <= 531:
            return "🌧️"
        elif 600 <= weather_id <= 622:
            return "❄️"
        elif 701 <= weather_id <= 741:
            return "🌫️"
        elif weather_id == 762:
            return "🌋"
        elif weather_id == 771:
            return "💨"
        elif weather_id == 781:
            return "🌪️"
        elif weather_id == 800:
            return "🌞"
        elif 801 <= weather_id <= 804:
            return "☁️"
        else:
            return ""


if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
