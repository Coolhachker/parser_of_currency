import time
from typing import List
import requests


def get_value_of_currency(currencies: List[str], session: requests.Session=requests.Session()):
    """
    Формат CURRENCY1/CURRENCY2
    :param currencies:
    :param session:
    :return:
    """
    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-encoding': "gzip, deflate, br, zstd",
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }
    list_of_results: list = []
    for currency in currencies:
        url = 'https://cash.rbc.ru/cash/json/converter_currency_rate/?currency_from=%s&currency_to=%s&source=cbrf&sum=1&date=' % (currency.split('/')[0], currency.split('/')[1])
        response = session.get(url=url, headers=headers)
        response_json = response.json()

        list_of_results.append({currency: response_json['data']['sum_result']})
        if len(currencies) > 5: time.sleep(.01)
    return list_of_results


