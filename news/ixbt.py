import requests
import lxml
from bs4 import BeautifulSoup
from news.db import PostDB

def ixbtparse(limit):
    try:
        url = 'https://www.ixbt.com/news/'
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edg/81.0.416.72"
        }
        response = requests.get(url, headers).text
        soup = BeautifulSoup(response, 'lxml')
        elements = soup.find_all('li', {'class': 'item'})
        elements2 = soup.find_all('strong')
        titles = []
        for e in elements2:
            titles.append(e.text)
        links = []
        for i in elements:
            link = i.find('a').get('href')
            links.append('https://www.ixbt.com' + link)
        results = []
        for _ in range(0, len(links)):
            link = links.pop()
            title = titles.pop()
            values = (link, title)
            results.append(values)
        results = list(reversed(results))
        for _ in range(0, len(results) - limit):
            results.pop()
        for v in results:
            if PostDB.verify_post(v[0]):
                PostDB().add_post_ifnexist(v[0], v[1])
                print('\n')
    except Exception as ex:
        print(ex)
