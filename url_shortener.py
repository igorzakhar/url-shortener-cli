import argparse
import logging
import os

from urllib.parse import urlparse

import requests

from dotenv import load_dotenv


def shorten_link(token, url):
    api_url = 'https://api-ssl.bitly.com/v4/bitlinks'
    headers = {'Authorization': f'Bearer {token}'}
    payload = {'long_url': url}

    response = requests.post(api_url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()['id']


def count_clicks(token, url):
    parsed_url = urlparse(url)
    link = f'{parsed_url.netloc}/{parsed_url.path}'
    api_url = f'https://api-ssl.bitly.com/v4/bitlinks/{link}/clicks/summary'
    headers = {'Authorization': f'Bearer {token}'}

    response = requests.get(api_url, headers=headers)
    response.raise_for_status()

    return response.json()['total_clicks']


def is_bitlink(token, url):
    parsed_url = urlparse(url)
    net_loc = parsed_url.netloc
    url_path = parsed_url.path
    api_url = f'https://api-ssl.bitly.com/v4/bitlinks/{net_loc}{url_path}'
    headers = {'Authorization': f'Bearer {token}'}

    response = requests.get(api_url, headers=headers)
    return response.ok


def main():
    load_dotenv()

    bitly_token = os.getenv('BITLY_TOKEN')

    parser = argparse.ArgumentParser(
        description='Cокращатель URL-адресов через API сервиса Bitly.'
    )
    parser.add_argument('url', help='Ссылка пользователя')
    args = parser.parse_args()

    if args.url:
        try:
            if not is_bitlink(bitly_token, args.url):
                short_url = shorten_link(bitly_token, args.url)
                print(short_url)
            else:
                click_count = count_clicks(bitly_token, args.url)
                print('Количество переходов по ссылке битли:', click_count)
        except requests.exceptions.HTTPError as error:
            logging.exception(error, exc_info=False)


if __name__ == '__main__':
    main()
