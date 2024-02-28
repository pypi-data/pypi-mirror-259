import re

import requests
from requests.exceptions import HTTPError

from .base import DolarSource
from .urls import URL_MONITORDOLAR


class MonitorDolarExtractor(DolarSource):
    def __init__(self):
        """
        Initializes the MonitorDolarExtractor instance with the specified driver type.

        Args:
            driver_type (str): Type of driver to use for web scraping.
        """
        self._url = URL_MONITORDOLAR

    def get_dolar_data(self) -> str:
        """
        Retrieves the raw data of the parallel dollar from the MonitorDolar website.

        Returns:
            str: Raw data of the parallel dollar.
        """

        headers = {
            "Host": "api.monitordolarvenezuela.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0",
            "Origin": "https://monitordolarvenezuela.com",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
        }
        try:
            response = requests.get(self._url, headers=headers)
            response.raise_for_status()
            data_json = response.json()
            prices = data_json["result"][0]
            del prices["id"]
            return prices
        except HTTPError as e:
            print(f"Error HTTP: {e.response.status_code}")
            return {}

    def get_dolar_price(self) -> float:
        """
        Retrieves the price of the parallel dollar.

        Returns:
            float: Price of the parallel dollar.
        """
        price = self.clean_data()
        return price["prom_epv"] if len(price) > 0 else None

    def clean_data(self) -> float:
        """
        Cleans the raw data of the parallel dollar and returns the cleaned price.

        Returns:
            float: Cleaned price of the parallel dollar.
        """
        price = self.get_dolar_data()
        if len(price) <= 0:
            return None

        cleaned_prices = {}
        for key, value in price.items():
            cleaned_price_str = re.sub(
                r"[^\d.,]", "", value if value is not None else "0.0"
            )
            cleaned_price_str = cleaned_price_str.replace(",", ".")
            float_cleaned_price = float(cleaned_price_str)
            float_cleaned_price = round(float_cleaned_price, 2)
            cleaned_prices[key] = float_cleaned_price

        return cleaned_prices

    def get_name(self):
        return "MonitorDolar"
