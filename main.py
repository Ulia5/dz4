from converters.converter_factory import ConverterFactory


def main():
    amount = float(input('Введите значение в USD: '))
    factory = ConverterFactory()

    for currency in ["EUR", "GBP", "RUB", "CNY"]:
        converter = factory.get_converter(currency)
        if converter:
            try:
                result = converter.convert(amount)
                print(f"{amount} USD to {currency}: {result:.2f}")
            except ValueError as e:
                print(f"Ошибка для {currency}: {e}")


if __name__ == "__main__":
    main()

