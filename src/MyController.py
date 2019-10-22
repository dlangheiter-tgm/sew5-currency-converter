from PyQt5.QtWidgets import QApplication, QMainWindow

from api import BaseApi
from api.LiveApi import LiveApi
from api.MockApi import MockApi
from gui import MyView
import sys


class MyController(QMainWindow):
    """
    Das ist der Controller
    """

    def set_message(self, message: str, time: int = 3000) -> None:
        """
        Set the statusbar message

        :param message: the message to be shown
        :param time: how long the message should be shown in ms
        """
        self.myForm.statusbar.showMessage(message, time)

    def set_output(self, text: str) -> None:
        """
        Sets the output to the given string

        :param text: Text to be set in the output
        """
        self.myForm.output.clear()
        self.myForm.output.append(text)

    def validate_input(self) -> None:
        """
        Validates the gathered input data

        :raise: Exception if a validation fails with the text of the error message
        """
        if len(self.currency) != 3:
            raise Exception("Währung muss 3 Zeichen lang sein")

        for t in self.targets:
            if len(t) != 3:
                raise Exception("Ziehlwärungen müssen drei Zeichen lang und mit ',' getrennt sein.")

    def read_values(self) -> None:
        """
        Reads the values from the GUI
        """
        self.amount = self.myForm.amount.value()
        self.currency = self.myForm.currency.text().strip().upper()
        self.target_currency = self.myForm.targetCurrency.text().strip().upper()
        self.targets = list(map(lambda s: s.strip(), self.target_currency.split(","))) if self.target_currency else []

    def calc_click(self) -> None:
        """
        Callback for when the calculate button is pressed
        """
        self.read_values()

        # Validated the input
        try:
            self.validate_input()
        except Exception as e:
            self.set_message(str(e))
            return

        # Tries to convert the currency and display
        try:
            res = self.strategy.calculate_rates(self.amount, self.currency, self.targets)

            self.set_output(str(res))
        except Exception as e:
            print(e)
            self.set_message(str(e))

    def live_click(self, checked: bool) -> None:
        """
        Callback for when the live-data toggle is clicked

        :param checked: If the toggle is checked
        """
        self.strategy = LiveApi() if checked else MockApi()

    def __init__(self):
        """
        Constructor
        """
        super().__init__(None)

        self.myForm = MyView.Ui_MainWindow()
        self.myForm.setupUi(self)
        self.myForm.amount.setMaximum(100000000)

        self.strategy = LiveApi()
        self.amount = 0
        self.currency = ""
        self.target_currency = ""
        self.targets = []
        self.life_data = True

        self.myForm.calculate.clicked.connect(self.calc_click)
        self.myForm.liveData.clicked.connect(self.live_click)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    c = MyController()
    c.show()
    sys.exit(app.exec_())
