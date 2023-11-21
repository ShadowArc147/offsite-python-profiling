import requests
import re
import time

import httpx
import asyncio

async def better_count_https_in_web_pages():
    with open('top15USWebsites.txt', 'r', encoding='utf-8') as f:
        urls = [line.strip() for line in f.readlines()]

    async with httpx.AsyncClient() as client:
        tasks = (client.get(url, follow_redirects=True) for url in urls)
        reqs = await asyncio.gather(*tasks)

    htmls = [req.text for req in reqs]

    count_https = 0
    count_http = 0
    for html in htmls:
        count_https += len(re.findall("https://", html))
        count_http += len(re.findall("http://", html))

    print('finished parsing')
    print(f'{count_https=}')
    print(f'{count_http=}')
    print(f'{count_https/count_http=}')


def main():
    
    asyncio.run(better_count_https_in_web_pages())

if __name__ == '__main__':
    main()