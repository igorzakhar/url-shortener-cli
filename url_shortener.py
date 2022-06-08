import logging
import os

import requests

from dotenv import load_dotenv


def shorten_link(token, url):
    api_url = 'https://api-ssl.bitly.com/v4/bitlinks'
    headers = {'Authorization': f'Bearer {token}'}
    payload = {'long_url': url}

    response = requests.post(api_url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()['id']


def main():
    load_dotenv()

    bitly_token = os.getenv('BITLY_TOKEN')

    long_url = 'http://dvmn.org/'
    try:
        print('Битлинк', shorten_link(bitly_token, long_url))
    except requests.exceptions.HTTPError as error:
        logging.exception(error, exc_info=False)


if __name__ == '__main__':
    main()
