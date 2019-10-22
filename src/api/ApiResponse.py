from typing import List

from api.CalculatedRate import CalculatedRate


class ApiResponse:
    """
    Class to represent the api response
    """

    def __init__(self, amount: float, base: str, date: str, rates: List[CalculatedRate] = None):
        """
        Constructor

        :param amount: Amount in base currency to be converted
        :param base: Base Currency
        :param date: when was the data
        :param rates: A list of calculated rates
        """
        self.amount = amount
        self.base = base
        self.date = date
        self.rates = {} if rates is None else rates

    def __str__(self) -> str:
        """
        Converts it to a formated string with all rates added in the output
        """
        ret = ""

        ret += "<b>{:.2f} {}</b> entsprechen<br>".format(self.amount, self.base)
        ret += "<ul>"

        for r in self.rates:
            ret += str(r)

        ret += "</ul>"
        ret += "<br>Stand: {}".format(self.date)

        return ret
