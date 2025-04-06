import requests, logging, time

class ExchangeRateService:
    def __init__(self, base_url="https://api.exchangerate-api.com/v4/latest/USD"):
        self.base_url = base_url
        self.logger = self._setup_logger()

    def _setup_logger(self):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        ch = logging.StreamHandler()
        ch.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        logger.addHandler(ch)
        return logger

    def get_rates(self, max_retries=3, retry_delay=2):
        for attempt in range(max_retries):
            try:
                response = requests.get(self.base_url, timeout=10)
                response.raise_for_status()
                return response.json()['rates']
            except requests.exceptions.RequestException as e:
                self.logger.warning(f"Attempt {attempt + 1}/{max_retries}: {e}")
                if attempt < max_retries - 1:
                    time.sleep(retry_delay)
        return None

