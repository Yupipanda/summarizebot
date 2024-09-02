import requests
import lxml
from bs4 import BeautifulSoup
from news.db import PostDB

def parsetech(limit):
    y = 0
    e = 1
    results = []
    while True:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/600.2.5 (KHTML, like Gecko) Version/8.0.2 Safari/600.2.5 (Amazonbot/0.1; +https://developer.amazon.com/support/amazonbot) '
        }
        response = requests.get(f'https://techcrunch.com/page/{e}/', headers).text
        sp = BeautifulSoup(response, 'lxml')
        el1 = sp.find_all('h2', {'class': 'has-link-color wp-block-post-title has-h-5-font-size wp-elements-565fa7bab0152bfdca0217543865c205'})
        for i in el1:
            el2 = i.find('a')
            if PostDB.verify_post(el2.get('href')):
                results.append((el2.get('href'), el2.text))
                y += 1
        e += 1
        if y >= limit:
            for _ in range(y - limit):
                results.pop()
        for w in results:
            PostDB().add_post_ifnexist(el2.get('href'), el2.text)
            print('\n')
        if len(results) == limit:
            break
