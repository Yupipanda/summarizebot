import requests
import lxml
from bs4 import BeautifulSoup
from news.db import PostDB

def parsehabr(limit):
    e = 1
    y = 0
    results = []
    while True:
        url = f'https://habr.com/ru/feed/page{e}/'
        headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Mobile/15E148 Safari/604.1 '}
        response = requests.get(url, headers).text
        sp = BeautifulSoup(response, 'lxml')
        el1 = sp.find_all('a', {'class': 'tm-title__link'})
        for i in el1:
            text = i.find('span').text
            link = 'https://habr.com' + i.get('href')
            if PostDB.verify_post(link):
                results.append((link, text))
                y += 1
        if y >= limit:
            for _ in range(y-limit):
                results.pop()
        for h in results:
            PostDB().add_post_ifnexist(h[0], h[1])
            print('\n')
        e += 1
        if e == 50 or len(results) == limit:
            break
