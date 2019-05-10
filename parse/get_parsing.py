from time import sleep
import requests
from random import choice, uniform
from bs4 import BeautifulSoup
import datetime

from .models import Flat

def get_html(url, useragent=None, proxy=None):
    r = requests.get(url, headers=useragent, proxies=proxy)
    return r.text


def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')

    pages = soup.find('div', class_='pagination-pages').find_all('a', class_='pagination-page')[-1].get('href')
    total_pages = pages.split('=')[1]

    return int(total_pages)


def get_page_data(html, all_data):
    soup = BeautifulSoup(html, 'lxml')
    ads = soup.find('div', class_='catalog-list').find_all('div', class_='item_table')

    for ad in ads:
        try:
            id_avito = ad.get('id')
        except:
            id_avito = ''

        try:
            title = ad.find('h3', class_='item-description-title').text.strip()
        except:
            title = ''

        try:
            price = ad.find('span', class_='price').text.strip()
        except:
            price = ''

        try:
            address = ad.find('div', class_='description').find('p', class_='address').text.strip().replace(u'\xa0', '')
            # address = ad.find('div', class_='description').find('p', class_='address').text.strip()
        except:
            address = ''

        try:
            url = 'https://www.avito.ru' + ad.find('a', class_='item-description-title-link').get('href')
        except:
            url = ''

        try:
            # date = ad.find('div', class_='data').find('div', class_='js-item-date').text.strip()
            date = ad.find('div', class_='data').find('div', class_='js-item-date')['data-absolute-date']
            # date = date.split('$nbsp')
            date = date.split('\xa0')

            if date[0] == 'Сегодня':
                print('today')
                date = datetime.datetime.today()
            elif date[0] == 'Вчера':
                date = datetime.datetime.yesterday()
            else:
                print(date[0])
                date = (date[0] + ' ' + date[1])


            # date = date.split('$nbsp')
            # date = datetime.datetime.now()
        except:
            date = ''

        # data = {'flat_id': id_avito,
        #         'title': title,
        #         'price': price,
        #         'address': address,
        #         'url': url,
        #         'date_avito': date}

    # Flat.objects.all().delete()

        flat_from_db = Flat.objects.filter(id_avito = id_avito)

        if flat_from_db:
            print('exist')
        else:
            flat = Flat(id_avito = id_avito,
                        title = title,
                        price = price,
                        address = address,
                        url = url,
                        date_avito = date)
            flat.save()
            print('add flat')


def main():
    url = 'https://www.avito.ru/sevastopol/kvartiry/prodam?p=1'
    base_url = 'https://www.avito.ru/sevastopol/kvartiry/prodam?'
    page_part = 'p='

    total_pages = get_total_pages(get_html(url))

    all_data = []
    output = []

    useragents = open('parse/user_agents.txt').read().split('\n')
    proxies = open('parse/proxies').read().split('\n')

    for i in range(1, 2):
    # for i in range(1, total_pages+1):
        sleep(uniform(2,5))

        proxy = {'http': 'http://' + choice(proxies)}
        useragent = {'User-Agent': choice(useragents)}
        print(proxy)

        url_gen = base_url + page_part + str(i)
        html = get_html(url_gen, useragent, proxy)
        data = get_page_data(html, all_data)
        # data.append(data)

    # return data

#
# __ init__ = '__main__':
#     main()
