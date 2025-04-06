from converters.exchange_rate_service import ExchangeRateService
from converters.usd_eur_converter import UsdToEurConverter
from converters.usd_gbp_converter import UsdToGbpConverter
from converters.usd_rub_converter import UsdToRubConverter
from converters.usd_cny_converter import UsdToCnyConverter

class ConverterFactory:
    def __init__(self):
        self.rate_service = ExchangeRateService()

    def get_converter(self, target_currency: str):
        converters = {
            "EUR": UsdToEurConverter(self.rate_service),
            "GBP": UsdToGbpConverter(self.rate_service),
            "RUB": UsdToRubConverter(self.rate_service),
            "CNY": UsdToCnyConverter(self.rate_service),
        }
        return converters.get(target_currency.upper())

