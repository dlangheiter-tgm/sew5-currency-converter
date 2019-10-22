from typing import List

from api import ApiResponse
from abc import ABC, abstractmethod


class BaseApi(ABC):
    """
    Common "interface" for the api
    """

    @abstractmethod
    def calculate_rates(self, amount: float, base: str, symbols: List[str]) -> ApiResponse:
        """
        Calculates the rates with the given parameters

        :param amount: Amount in the base currency
        :param base: Base currency
        :param symbols: In what currencies should the amount be converted. If empty, requests all
        :return: An ApiResponse object
        :raise: Exception if an error occoures. Will be displayed by the ui
        """
        pass
