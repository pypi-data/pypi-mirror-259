import json
import re

import requests
from requests.exceptions import HTTPError

from .base import DolarSource
from .urls import URL_DOLARTODAY


class DolarTodayExtractor(DolarSource):
    """
    Class to extract parallel dollar data from the DolarToday website.
    """

    def __init__(self):
        """
        Initializes the DolarTodayExtractor instance with the specified driver type.

        Args:
            driver_type (str): Type of driver to use for web scraping.
        """
        self._url = URL_DOLARTODAY

    def get_dolar_data(self) -> json:
        """
        Retrieves the raw data of the parallel dollar from the DolarToday website.

        Returns:
            str: Raw data of the parallel dollar.
        """

        try:
            data = {"action": "dt_currency_calculator_handler", "amount": "1"}
            response = requests.post(self._url, data=data)
            response.raise_for_status()
            return response.json()
        except HTTPError as e:
            print(f"Error HTTP: {e.response.status_code}")
            return {}

    def clean_data(self) -> float:
        """
        Cleans the raw data of the parallel dollar and returns the cleaned price.

        Returns:
            float: Cleaned price of the parallel dollar.
        """
        data = self.get_dolar_data()

        if len(data) <= 0:
            return 0

        cleaned_prices = {}
        for key, price in data.items():
            cleaned_price_str = re.sub(r"[^\d.,]", "", price)
            cleaned_price_str = cleaned_price_str.replace(",", ".")
            float_cleaned_price = float(cleaned_price_str[1:])
            float_cleaned_price = round(float_cleaned_price, 2)
            cleaned_prices[key] = float_cleaned_price

        return cleaned_prices

    def get_dolar_price(self) -> float:
        """
        Retrieves the price of the parallel dollar.

        Returns:
            float: Price of the parallel dollar.
        """
        price = self.clean_data()
        if price != 0:
            return price["Dólar Paralelo"] if len(price) > 0 else None
        return None

    def get_name(self):
        return "DolarToday"
