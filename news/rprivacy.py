from news.db import PostDB
import json, requests

def parserprivacy(limit):
    try:
        url = f'https://www.reddit.com/r/privacy/hot.json?sort=new&limit={limit}'
        headers = {
            "User-Agent": "'Mozilla/5.0 (Windows NT 6.2; rv:20.0) Gecko/20121202 Firefox/20.0'"    
        }
        response = requests.get(url, headers=headers)
        data = json.loads(response.text)
        posts = []
        for post in data["data"]["children"]:
            title = post["data"]["title"]
            link = post["data"]["url"]
            values = (link, title)
            posts.append(values)
        if len(posts) != limit:
            for _ in range(0, len(posts) - limit):
                posts.pop()
        print('Данные получены, начинаю проверку ----\n')
        t = 0
        for j in posts:
            if PostDB.verify_post(j[0]):
                print(f'Пост № {t} проверен, добавляю в базу ----\n')
                PostDB().add_post_ifnexist(j[0], j[1])
                print('\n')
                t += 1
    except Exception as ex:
       print(ex)

    
