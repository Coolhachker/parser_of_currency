# parser_of_currency
парсер валют

Структура проекта:
parser/currencies.py - в файле содерится функция

```get_list_of_currencies(session: requests.Session=requests.Session())``` для получения UID валют.

parser/value_of_currency.py - в файле содержится функция

```get_value_of_currency(currencies: List[str], session: requests.Session=requests.Session())``` для получения точного значения валюты
