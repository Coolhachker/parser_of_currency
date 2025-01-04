import requests
from bs4 import BeautifulSoup


def get_list_of_currencies(session: requests.Session=requests.Session()):
    url = 'https://cash.rbc.ru/cash/currency.html'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1.1 Safari/605.1.15'
    }
    response = session.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser_of_currencies_cht')

    list_of_currencies: list = []
    for currency in soup.find_all('div', class_='guide__row js-currency-row'):
        if currency.find_next('div', class_='guide__cell js-currency-uid').text != 'RUB':
            list_of_currencies.append(currency.find_next('div', class_='guide__cell js-currency-uid').text)
        else:
            list_of_currencies.append('RUR')

    return list_of_currencies