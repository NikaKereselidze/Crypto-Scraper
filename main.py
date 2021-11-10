#! /bin/python3
from bs4 import BeautifulSoup
from requests import get, post
from datetime import datetime
import os

try:

    cryptocurrency = input('''
(1) Bitcoin   - BTC
(2) Ethereum  - ETH
(3) Tron      - TRX
(4) Shiba Inu - SHIB
(5) VeChain   - VET
(6) Dogecoin  - DOGE

Enter Crypto Currency: ''')
    global crypto
    if cryptocurrency == '1':
        crypto = 'bitcoin'
    elif cryptocurrency == '2':
        crypto = 'ethereum'
    elif cryptocurrency == '3':
        crypto = 'tron'
    elif cryptocurrency == '4':
        crypto = 'shiba-inu'
    elif cryptocurrency == '5':
        crypto = 'vechain'
    elif cryptocurrency == '6':
        crypto = 'dogecoin'
    else:
        print('\nEnter a valid value (number)\n')
        exit()
    currency = input('''
(1) USD - $
(2) GEL - ლ

Enter currency: ''')

    if currency == '1':
        while True:
            html = get(f'https://coinmarketcap.com/currencies/{crypto}/')
            soup = BeautifulSoup(html.text, 'lxml')
            price = soup.find('div', class_='priceValue')
            price = price.text
            try:
                os.mkdir('USD')
            except:
                pass
            price = price.replace('$', 'USD ')
            log_file = open(f'USD/{crypto}_usd.csv', 'a+')
            log_file.write(f'{price} at {datetime.now()},\n')
            print('\n'*150, crypto, '-', price)
    elif currency == '2':
        selected_currency = 'gel'
        html = get(f'https://wise.com/gb/currency-converter/usd-to-{selected_currency}-rate')
        soup = BeautifulSoup(html.text, 'lxml')
        usd_to_gel = soup.find('span', class_='text-success').text
        while True:
            html = get(f'https://coinmarketcap.com/currencies/{crypto}/')
            soup = BeautifulSoup(html.text, 'lxml')
            price = soup.find('div', class_='priceValue')
            price = price.text
            price = price.replace('$', '')
            if '.' in price:
                splitted_price = price.split('.')
                print(splitted_price)
                price = splitted_price[0]
                price = price.replace(',', '')
            float_price = float(price) * float(usd_to_gel)
            price = f'GEL {float_price}'
            try:
                os.mkdir('GEL')
            except:
                pass
            log_file = open(f'GEL/{crypto}-{selected_currency}.csv', 'a+')
            log_file.write(f'{price} at {datetime.now()},\n')
            print('\n'*150, crypto, '-', price)
    else:
        print('\nEnter a valid value (number)\n')
        exit()
except KeyboardInterrupt:
    print(' exit()')
    exit()
