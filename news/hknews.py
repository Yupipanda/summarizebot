import requests
from bs4 import BeautifulSoup
from news.db import PostDB


def parse_hknews(limit):
    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/128.0.6613.98 Mobile/15E148 Safari/604.1"
    }
    i = 1
    try:
        rr = []
        while True:
            if len(rr) >= limit:
                if len(rr) != limit:
                    for _ in range(-1, len(rr) - 1 - limit):
                        rr.pop()
                break
            print(f'Парсим страницу {i}')
            uri = f'https://news.ycombinator.com/?p={i}'
            resp = requests.get(uri, headers=headers).text
            sp = BeautifulSoup(resp, 'lxml')
            morebtn = sp.find('a', {'class': 'morelink'})
            elements = sp.find_all('span', {'class': 'titleline'})
            for u in elements:
                a = u.find('a')
                if PostDB.verify_post(a.get('href')):
                    rr.append((a.get('href'),a.text))
            if morebtn:
                i += 1
            else:
                break
        print('\nДобавляю данные в базу данных ----\n')
        j = 0
        for x in rr:
            PostDB().add_post_ifnexist(link=x[0], title=x[1])
            j += 1
            print(f'Пост {j} добавлен.\n')
    except Exception as ex:
        print(ex)


