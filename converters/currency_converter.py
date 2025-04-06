from abc import ABC, abstractmethod

class CurrencyConverter(ABC):
    @property
    @abstractmethod
    def target_currency(self) -> str:
        """Код целевой валюты (например, 'EUR')."""
        pass

    @abstractmethod
    def convert(self, amount: float) -> float:
        """Конвертирует сумму из USD в целевую валюту."""
        pass

