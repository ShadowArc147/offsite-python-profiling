import requests
import re
import time

import httpx
import asyncio


def count_https_in_web_pages():
    with open('top15USWebsites.txt', 'r', encoding='utf-8') as f:
        urls = [line.strip() for line in f.readlines()]

    htmls = []
    for url in urls:
        htmls = htmls + [requests.get(url).text]

    count_https = 0
    count_http = 0
    for html in htmls:
        count_https += len(re.findall("https://", html))
        count_http += len(re.findall("http://", html))

    print('finished parsing')
    time.sleep(2.0)
    print(f'{count_https=}')
    print(f'{count_http=}')
    print(f'{count_https/count_http=}')

def main():
    
    count_https_in_web_pages()

if __name__ == '__main__':
    main()