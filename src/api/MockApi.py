from typing import List
import json
from pathlib import Path

from api.ApiResponse import ApiResponse
from api.BaseApi import BaseApi
from api.CalculatedRate import CalculatedRate


class MockApi(BaseApi):
    """
    Api for when no internet connection exists. Loads data from file and converts rates based on that
    """

    def __init__(self, path="./mock.json"):
        """
        Constructor

        :param path: Path to the data file. Relative to the py file
        """
        self.path = Path(__file__).parent / path

    def load_data(self):
        """
        Loads the data from the file

        :return: The parsed json data from the file
        """
        with open(self.path) as json_file:
            return json.load(json_file)

    def calculate_rates(self, amount: float, base: str, symbols: List[str]) -> ApiResponse:
        data = self.load_data()
        raw_rates = data['rates']

        if len(symbols) == 0:
            symbols = (['EUR'] + list(data['rates'].keys()))
            symbols.remove(base)

        rates = []

        # File is saved with the base as EUR. Easier conversion
        if base == 'EUR':
            for s in symbols:
                rate = raw_rates[s]
                rates.append(CalculatedRate(s, rate, amount * rate))

        else:
            raw_rates['EUR'] = 1
            # Convert amount to eur
            base_amt = amount / raw_rates[base]
            for s in symbols:
                rate = raw_rates[s]
                rates.append(CalculatedRate(s, rate, base_amt * rate))

        return ApiResponse(amount, base, data['date'], rates)
