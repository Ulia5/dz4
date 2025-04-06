from converters.currency_converter import CurrencyConverter
from converters.exchange_rate_service import ExchangeRateService

class UsdToEurConverter(CurrencyConverter):
    def __init__(self, rate_service: ExchangeRateService):
        self.rate_service = rate_service
        self.rates = self.rate_service.get_rates()

    @property
    def target_currency(self):
        return "EUR"

    def convert(self, amount: float) -> float:
        if not self.rates:
            raise ValueError("Rates not loaded")
        return amount * self.rates[self.target_currency]

