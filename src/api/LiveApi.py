from typing import List
import requests

from api.ApiResponse import ApiResponse
from api.BaseApi import BaseApi
from api.CalculatedRate import CalculatedRate


class LiveApi(BaseApi):
    """
    Api that works with the api on exchangeratesapi.io
    """

    def __init__(self, url="https://api.exchangeratesapi.io/latest"):
        self.url = url

    def request_rates(self, base: str, symbols: List[str]):
        """
        Requests the rates from the API

        :param base: Base currency
        :param symbols: What currencies to query
        :return: The parsed data from the API
        """
        params = {"base": base, "symbols": ','.join(symbols)}
        resp = ""
        try:
            resp = requests.get(self.url, params=params)
        except Exception as e:
            print(e)
            raise Exception("No internet connection. Establish a internet connection or uncheck live-data")
        json = resp.json()
        if resp.status_code != 200:
            raise Exception(json['error'])

        return json

    def calculate_rates(self, amount: float, base: str, symbols: List[str]) -> ApiResponse:
        res = self.request_rates(base, symbols)
        raw_rates = res['rates']
        rates = []

        # transform dict to Rate array
        for s in raw_rates.keys():
            rates.append(CalculatedRate(s, raw_rates[s], amount * raw_rates[s]))

        return ApiResponse(amount, base, res['date'], rates)
