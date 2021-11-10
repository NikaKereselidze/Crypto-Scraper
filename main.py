from bs4 import BeautifulSoup
from requests import get, post
from datetime import datetime
import os

try:
    currency = input('''
(1) USD - $
(2) GEL - ლ

Enter currency: ''')

    if currency == '1':
        while True:
            html = get('https://coinmarketcap.com/currencies/shiba-inu/')
            soup = BeautifulSoup(html.text, 'lxml')
            price = soup.find('div', class_='priceValue smallerPrice')
            price = price.text
            try:
                os.mkdir('USD')
            except:
                pass
            price = price.replace('$', 'USD ')
            log_file = open('USD/shib_usd.csv', 'a+')
            log_file.write(f'{price} at {datetime.now()},\n')
            print('\n'*150, price)
    elif currency == '2':
        selected_currency = 'gel'
        html = get(f'https://wise.com/gb/currency-converter/usd-to-{selected_currency}-rate')
        soup = BeautifulSoup(html.text, 'lxml')
        usd_to_gel = soup.find('span', class_='text-success').text
        while True:
            html = get('https://coinmarketcap.com/currencies/shiba-inu/')
            soup = BeautifulSoup(html.text, 'lxml')
            price = soup.find('div', class_='priceValue smallerPrice')
            price = price.text
            price = price.replace('$', '')
            print(float(price), float(usd_to_gel))
            float_price = float(price) * float(usd_to_gel)
            price = f'GEL {float_price}'
            try:
                os.mkdir('GEL')
            except:
                pass
            log_file = open(f'GEL/shib_{selected_currency}.csv', 'a+')
            log_file.write(f'{price} at {datetime.now()},\n')
            print('\n'*150, price)
except KeyboardInterrupt:
    print(' exit()')
    exit()